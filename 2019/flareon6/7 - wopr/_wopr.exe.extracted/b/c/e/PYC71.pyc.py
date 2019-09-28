# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: socketserver.py
"""Generic socket server classes.

This module tries to capture the various aspects of defining a server:

For socket-based servers:

- address family:
        - AF_INET{,6}: IP (Internet Protocol) sockets (default)
        - AF_UNIX: Unix domain sockets
        - others, e.g. AF_DECNET are conceivable (see <socket.h>
- socket type:
        - SOCK_STREAM (reliable stream, e.g. TCP)
        - SOCK_DGRAM (datagrams, e.g. UDP)

For request-based servers (including socket-based):

- client address verification before further looking at the request
        (This is actually a hook for any processing that needs to look
         at the request before anything else, e.g. logging)
- how to handle multiple requests:
        - synchronous (one request is handled at a time)
        - forking (each request is handled by a new process)
        - threading (each request is handled by a new thread)

The classes in this module favor the server type that is simplest to
write: a synchronous TCP/IP server.  This is bad class design, but
save some typing.  (There's also the issue that a deep class hierarchy
slows down method lookups.)

There are five classes in an inheritance diagram, four of which represent
synchronous servers of four types:

        +------------+
        | BaseServer |
        +------------+
              |
              v
        +-----------+        +------------------+
        | TCPServer |------->| UnixStreamServer |
        +-----------+        +------------------+
              |
              v
        +-----------+        +--------------------+
        | UDPServer |------->| UnixDatagramServer |
        +-----------+        +--------------------+

Note that UnixDatagramServer derives from UDPServer, not from
UnixStreamServer -- the only difference between an IP and a Unix
stream server is the address family, which is simply repeated in both
unix server classes.

Forking and threading versions of each type of server can be created
using the ForkingMixIn and ThreadingMixIn mix-in classes.  For
instance, a threading UDP server class is created as follows:

        class ThreadingUDPServer(ThreadingMixIn, UDPServer): pass

The Mix-in class must come first, since it overrides a method defined
in UDPServer! Setting the various member variables also changes
the behavior of the underlying server mechanism.

To implement a service, you must derive a class from
BaseRequestHandler and redefine its handle() method.  You can then run
various versions of the service by combining one of the server classes
with your request handler class.

The request handler class must be different for datagram or stream
services.  This can be hidden by using the request handler
subclasses StreamRequestHandler or DatagramRequestHandler.

Of course, you still have to use your head!

For instance, it makes no sense to use a forking server if the service
contains state in memory that can be modified by requests (since the
modifications in the child process would never reach the initial state
kept in the parent process and passed to each child).  In this case,
you can use a threading server, but you will probably have to use
locks to avoid two requests that come in nearly simultaneous to apply
conflicting changes to the server state.

On the other hand, if you are building e.g. an HTTP server, where all
data is stored externally (e.g. in the file system), a synchronous
class will essentially render the service "deaf" while one request is
being handled -- which may be for a very long time if a client is slow
to read all the data it has requested.  Here a threading or forking
server is appropriate.

In some cases, it may be appropriate to process part of a request
synchronously, but to finish processing in a forked child depending on
the request data.  This can be implemented by using a synchronous
server and doing an explicit fork in the request handler class
handle() method.

Another approach to handling multiple simultaneous requests in an
environment that supports neither threads nor fork (or where these are
too expensive or inappropriate for the service) is to maintain an
explicit table of partially finished requests and to use a selector to
decide which request to work on next (or whether to handle a new
incoming request).  This is particularly important for stream services
where each client can potentially be connected for a long time (if
threads or subprocesses cannot be used).

Future work:
- Standard classes for Sun RPC (which uses either UDP or TCP)
- Standard mix-in classes to implement various authentication
  and encryption schemes

XXX Open problems:
- What to do with out-of-band data?

BaseServer:
- split generic "request" functionality out into BaseServer class.
  Copyright (C) 2000  Luke Kenneth Casson Leighton <lkcl@samba.org>

  example: read entries from a SQL database (requires overriding
  get_request() to return a table entry from the database).
  entry is processed by a RequestHandlerClass.

"""
__version__ = '0.4'
import socket, selectors, os, sys, threading
from io import BufferedIOBase
from time import monotonic as time
__all__ = [
 'BaseServer', 'TCPServer', 'UDPServer',
 'ThreadingUDPServer', 'ThreadingTCPServer',
 'BaseRequestHandler', 'StreamRequestHandler',
 'DatagramRequestHandler', 'ThreadingMixIn']
if hasattr(os, 'fork'):
    __all__.extend(['ForkingUDPServer', 'ForkingTCPServer', 'ForkingMixIn'])
if hasattr(socket, 'AF_UNIX'):
    __all__.extend(['UnixStreamServer', 'UnixDatagramServer',
     'ThreadingUnixStreamServer',
     'ThreadingUnixDatagramServer'])
if hasattr(selectors, 'PollSelector'):
    _ServerSelector = selectors.PollSelector
else:
    _ServerSelector = selectors.SelectSelector

class BaseServer:
    r"""'Base class for server classes.\n\n    Methods for the caller:\n\n    - __init__(server_address, RequestHandlerClass)\n    - serve_forever(poll_interval=0.5)\n    - shutdown()\n    - handle_request()  # if you do not use serve_forever()\n    - fileno() -> int   # for selector\n\n    Methods that may be overridden:\n\n    - server_bind()\n    - server_activate()\n    - get_request() -> request, client_address\n    - handle_timeout()\n    - verify_request(request, client_address)\n    - server_close()\n    - process_request(request, client_address)\n    - shutdown_request(request)\n    - close_request(request)\n    - service_actions()\n    - handle_error()\n\n    Methods for derived classes:\n\n    - finish_request(request, client_address)\n\n    Class variables that may be overridden by derived classes or\n    instances:\n\n    - timeout\n    - address_family\n    - socket_type\n    - allow_reuse_address\n\n    Instance variables:\n\n    - RequestHandlerClass\n    - socket\n\n    '"""
    timeout = None

    def __init__(self, server_address, RequestHandlerClass):
        """Constructor.  May be extended, do not override."""
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self._BaseServer__is_shut_down = threading.Event()
        self._BaseServer__shutdown_request = False

    def server_activate(self):
        """Called by constructor to activate the server.

        May be overridden.

        """
        pass

    def serve_forever(self, poll_interval=0.5):
        """Handle one request at a time until shutdown.

        Polls for shutdown every poll_interval seconds. Ignores
        self.timeout. If you need to do periodic tasks, do them in
        another thread.
        """
        self._BaseServer__is_shut_down.clear()
        try:
            with _ServerSelector() as (selector):
                selector.register(self, selectors.EVENT_READ)
                while 1:
                    if not self._BaseServer__shutdown_request:
                        ready = selector.select(poll_interval)
                        if self._BaseServer__shutdown_request:
                            break
                        if ready:
                            self._handle_request_noblock()
                        self.service_actions()

        finally:
            self._BaseServer__shutdown_request = False
            self._BaseServer__is_shut_down.set()

    def shutdown(self):
        """Stops the serve_forever loop.

        Blocks until the loop has finished. This must be called while
        serve_forever() is running in another thread, or it will
        deadlock.
        """
        self._BaseServer__shutdown_request = True
        self._BaseServer__is_shut_down.wait()

    def service_actions(self):
        """Called by the serve_forever() loop.

        May be overridden by a subclass / Mixin to implement any code that
        needs to be run during the loop.
        """
        pass

    def handle_request(self):
        """Handle one request, possibly blocking.

        Respects self.timeout.
        """
        timeout = self.socket.gettimeout()
        if timeout is None:
            timeout = self.timeout
        elif self.timeout is not None:
            timeout = min(timeout, self.timeout)
        else:
            if timeout is not None:
                deadline = time() + timeout
            with _ServerSelector() as (selector):
                selector.register(self, selectors.EVENT_READ)
                while 1:
                    ready = selector.select(timeout)
                    if ready:
                        return self._handle_request_noblock()
                    if timeout is not None:
                        timeout = deadline - time()
                        if timeout < 0:
                            return self.handle_timeout()

    def _handle_request_noblock(self):
        """Handle one request, without blocking.

        I assume that selector.select() has returned that the socket is
        readable before this function was called, so there should be no risk of
        blocking in get_request().
        """
        try:
            request, client_address = self.get_request()
        except OSError:
            return
        else:
            if self.verify_request(request, client_address):
                try:
                    self.process_request(request, client_address)
                except Exception:
                    self.handle_error(request, client_address)
                    self.shutdown_request(request)
                except:
                    self.shutdown_request(request)
                    raise

            else:
                self.shutdown_request(request)

    def handle_timeout(self):
        """Called if no new request arrives within self.timeout.

        Overridden by ForkingMixIn.
        """
        pass

    def verify_request(self, request, client_address):
        """Verify the request.  May be overridden.

        Return True if we should proceed with this request.

        """
        return True

    def process_request(self, request, client_address):
        """Call finish_request.

        Overridden by ForkingMixIn and ThreadingMixIn.

        """
        self.finish_request(request, client_address)
        self.shutdown_request(request)

    def server_close(self):
        """Called to clean-up the server.

        May be overridden.

        """
        pass

    def finish_request(self, request, client_address):
        """Finish one request by instantiating RequestHandlerClass."""
        self.RequestHandlerClass(request, client_address, self)

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request."""
        pass

    def handle_error(self, request, client_address):
        """Handle an error gracefully.  May be overridden.

        The default is to print a traceback and continue.

        """
        print('----------------------------------------', file=(sys.stderr))
        print('Exception happened during processing of request from', client_address,
          file=(sys.stderr))
        import traceback
        traceback.print_exc()
        print('----------------------------------------', file=(sys.stderr))

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.server_close()


class TCPServer(BaseServer):
    """"Base class for various socket-based server classes.\\n\\n    Defaults to synchronous IP stream (i.e., TCP).\\n\\n    Methods for the caller:\\n\\n    - __init__(server_address, RequestHandlerClass, bind_and_activate=True)\\n    - serve_forever(poll_interval=0.5)\\n    - shutdown()\\n    - handle_request()  # if you don't use serve_forever()\\n    - fileno() -> int   # for selector\\n\\n    Methods that may be overridden:\\n\\n    - server_bind()\\n    - server_activate()\\n    - get_request() -> request, client_address\\n    - handle_timeout()\\n    - verify_request(request, client_address)\\n    - process_request(request, client_address)\\n    - shutdown_request(request)\\n    - close_request(request)\\n    - handle_error()\\n\\n    Methods for derived classes:\\n\\n    - finish_request(request, client_address)\\n\\n    Class variables that may be overridden by derived classes or\\n    instances:\\n\\n    - timeout\\n    - address_family\\n    - socket_type\\n    - request_queue_size (only for stream sockets)\\n    - allow_reuse_address\\n\\n    Instance variables:\\n\\n    - server_address\\n    - RequestHandlerClass\\n    - socket\\n\\n    \""""
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 5
    allow_reuse_address = False

    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        BaseServer.__init__(self, server_address, RequestHandlerClass)
        self.socket = socket.socket(self.address_family, self.socket_type)
        if bind_and_activate:
            pass
        try:
            self.server_bind()
            self.server_activate()
        except:
            self.server_close()
            raise

    def server_bind(self):
        """Called by constructor to bind the socket.

        May be overridden.

        """
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_activate(self):
        """Called by constructor to activate the server.

        May be overridden.

        """
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        """Called to clean-up the server.

        May be overridden.

        """
        self.socket.close()

    def fileno(self):
        """Return socket file number.

        Interface required by selector.

        """
        return self.socket.fileno()

    def get_request(self):
        """Get the request and client address from the socket.

        May be overridden.

        """
        return self.socket.accept()

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        try:
            request.shutdown(socket.SHUT_WR)
        except OSError:
            pass

        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request."""
        request.close()


class UDPServer(TCPServer):
    """'UDP server class.'"""
    allow_reuse_address = False
    socket_type = socket.SOCK_DGRAM
    max_packet_size = 8192

    def get_request(self):
        data, client_addr = self.socket.recvfrom(self.max_packet_size)
        return (
         (
          data, self.socket), client_addr)

    def server_activate(self):
        pass

    def shutdown_request(self, request):
        self.close_request(request)

    def close_request(self, request):
        pass


if hasattr(os, 'fork'):

    class ForkingMixIn:
        """'Mix-in class to handle each request in a new process.'"""
        timeout = 300
        active_children = None
        max_children = 40
        block_on_close = True

        def collect_children(self, *, blocking=False):
            """Internal routine to wait for children that have exited."""
            if self.active_children is None:
                return
            while 1:
                if len(self.active_children) >= self.max_children:
                    try:
                        pid, _ = os.waitpid(-1, 0)
                        self.active_children.discard(pid)
                    except ChildProcessError:
                        self.active_children.clear()
                    except OSError:
                        break

            for pid in self.active_children.copy():
                try:
                    flags = 0 if blocking else os.WNOHANG
                    pid, _ = os.waitpid(pid, flags)
                    self.active_children.discard(pid)
                except ChildProcessError:
                    self.active_children.discard(pid)
                except OSError:
                    pass

        def handle_timeout(self):
            """Wait for zombies after self.timeout seconds of inactivity.

            May be extended, do not override.
            """
            self.collect_children()

        def service_actions(self):
            """Collect the zombie child processes regularly in the ForkingMixIn.

            service_actions is called in the BaseServer's serve_forver loop.
            """
            self.collect_children()

        def process_request(self, request, client_address):
            """Fork a new subprocess to process the request."""
            pid = os.fork()
            if pid:
                if self.active_children is None:
                    self.active_children = set()
                self.active_children.add(pid)
                self.close_request(request)
                return
            status = 1
            try:
                try:
                    self.finish_request(request, client_address)
                    status = 0
                except Exception:
                    self.handle_error(request, client_address)

            finally:
                try:
                    self.shutdown_request(request)
                finally:
                    os._exit(status)

        def server_close(self):
            super().server_close()
            self.collect_children(blocking=(self.block_on_close))


class ThreadingMixIn:
    """'Mix-in class to handle each request in a new thread.'"""
    daemon_threads = False
    block_on_close = True
    _threads = None

    def process_request_thread(self, request, client_address):
        """Same as in BaseServer but as a thread.

        In addition, exception handling is done here.

        """
        try:
            try:
                self.finish_request(request, client_address)
            except Exception:
                self.handle_error(request, client_address)

        finally:
            self.shutdown_request(request)

    def process_request(self, request, client_address):
        """Start a new thread to process the request."""
        t = threading.Thread(target=(self.process_request_thread), args=(
         request, client_address))
        t.daemon = self.daemon_threads
        if not t.daemon:
            if self.block_on_close:
                if self._threads is None:
                    self._threads = []
                self._threads.append(t)
            t.start()

    def server_close(self):
        super().server_close()
        if self.block_on_close:
            threads = self._threads
            self._threads = None
        if threads:
            for thread in threads:
                thread.join()


if hasattr(os, 'fork'):

    class ForkingUDPServer(ForkingMixIn, UDPServer):
        pass


    class ForkingTCPServer(ForkingMixIn, TCPServer):
        pass


class ThreadingUDPServer(ThreadingMixIn, UDPServer):
    pass


class ThreadingTCPServer(ThreadingMixIn, TCPServer):
    pass


if hasattr(socket, 'AF_UNIX'):

    class UnixStreamServer(TCPServer):
        address_family = socket.AF_UNIX


    class UnixDatagramServer(UDPServer):
        address_family = socket.AF_UNIX


    class ThreadingUnixStreamServer(ThreadingMixIn, UnixStreamServer):
        pass


    class ThreadingUnixDatagramServer(ThreadingMixIn, UnixDatagramServer):
        pass


class BaseRequestHandler:
    r"""'Base class for request handler classes.\n\n    This class is instantiated for each request to be handled.  The\n    constructor sets the instance variables request, client_address\n    and server, and then calls the handle() method.  To implement a\n    specific service, all you need to do is to derive a class which\n    defines a handle() method.\n\n    The handle() method can find the request as self.request, the\n    client address as self.client_address, and the server (in case it\n    needs access to per-server information) as self.server.  Since a\n    separate instance is created for each request, the handle() method\n    can define other arbitrary instance variables.\n\n    '"""

    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()

    def setup(self):
        pass

    def handle(self):
        pass

    def finish(self):
        pass


class StreamRequestHandler(BaseRequestHandler):
    """'Define self.rfile and self.wfile for stream sockets.'"""
    rbufsize = -1
    wbufsize = 0
    timeout = None
    disable_nagle_algorithm = False

    def setup(self):
        self.connection = self.request
        if self.timeout is not None:
            self.connection.settimeout(self.timeout)
        if self.disable_nagle_algorithm:
            self.connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        self.rfile = self.connection.makefile('rb', self.rbufsize)
        if self.wbufsize == 0:
            self.wfile = _SocketWriter(self.connection)
        else:
            self.wfile = self.connection.makefile('wb', self.wbufsize)

    def finish(self):
        if not self.wfile.closed:
            try:
                self.wfile.flush()
            except socket.error:
                pass

            self.wfile.close()
            self.rfile.close()


class _SocketWriter(BufferedIOBase):
    r"""'Simple writable BufferedIOBase implementation for a socket\n\n    Does not hold data in a buffer, avoiding any need to call flush().'"""

    def __init__(self, sock):
        self._sock = sock

    def writable(self):
        return True

    def write(self, b):
        self._sock.sendall(b)
        with memoryview(b) as (view):
            return view.nbytes

    def fileno(self):
        return self._sock.fileno()


class DatagramRequestHandler(BaseRequestHandler):
    """'Define self.rfile and self.wfile for datagram sockets.'"""

    def setup(self):
        from io import BytesIO
        self.packet, self.socket = self.request
        self.rfile = BytesIO(self.packet)
        self.wfile = BytesIO()

    def finish(self):
        self.socket.sendto(self.wfile.getvalue(), self.client_address)