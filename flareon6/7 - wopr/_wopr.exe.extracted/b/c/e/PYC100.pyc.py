# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: http\client.py
r"""HTTP/1.1 client library

<intro stuff goes here>
<other stuff, too>

HTTPConnection goes through a number of "states", which define when a client
may legally make another request or fetch the response for a particular
request. This diagram details these state transitions:

    (null)
      |
      | HTTPConnection()
      v
    Idle
      |
      | putrequest()
      v
    Request-started
      |
      | ( putheader() )*  endheaders()
      v
    Request-sent
      |\_____________________________
      |                              | getresponse() raises
      | response = getresponse()     | ConnectionError
      v                              v
    Unread-response                Idle
    [Response-headers-read]
      |\____________________
      |                     |
      | response.read()     | putrequest()
      v                     v
    Idle                  Req-started-unread-response
                     ______/|
                   /        |
   response.read() |        | ( putheader() )*  endheaders()
                   v        v
       Request-started    Req-sent-unread-response
                            |
                            | response.read()
                            v
                          Request-sent

This diagram presents the following rules:
  -- a second request may not be started until {response-headers-read}
  -- a response [object] cannot be retrieved until {request-sent}
  -- there is no differentiation between an unread response body and a
     partially read response body

Note: this enforcement is applied by the HTTPConnection class. The
      HTTPResponse class does not enforce this state machine, which
      implies sophisticated clients may accelerate the request/response
      pipeline. Caution should be taken, though: accelerating the states
      beyond the above pattern may imply knowledge of the server's
      connection-close behavior for certain requests. For example, it
      is impossible to tell whether the server will close the connection
      UNTIL the response headers have been read; this means that further
      requests cannot be placed into the pipeline until it is known that
      the server will NOT be closing the connection.

Logical State                  __state            __response
-------------                  -------            ----------
Idle                           _CS_IDLE           None
Request-started                _CS_REQ_STARTED    None
Request-sent                   _CS_REQ_SENT       None
Unread-response                _CS_IDLE           <response_class>
Req-started-unread-response    _CS_REQ_STARTED    <response_class>
Req-sent-unread-response       _CS_REQ_SENT       <response_class>
"""
import email.parser, email.message, http, io, re, socket, collections.abc
from urllib.parse import urlsplit
__all__ = [
 'HTTPResponse', 'HTTPConnection',
 'HTTPException', 'NotConnected', 'UnknownProtocol',
 'UnknownTransferEncoding', 'UnimplementedFileMode',
 'IncompleteRead', 'InvalidURL', 'ImproperConnectionState',
 'CannotSendRequest', 'CannotSendHeader', 'ResponseNotReady',
 'BadStatusLine', 'LineTooLong', 'RemoteDisconnected', 'error',
 'responses']
HTTP_PORT = 80
HTTPS_PORT = 443
_UNKNOWN = 'UNKNOWN'
_CS_IDLE = 'Idle'
_CS_REQ_STARTED = 'Request-started'
_CS_REQ_SENT = 'Request-sent'
globals().update(http.HTTPStatus.__members__)
responses = {v:v.phrase for v in http.HTTPStatus.__members__.values()}
MAXAMOUNT = 1048576
_MAXLINE = 65536
_MAXHEADERS = 100
_is_legal_header_name = re.compile('[^:\\s][^:\\r\\n]*').fullmatch
_is_illegal_header_value = re.compile('\\n(?![ \\t])|\\r(?![ \\t\\n])').search
_METHODS_EXPECTING_BODY = {
 'PATCH', 'POST', 'PUT'}

def _encode(data, name='data'):
    """Call data.encode("latin-1") but show a better error message."""
    try:
        return data.encode('latin-1')
    except UnicodeEncodeError as err:
        try:
            raise UnicodeEncodeError(err.encoding, err.object, err.start, err.end, "%s (%.20r) is not valid Latin-1. Use %s.encode('utf-8') if you want to send it encoded in UTF-8." % (
             name.title(), data[err.start:err.end], name)) from None
        finally:
            err = None
            del err


class HTTPMessage(email.message.Message):

    def getallmatchingheaders(self, name):
        """Find all header lines matching a given header name.

        Look through the list of headers and find all lines matching a given
        header name (and their continuation lines).  A list of the lines is
        returned, without interpretation.  If the header does not occur, an
        empty list is returned.  If the header occurs multiple times, all
        occurrences are returned.  Case is not important in the header name.

        """
        name = name.lower() + ':'
        n = len(name)
        lst = []
        hit = 0
        for line in self.keys():
            if line[:n].lower() == name:
                hit = 1
            elif not line[:1].isspace():
                hit = 0
            if hit:
                lst.append(line)

        return lst


def parse_headers(fp, _class=HTTPMessage):
    """Parses only RFC2822 headers from a file pointer.

    email Parser wants to see strings rather than bytes.
    But a TextIOWrapper around self.rfile would buffer too many bytes
    from the stream, bytes which we later need to read as bytes.
    So we read the correct bytes here, as bytes, for email Parser
    to parse.

    """
    headers = []
    while 1:
        line = fp.readline(_MAXLINE + 1)
        if len(line) > _MAXLINE:
            raise LineTooLong('header line')
        headers.append(line)
        if len(headers) > _MAXHEADERS:
            raise HTTPException('got more than %d headers' % _MAXHEADERS)
        if line in ('\r\n', '\n', ''):
            break

    hstring = ''.join(headers).decode('iso-8859-1')
    return email.parser.Parser(_class=_class).parsestr(hstring)


class HTTPResponse(io.BufferedIOBase):

    def __init__(self, sock, debuglevel=0, method=None, url=None):
        self.fp = sock.makefile('rb')
        self.debuglevel = debuglevel
        self._method = method
        self.headers = self.msg = None
        self.version = _UNKNOWN
        self.status = _UNKNOWN
        self.reason = _UNKNOWN
        self.chunked = _UNKNOWN
        self.chunk_left = _UNKNOWN
        self.length = _UNKNOWN
        self.will_close = _UNKNOWN

    def _read_status(self):
        line = str(self.fp.readline(_MAXLINE + 1), 'iso-8859-1')
        if len(line) > _MAXLINE:
            raise LineTooLong('status line')
        if self.debuglevel > 0:
            print('reply:', repr(line))
        if not line:
            raise RemoteDisconnected('Remote end closed connection without response')
        try:
            version, status, reason = line.split(None, 2)
        except ValueError:
            try:
                version, status = line.split(None, 1)
                reason = ''
            except ValueError:
                version = ''

        if not version.startswith('HTTP/'):
            self._close_conn()
            raise BadStatusLine(line)
        try:
            status = int(status)
            if status < 100 or status > 999:
                raise BadStatusLine(line)
        except ValueError:
            raise BadStatusLine(line)

        return (version, status, reason)

    def begin--- This code section failed: ---

 290       0  LOAD_FAST                'self'
           2  LOAD_ATTR                headers
           4  LOAD_CONST               None
           6  COMPARE_OP               is-not
           8  POP_JUMP_IF_FALSE    14  'to 14'

 292      10  LOAD_CONST               None
          12  RETURN_END_IF    
        14_0  COME_FROM             8  '8'

 295      14  SETUP_LOOP          120  'to 120'

 296      16  LOAD_FAST                'self'
          18  LOAD_METHOD              _read_status
          20  CALL_METHOD_0         0  ''
          22  UNPACK_SEQUENCE_3     3 
          24  STORE_FAST               'version'
          26  STORE_FAST               'status'
          28  STORE_FAST               'reason'

 297      30  LOAD_FAST                'status'
          32  LOAD_GLOBAL              CONTINUE
          34  COMPARE_OP               !=
          36  POP_JUMP_IF_FALSE    40  'to 40'

 298      38  BREAK_LOOP       
        40_0  COME_FROM            36  '36'

 300      40  SETUP_LOOP          116  'to 116'

 301      42  LOAD_FAST                'self'
          44  LOAD_ATTR                fp
          46  LOAD_METHOD              readline
          48  LOAD_GLOBAL              _MAXLINE
          50  LOAD_CONST               1
          52  BINARY_ADD       
          54  CALL_METHOD_1         1  ''
          56  STORE_FAST               'skip'

 302      58  LOAD_GLOBAL              len
          60  LOAD_FAST                'skip'
          62  CALL_FUNCTION_1       1  ''
          64  LOAD_GLOBAL              _MAXLINE
          66  COMPARE_OP               >
          68  POP_JUMP_IF_FALSE    78  'to 78'

 303      70  LOAD_GLOBAL              LineTooLong
          72  LOAD_STR                 'header line'
          74  CALL_FUNCTION_1       1  ''
          76  RAISE_VARARGS_1       1  ''
        78_0  COME_FROM            68  '68'

 304      78  LOAD_FAST                'skip'
          80  LOAD_METHOD              strip
          82  CALL_METHOD_0         0  ''
          84  STORE_FAST               'skip'

 305      86  LOAD_FAST                'skip'
          88  POP_JUMP_IF_TRUE     92  'to 92'

 306      90  BREAK_LOOP       
        92_0  COME_FROM            88  '88'

 307      92  LOAD_FAST                'self'
          94  LOAD_ATTR                debuglevel
          96  LOAD_CONST               0
          98  COMPARE_OP               >
         100  POP_JUMP_IF_FALSE    42  'to 42'

 308     102  LOAD_GLOBAL              print
         104  LOAD_STR                 'header:'
         106  LOAD_FAST                'skip'
         108  CALL_FUNCTION_2       2  ''
         110  POP_TOP          
         112  JUMP_BACK            42  'to 42'
         114  POP_BLOCK        
       116_0  COME_FROM_LOOP       40  '40'
         116  JUMP_BACK            16  'to 16'
         118  POP_BLOCK        
       120_0  COME_FROM_LOOP       14  '14'

 310     120  LOAD_FAST                'status'
         122  DUP_TOP          
         124  LOAD_FAST                'self'
         126  STORE_ATTR               code
         128  LOAD_FAST                'self'
         130  STORE_ATTR               status

 311     132  LOAD_FAST                'reason'
         134  LOAD_METHOD              strip
         136  CALL_METHOD_0         0  ''
         138  LOAD_FAST                'self'
         140  STORE_ATTR               reason

 312     142  LOAD_FAST                'version'
         144  LOAD_CONST               ('HTTP/1.0', 'HTTP/0.9')
         146  COMPARE_OP               in
         148  POP_JUMP_IF_FALSE   158  'to 158'

 314     150  LOAD_CONST               10
         152  LOAD_FAST                'self'
         154  STORE_ATTR               version
         156  JUMP_FORWARD        184  'to 184'
         158  ELSE                     '184'

 315     158  LOAD_FAST                'version'
         160  LOAD_METHOD              startswith
         162  LOAD_STR                 'HTTP/1.'
         164  CALL_METHOD_1         1  ''
         166  POP_JUMP_IF_FALSE   176  'to 176'

 316     168  LOAD_CONST               11
         170  LOAD_FAST                'self'
         172  STORE_ATTR               version
         174  JUMP_FORWARD        184  'to 184'
         176  ELSE                     '184'

 318     176  LOAD_GLOBAL              UnknownProtocol
         178  LOAD_FAST                'version'
         180  CALL_FUNCTION_1       1  ''
         182  RAISE_VARARGS_1       1  ''
       184_0  COME_FROM           174  '174'
       184_1  COME_FROM           156  '156'

 320     184  LOAD_GLOBAL              parse_headers
         186  LOAD_FAST                'self'
         188  LOAD_ATTR                fp
         190  CALL_FUNCTION_1       1  ''
         192  DUP_TOP          
         194  LOAD_FAST                'self'
         196  STORE_ATTR               headers
         198  LOAD_FAST                'self'
         200  STORE_ATTR               msg

 322     202  LOAD_FAST                'self'
         204  LOAD_ATTR                debuglevel
         206  LOAD_CONST               0
         208  COMPARE_OP               >
         210  POP_JUMP_IF_FALSE   252  'to 252'

 323     212  SETUP_LOOP          252  'to 252'
         214  LOAD_FAST                'self'
         216  LOAD_ATTR                headers
         218  GET_ITER         
         220  FOR_ITER            250  'to 250'
         222  STORE_FAST               'hdr'

 324     224  LOAD_GLOBAL              print
         226  LOAD_STR                 'header:'
         228  LOAD_FAST                'hdr'
         230  LOAD_STR                 ':'
         232  BINARY_ADD       
         234  LOAD_FAST                'self'
         236  LOAD_ATTR                headers
         238  LOAD_METHOD              get
         240  LOAD_FAST                'hdr'
         242  CALL_METHOD_1         1  ''
         244  CALL_FUNCTION_3       3  ''
         246  POP_TOP          
         248  JUMP_BACK           220  'to 220'
         250  POP_BLOCK        
       252_0  COME_FROM_LOOP      212  '212'
       252_1  COME_FROM           210  '210'

 327     252  LOAD_FAST                'self'
         254  LOAD_ATTR                headers
         256  LOAD_METHOD              get
         258  LOAD_STR                 'transfer-encoding'
         260  CALL_METHOD_1         1  ''
         262  STORE_FAST               'tr_enc'

 328     264  LOAD_FAST                'tr_enc'
         266  POP_JUMP_IF_FALSE   298  'to 298'
         270  LOAD_FAST                'tr_enc'
         272  LOAD_METHOD              lower
         274  CALL_METHOD_0         0  ''
         276  LOAD_STR                 'chunked'
         278  COMPARE_OP               ==
         280  POP_JUMP_IF_FALSE   298  'to 298'

 329     284  LOAD_CONST               True
         286  LOAD_FAST                'self'
         288  STORE_ATTR               chunked

 330     290  LOAD_CONST               None
         292  LOAD_FAST                'self'
         294  STORE_ATTR               chunk_left
         296  JUMP_FORWARD        304  'to 304'
       298_0  COME_FROM           266  '266'

 332     298  LOAD_CONST               False
         300  LOAD_FAST                'self'
         302  STORE_ATTR               chunked
       304_0  COME_FROM           296  '296'

 335     304  LOAD_FAST                'self'
         306  LOAD_METHOD              _check_close
         308  CALL_METHOD_0         0  ''
         310  LOAD_FAST                'self'
         312  STORE_ATTR               will_close

 339     314  LOAD_CONST               None
         316  LOAD_FAST                'self'
         318  STORE_ATTR               length

 340     320  LOAD_FAST                'self'
         322  LOAD_ATTR                headers
         324  LOAD_METHOD              get
         326  LOAD_STR                 'content-length'
         328  CALL_METHOD_1         1  ''
         330  STORE_FAST               'length'

 343     332  LOAD_FAST                'self'
         334  LOAD_ATTR                headers
         336  LOAD_METHOD              get
         338  LOAD_STR                 'transfer-encoding'
         340  CALL_METHOD_1         1  ''
         342  STORE_FAST               'tr_enc'

 344     344  LOAD_FAST                'length'
         346  POP_JUMP_IF_FALSE   422  'to 422'
         350  LOAD_FAST                'self'
         352  LOAD_ATTR                chunked
         354  POP_JUMP_IF_TRUE    422  'to 422'

 345     358  SETUP_EXCEPT        374  'to 374'

 346     360  LOAD_GLOBAL              int
         362  LOAD_FAST                'length'
         364  CALL_FUNCTION_1       1  ''
         366  LOAD_FAST                'self'
         368  STORE_ATTR               length
         370  POP_BLOCK        
         372  JUMP_FORWARD        402  'to 402'
       374_0  COME_FROM_EXCEPT    358  '358'

 347     374  DUP_TOP          
         376  LOAD_GLOBAL              ValueError
         378  COMPARE_OP               exception-match
         380  POP_JUMP_IF_FALSE   400  'to 400'
         384  POP_TOP          
         386  POP_TOP          
         388  POP_TOP          

 348     390  LOAD_CONST               None
         392  LOAD_FAST                'self'
         394  STORE_ATTR               length
         396  POP_EXCEPT       
         398  JUMP_FORWARD        420  'to 420'
         400  END_FINALLY      
       402_0  COME_FROM           372  '372'

 350     402  LOAD_FAST                'self'
         404  LOAD_ATTR                length
         406  LOAD_CONST               0
         408  COMPARE_OP               <
         410  POP_JUMP_IF_FALSE   428  'to 428'

 351     414  LOAD_CONST               None
         416  LOAD_FAST                'self'
         418  STORE_ATTR               length
       420_0  COME_FROM           398  '398'
         420  JUMP_FORWARD        428  'to 428'
       422_0  COME_FROM           354  '354'

 353     422  LOAD_CONST               None
         424  LOAD_FAST                'self'
         426  STORE_ATTR               length
       428_0  COME_FROM           420  '420'
       428_1  COME_FROM           410  '410'

 356     428  LOAD_FAST                'status'
         430  LOAD_GLOBAL              NO_CONTENT
         432  COMPARE_OP               ==
         434  POP_JUMP_IF_TRUE    486  'to 486'
         438  LOAD_FAST                'status'
         440  LOAD_GLOBAL              NOT_MODIFIED
         442  COMPARE_OP               ==
         444  POP_JUMP_IF_TRUE    486  'to 486'

 357     448  LOAD_CONST               100
         450  LOAD_FAST                'status'
         452  DUP_TOP          
         454  ROT_THREE        
         456  COMPARE_OP               <=
         458  POP_JUMP_IF_FALSE   472  'to 472'
         462  LOAD_CONST               200
         464  COMPARE_OP               <
         466  POP_JUMP_IF_TRUE    486  'to 486'
         470  JUMP_FORWARD        474  'to 474'
         472  ELSE                     '474'
         472  POP_TOP          
       474_0  COME_FROM           470  '470'

 358     474  LOAD_FAST                'self'
         476  LOAD_ATTR                _method
         478  LOAD_STR                 'HEAD'
         480  COMPARE_OP               ==
       482_0  COME_FROM           466  '466'
       482_1  COME_FROM           444  '444'
       482_2  COME_FROM           434  '434'
         482  POP_JUMP_IF_FALSE   492  'to 492'

 359     486  LOAD_CONST               0
         488  LOAD_FAST                'self'
         490  STORE_ATTR               length
       492_0  COME_FROM           482  '482'

 364     492  LOAD_FAST                'self'
         494  LOAD_ATTR                will_close
         496  POP_JUMP_IF_TRUE    526  'to 526'

 365     500  LOAD_FAST                'self'
         502  LOAD_ATTR                chunked
         504  POP_JUMP_IF_TRUE    526  'to 526'

 366     508  LOAD_FAST                'self'
         510  LOAD_ATTR                length
         512  LOAD_CONST               None
         514  COMPARE_OP               is
         516  POP_JUMP_IF_FALSE   526  'to 526'

 367     520  LOAD_CONST               True
         522  LOAD_FAST                'self'
         524  STORE_ATTR               will_close
       526_0  COME_FROM           516  '516'
       526_1  COME_FROM           504  '504'
       526_2  COME_FROM           496  '496'

Parse error at or near `COME_FROM' instruction at offset 482_0

    def _check_close(self):
        conn = self.headers.get('connection')
        if self.version == 11:
            pass
        if conn:
            if 'close' in conn.lower():
                return True
            return False
        elif self.headers.get('keep-alive'):
            return False
        else:
            if conn:
                if 'keep-alive' in conn.lower():
                    return False
                pconn = self.headers.get('proxy-connection')
                if pconn:
                    pass
            if 'keep-alive' in pconn.lower():
                return False
            return True

    def _close_conn(self):
        fp = self.fp
        self.fp = None
        fp.close()

    def close(self):
        try:
            super().close()
        finally:
            if self.fp:
                self._close_conn()

    def flush(self):
        super().flush()
        if self.fp:
            self.fp.flush()

    def readable(self):
        """Always returns True"""
        return True

    def isclosed(self):
        """True if the connection is closed."""
        return self.fp is None

    def read(self, amt=None):
        if self.fp is None:
            return ''
        elif self._method == 'HEAD':
            self._close_conn()
            return ''
        elif amt is not None:
            b = bytearray(amt)
            n = self.readinto(b)
            return memoryview(b)[:n].tobytes()
        elif self.chunked:
            return self._readall_chunked()
        else:
            if self.length is None:
                s = self.fp.read()
            else:
                try:
                    s = self._safe_read(self.length)
                except IncompleteRead:
                    self._close_conn()
                    raise

                self.length = 0
            self._close_conn()
            return s

    def readinto(self, b):
        """Read up to len(b) bytes into bytearray b and return the number
        of bytes read.
        """
        if self.fp is None:
            return 0
        elif self._method == 'HEAD':
            self._close_conn()
            return 0
        elif self.chunked:
            return self._readinto_chunked(b)
        else:
            if self.length is not None:
                if len(b) > self.length:
                    b = memoryview(b)[0:self.length]
                n = self.fp.readinto(b)
                if not n:
                    if b:
                        self._close_conn()
            elif self.length is not None:
                self.length -= n
            else:
                if not self.length:
                    self._close_conn()

            return n

    def _read_next_chunk_size(self):
        line = self.fp.readline(_MAXLINE + 1)
        if len(line) > _MAXLINE:
            raise LineTooLong('chunk size')
        i = line.find(';')
        if i >= 0:
            line = line[:i]
        try:
            return int(line, 16)
        except ValueError:
            self._close_conn()
            raise

    def _read_and_discard_trailer(self):
        while 1:
            line = self.fp.readline(_MAXLINE + 1)
            if len(line) > _MAXLINE:
                raise LineTooLong('trailer line')
            if not line:
                break
            if line in ('\r\n', '\n', ''):
                break

    def _get_chunk_left(self):
        chunk_left = self.chunk_left
        if not chunk_left:
            if chunk_left is not None:
                self._safe_read(2)
            try:
                chunk_left = self._read_next_chunk_size()
            except ValueError:
                raise IncompleteRead('')

            if chunk_left == 0:
                self._read_and_discard_trailer()
                self._close_conn()
                chunk_left = None
            self.chunk_left = chunk_left
        return chunk_left

    def _readall_chunked(self):
        if not self.chunked != _UNKNOWN:
            raise AssertionError
        value = []
        try:
            while True:
                chunk_left = self._get_chunk_left()
                if chunk_left is None:
                    break
                value.append(self._safe_read(chunk_left))
                self.chunk_left = 0

            return ''.join(value)
        except IncompleteRead:
            raise IncompleteRead(''.join(value))

    def _readinto_chunked(self, b):
        if not self.chunked != _UNKNOWN:
            raise AssertionError
        total_bytes = 0
        mvb = memoryview(b)
        try:
            while True:
                chunk_left = self._get_chunk_left()
                if chunk_left is None:
                    return total_bytes
                if len(mvb) <= chunk_left:
                    n = self._safe_readinto(mvb)
                    self.chunk_left = chunk_left - n
                    return total_bytes + n
                temp_mvb = mvb[:chunk_left]
                n = self._safe_readinto(temp_mvb)
                mvb = mvb[n:]
                total_bytes += n
                self.chunk_left = 0

        except IncompleteRead:
            raise IncompleteRead(bytes(b[0:total_bytes]))

    def _safe_read(self, amt):
        """Read the number of bytes requested, compensating for partial reads.

        Normally, we have a blocking socket, but a read() can be interrupted
        by a signal (resulting in a partial read).

        Note that we cannot distinguish between EOF and an interrupt when zero
        bytes have been read. IncompleteRead() will be raised in this
        situation.

        This function should be used when <amt> bytes "should" be present for
        reading. If the bytes are truly not available (due to EOF), then the
        IncompleteRead exception can be used to detect the problem.
        """
        s = []
        while 1:
            if amt > 0:
                chunk = self.fp.read(min(amt, MAXAMOUNT))
                if not chunk:
                    raise IncompleteRead(''.join(s), amt)
                s.append(chunk)
                amt -= len(chunk)

        return ''.join(s)

    def _safe_readinto(self, b):
        """Same as _safe_read, but for reading into a buffer."""
        total_bytes = 0
        mvb = memoryview(b)
        while 1:
            if total_bytes < len(b):
                if MAXAMOUNT < len(mvb):
                    temp_mvb = mvb[0:MAXAMOUNT]
                    n = self.fp.readinto(temp_mvb)
                else:
                    n = self.fp.readinto(mvb)
                if not n:
                    raise IncompleteRead(bytes(mvb[0:total_bytes]), len(b))
                mvb = mvb[n:]
                total_bytes += n

        return total_bytes

    def read1(self, n=-1):
        """Read with at most one underlying system call.  If at least one
        byte is buffered, return that instead.
        """
        if self.fp is None or self._method == 'HEAD':
            return ''
        elif self.chunked:
            return self._read1_chunked(n)
        else:
            if self.length is not None:
                if n < 0 or n > self.length:
                    n = self.length
                result = self.fp.read1(n)
                if not result:
                    if n:
                        self._close_conn()
            elif self.length is not None:
                self.length -= len(result)
            return result

    def peek(self, n=-1):
        if self.fp is None or self._method == 'HEAD':
            return ''
        elif self.chunked:
            return self._peek_chunked(n)
        else:
            return self.fp.peek(n)

    def readline(self, limit=-1):
        if self.fp is None or self._method == 'HEAD':
            return ''
        elif self.chunked:
            return super().readline(limit)
        else:
            if self.length is not None:
                if limit < 0 or limit > self.length:
                    limit = self.length
                result = self.fp.readline(limit)
                if not result:
                    if limit:
                        self._close_conn()
            elif self.length is not None:
                self.length -= len(result)
            return result

    def _read1_chunked(self, n):
        chunk_left = self._get_chunk_left()
        if chunk_left is None or n == 0:
            return ''
        else:
            if not 0 <= n <= chunk_left:
                n = chunk_left
            read = self.fp.read1(n)
            self.chunk_left -= len(read)
            if not read:
                raise IncompleteRead('')
            return read

    def _peek_chunked(self, n):
        try:
            chunk_left = self._get_chunk_left()
        except IncompleteRead:
            return ''
        else:
            if chunk_left is None:
                return ''
            else:
                return self.fp.peek(chunk_left)[:chunk_left]

    def fileno(self):
        return self.fp.fileno()

    def getheader(self, name, default=None):
        """Returns the value of the header matching *name*.

        If there are multiple matching headers, the values are
        combined into a single string separated by commas and spaces.

        If no matching header is found, returns *default* or None if
        the *default* is not specified.

        If the headers are unknown, raises http.client.ResponseNotReady.

        """
        if self.headers is None:
            raise ResponseNotReady()
        headers = self.headers.get_all(name) or default
        if not (isinstance(headers, str) or hasattr(headers, '__iter__')):
            return headers
        else:
            return ', '.join(headers)

    def getheaders(self):
        """Return list of (header, value) tuples."""
        if self.headers is None:
            raise ResponseNotReady()
        return list(self.headers.items())

    def __iter__(self):
        return self

    def info(self):
        """Returns an instance of the class mimetools.Message containing
        meta-information associated with the URL.

        When the method is HTTP, these headers are those returned by
        the server at the head of the retrieved HTML page (including
        Content-Length and Content-Type).

        When the method is FTP, a Content-Length header will be
        present if (as is now usual) the server passed back a file
        length in response to the FTP retrieval request. A
        Content-Type header will be present if the MIME type can be
        guessed.

        When the method is local-file, returned headers will include
        a Date representing the file's last-modified time, a
        Content-Length giving file size, and a Content-Type
        containing a guess at the file's type. See also the
        description of the mimetools module.

        """
        return self.headers

    def geturl(self):
        """Return the real URL of the page.

        In some cases, the HTTP server redirects a client to another
        URL. The urlopen() function handles this transparently, but in
        some cases the caller needs to know which URL the client was
        redirected to. The geturl() method can be used to get at this
        redirected URL.

        """
        return self.url

    def getcode(self):
        """Return the HTTP status code that was sent with the response,
        or None if the URL is not an HTTP URL.

        """
        return self.status


class HTTPConnection:
    _http_vsn = 11
    _http_vsn_str = 'HTTP/1.1'
    response_class = HTTPResponse
    default_port = HTTP_PORT
    auto_open = 1
    debuglevel = 0

    @staticmethod
    def _is_textIO(stream):
        """Test whether a file-like object is a text or a binary stream.
        """
        return isinstance(stream, io.TextIOBase)

    @staticmethod
    def _get_content_length(body, method):
        """Get the content-length based on the body.

        If the body is None, we set Content-Length: 0 for methods that expect
        a body (RFC 7230, Section 3.3.2). We also set the Content-Length for
        any method if the body is a str or bytes-like object and not a file.
        """
        if body is None:
            if method.upper() in _METHODS_EXPECTING_BODY:
                return 0
            return
        if hasattr(body, 'read'):
            return
        try:
            mv = memoryview(body)
            return mv.nbytes
        except TypeError:
            pass

        if isinstance(body, str):
            return len(body)

    def __init__(self, host, port=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, source_address=None, blocksize=8192):
        self.timeout = timeout
        self.source_address = source_address
        self.blocksize = blocksize
        self.sock = None
        self._buffer = []
        self._HTTPConnection__response = None
        self._HTTPConnection__state = _CS_IDLE
        self._method = None
        self._tunnel_host = None
        self._tunnel_port = None
        self._tunnel_headers = {}
        self.host, self.port = self._get_hostport(host, port)
        self._create_connection = socket.create_connection

    def set_tunnel(self, host, port=None, headers=None):
        """Set up host and port for HTTP CONNECT tunnelling.

        In a connection that uses HTTP CONNECT tunneling, the host passed to the
        constructor is used as a proxy server that relays all communication to
        the endpoint passed to `set_tunnel`. This done by sending an HTTP
        CONNECT request to the proxy server when the connection is established.

        This method must be called before the HTML connection has been
        established.

        The headers argument should be a mapping of extra HTTP headers to send
        with the CONNECT request.
        """
        if self.sock:
            raise RuntimeError("Can't set up tunnel for established connection")
        self._tunnel_host, self._tunnel_port = self._get_hostport(host, port)
        if headers:
            self._tunnel_headers = headers
        else:
            self._tunnel_headers.clear()

    def _get_hostport(self, host, port):
        if port is None:
            i = host.rfind(':')
            j = host.rfind(']')
            if i > j:
                try:
                    port = int(host[i + 1:])
                except ValueError:
                    if host[i + 1:] == '':
                        port = self.default_port
                    else:
                        raise InvalidURL("nonnumeric port: '%s'" % host[i + 1:])

                host = host[:i]
            else:
                port = self.default_port
            if host:
                pass
            if host[0] == '[':
                if host[(-1)] == ']':
                    host = host[1:-1]
                return (
                 host, port)

    def set_debuglevel(self, level):
        self.debuglevel = level

    def _tunnel(self):
        connect_str = 'CONNECT %s:%d HTTP/1.0\r\n' % (self._tunnel_host,
         self._tunnel_port)
        connect_bytes = connect_str.encode('ascii')
        self.send(connect_bytes)
        for header, value in self._tunnel_headers.items():
            header_str = '%s: %s\r\n' % (header, value)
            header_bytes = header_str.encode('latin-1')
            self.send(header_bytes)

        self.send('\r\n')
        response = self.response_class((self.sock), method=(self._method))
        version, code, message = response._read_status()
        if code != http.HTTPStatus.OK:
            self.close()
            raise OSError('Tunnel connection failed: %d %s' % (code,
             message.strip()))
        while 1:
            line = response.fp.readline(_MAXLINE + 1)
            if len(line) > _MAXLINE:
                raise LineTooLong('header line')
            if not line:
                break
            if line in ('\r\n', '\n', ''):
                break
            if self.debuglevel > 0:
                print('header:', line.decode())

    def connect(self):
        """Connect to the host and port specified in __init__."""
        self.sock = self._create_connection((
         self.host, self.port), self.timeout, self.source_address)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        if self._tunnel_host:
            self._tunnel()

    def close(self):
        """Close the connection to the HTTP server."""
        self._HTTPConnection__state = _CS_IDLE
        try:
            sock = self.sock
            if sock:
                self.sock = None
                sock.close()
        finally:
            response = self._HTTPConnection__response
            if response:
                self._HTTPConnection__response = None
                response.close()

    def send(self, data):
        """Send `data' to the server.
        ``data`` can be a string object, a bytes object, an array object, a
        file-like object that supports a .read() method, or an iterable object.
        """
        if self.sock is None:
            if self.auto_open:
                self.connect()
            else:
                raise NotConnected()
        if self.debuglevel > 0:
            print('send:', repr(data))
        if hasattr(data, 'read'):
            if self.debuglevel > 0:
                print('sendIng a read()able')
            encode = self._is_textIO(data)
        if encode:
            if self.debuglevel > 0:
                print('encoding file using iso-8859-1')
            while True:
                datablock = data.read(self.blocksize)
                if not datablock:
                    break
                if encode:
                    datablock = datablock.encode('iso-8859-1')
                self.sock.sendall(datablock)

            return
        try:
            self.sock.sendall(data)
        except TypeError:
            if isinstance(data, collections.abc.Iterable):
                for d in data:
                    self.sock.sendall(d)

            else:
                raise TypeError('data should be a bytes-like object or an iterable, got %r' % type(data))

    def _output(self, s):
        r"""Add a line of output to the current request buffer.

        Assumes that the line does *not* end with \r\n.
        """
        self._buffer.append(s)

    def _read_readable(self, readable):
        if self.debuglevel > 0:
            print('sendIng a read()able')
        encode = self._is_textIO(readable)
        if encode:
            if self.debuglevel > 0:
                print('encoding file using iso-8859-1')
            while True:
                datablock = readable.read(self.blocksize)
                if not datablock:
                    break
                if encode:
                    datablock = datablock.encode('iso-8859-1')
                yield datablock

    def _send_output(self, message_body=None, encode_chunked=False):
        r"""Send the currently buffered request and clear the buffer.

        Appends an extra \r\n to the buffer.
        A message_body may be specified, to be appended to the request.
        """
        self._buffer.extend(('', ''))
        msg = '\r\n'.join(self._buffer)
        del self._buffer[:]
        self.send(msg)
        if message_body is not None:
            if hasattr(message_body, 'read'):
                chunks = self._read_readable(message_body)
            else:
                try:
                    memoryview(message_body)
                except TypeError:
                    try:
                        chunks = iter(message_body)
                    except TypeError:
                        raise TypeError('message_body should be a bytes-like object or an iterable, got %r' % type(message_body))

                else:
                    chunks = (
                     message_body,)
                for chunk in chunks:
                    if not chunk:
                        if self.debuglevel > 0:
                            print('Zero length chunk ignored')
                    elif encode_chunked:
                        if self._http_vsn == 11:
                            chunk = f"{len(chunk):X}\r\n".encode('ascii') + chunk + '\r\n'
                        self.send(chunk)

                if encode_chunked:
                    pass
        if self._http_vsn == 11:
            self.send('0\r\n\r\n')

    def putrequest(self, method, url, skip_host=False, skip_accept_encoding=False):
        """Send a request to the server.

        `method' specifies an HTTP request method, e.g. 'GET'.
        `url' specifies the object being requested, e.g. '/index.html'.
        `skip_host' if True does not add automatically a 'Host:' header
        `skip_accept_encoding' if True does not add automatically an
           'Accept-Encoding:' header
        """
        if self._HTTPConnection__response:
            if self._HTTPConnection__response.isclosed():
                self._HTTPConnection__response = None
            if self._HTTPConnection__state == _CS_IDLE:
                self._HTTPConnection__state = _CS_REQ_STARTED
            else:
                raise CannotSendRequest(self._HTTPConnection__state)
            self._method = method
            if not url:
                url = '/'
            request = '%s %s %s' % (method, url, self._http_vsn_str)
            self._output(request.encode('ascii'))
            if self._http_vsn == 11:
                pass
        if not skip_host:
            netloc = ''
            if url.startswith('http'):
                nil, netloc, nil, nil, nil = urlsplit(url)
            if netloc:
                try:
                    netloc_enc = netloc.encode('ascii')
                except UnicodeEncodeError:
                    netloc_enc = netloc.encode('idna')

                self.putheader('Host', netloc_enc)
            else:
                if self._tunnel_host:
                    host = self._tunnel_host
                    port = self._tunnel_port
                else:
                    host = self.host
                    port = self.port
                try:
                    host_enc = host.encode('ascii')
                except UnicodeEncodeError:
                    host_enc = host.encode('idna')

                if host.find(':') >= 0:
                    host_enc = '[' + host_enc + ']'
                if port == self.default_port:
                    self.putheader('Host', host_enc)
                else:
                    host_enc = host_enc.decode('ascii')
                    self.putheader('Host', '%s:%s' % (host_enc, port))
        if not skip_accept_encoding:
            self.putheader('Accept-Encoding', 'identity')

    def putheader(self, header, *values):
        """Send a request header line to the server.

        For example: h.putheader('Accept', 'text/html')
        """
        if self._HTTPConnection__state != _CS_REQ_STARTED:
            raise CannotSendHeader()
        if hasattr(header, 'encode'):
            header = header.encode('ascii')
        if not _is_legal_header_name(header):
            raise ValueError('Invalid header name %r' % (header,))
        values = list(values)
        for i, one_value in enumerate(values):
            if hasattr(one_value, 'encode'):
                values[i] = one_value.encode('latin-1')
            elif isinstance(one_value, int):
                values[i] = str(one_value).encode('ascii')
            if _is_illegal_header_value(values[i]):
                raise ValueError('Invalid header value %r' % (values[i],))

        value = '\r\n\t'.join(values)
        header = header + ': ' + value
        self._output(header)

    def endheaders(self, message_body=None, *, encode_chunked=False):
        """Indicate that the last header line has been sent to the server.

        This method sends the request to the server.  The optional message_body
        argument can be used to pass a message body associated with the
        request.
        """
        if self._HTTPConnection__state == _CS_REQ_STARTED:
            self._HTTPConnection__state = _CS_REQ_SENT
        else:
            raise CannotSendHeader()
        self._send_output(message_body, encode_chunked=encode_chunked)

    def request(self, method, url, body=None, headers={}, *, encode_chunked=False):
        """Send a complete request to the server."""
        self._send_request(method, url, body, headers, encode_chunked)

    def _send_request(self, method, url, body, headers, encode_chunked):
        header_names = frozenset(k.lower() for k in headers)
        skips = {}
        if 'host' in header_names:
            skips['skip_host'] = 1
        if 'accept-encoding' in header_names:
            skips['skip_accept_encoding'] = 1
        (self.putrequest)(method, url, **skips)
        if 'content-length' not in header_names:
            if 'transfer-encoding' not in header_names:
                encode_chunked = False
                content_length = self._get_content_length(body, method)
                if content_length is None:
                    if body is not None:
                        if self.debuglevel > 0:
                            print('Unable to determine size of %r' % body)
                        encode_chunked = True
                        self.putheader('Transfer-Encoding', 'chunked')
                    else:
                        self.putheader('Content-Length', str(content_length))
            else:
                encode_chunked = False
            for hdr, value in headers.items():
                self.putheader(hdr, value)

            if isinstance(body, str):
                body = _encode(body, 'body')
            self.endheaders(body, encode_chunked=encode_chunked)

    def getresponse(self):
        """Get the response from the server.

        If the HTTPConnection is in the correct state, returns an
        instance of HTTPResponse or of whatever object is returned by
        the response_class variable.

        If a request has not been sent or if a previous response has
        not be handled, ResponseNotReady is raised.  If the HTTP
        response indicates that the connection should be closed, then
        it will be closed before the response is returned.  When the
        connection is closed, the underlying socket is closed.
        """
        if self._HTTPConnection__response:
            if self._HTTPConnection__response.isclosed():
                self._HTTPConnection__response = None
            if self._HTTPConnection__state != _CS_REQ_SENT or self._HTTPConnection__response:
                raise ResponseNotReady(self._HTTPConnection__state)
            if self.debuglevel > 0:
                response = self.response_class((self.sock), (self.debuglevel), method=(self._method))
            else:
                response = self.response_class((self.sock), method=(self._method))
        try:
            try:
                response.begin()
            except ConnectionError:
                self.close()
                raise

            if not response.will_close != _UNKNOWN:
                raise AssertionError
            self._HTTPConnection__state = _CS_IDLE
            if response.will_close:
                self.close()
            else:
                self._HTTPConnection__response = response
            return response
        except:
            response.close()
            raise


try:
    import ssl
except ImportError:
    pass
else:

    class HTTPSConnection(HTTPConnection):
        """'This class allows communication via SSL.'"""
        default_port = HTTPS_PORT

        def __init__(self, host, port=None, key_file=None, cert_file=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, source_address=None, *, context=None, check_hostname=None, blocksize=8192):
            super(HTTPSConnection, self).__init__(host, port, timeout, source_address,
              blocksize=blocksize)
            if key_file is not None or cert_file is not None or check_hostname is not None:
                import warnings
                warnings.warn('key_file, cert_file and check_hostname are deprecated, use a custom context instead.', DeprecationWarning, 2)
            self.key_file = key_file
            self.cert_file = cert_file
            if context is None:
                context = ssl._create_default_https_context()
            will_verify = context.verify_mode != ssl.CERT_NONE
            if check_hostname is None:
                check_hostname = context.check_hostname
            if check_hostname:
                if not will_verify:
                    raise ValueError('check_hostname needs a SSL context with either CERT_OPTIONAL or CERT_REQUIRED')
                if key_file or cert_file:
                    context.load_cert_chain(cert_file, key_file)
                self._context = context
                if check_hostname is not None:
                    self._context.check_hostname = check_hostname

        def connect(self):
            """Connect to a host on a given (SSL) port."""
            super().connect()
            if self._tunnel_host:
                server_hostname = self._tunnel_host
            else:
                server_hostname = self.host
            self.sock = self._context.wrap_socket((self.sock), server_hostname=server_hostname)


    __all__.append('HTTPSConnection')

class HTTPException(Exception):
    pass


class NotConnected(HTTPException):
    pass


class InvalidURL(HTTPException):
    pass


class UnknownProtocol(HTTPException):

    def __init__(self, version):
        self.args = (
         version,)
        self.version = version


class UnknownTransferEncoding(HTTPException):
    pass


class UnimplementedFileMode(HTTPException):
    pass


class IncompleteRead(HTTPException):

    def __init__(self, partial, expected=None):
        self.args = (
         partial,)
        self.partial = partial
        self.expected = expected

    def __repr__(self):
        if self.expected is not None:
            e = ', %i more expected' % self.expected
        else:
            e = ''
        return '%s(%i bytes read%s)' % (self.__class__.__name__,
         len(self.partial), e)

    def __str__(self):
        return repr(self)


class ImproperConnectionState(HTTPException):
    pass


class CannotSendRequest(ImproperConnectionState):
    pass


class CannotSendHeader(ImproperConnectionState):
    pass


class ResponseNotReady(ImproperConnectionState):
    pass


class BadStatusLine(HTTPException):

    def __init__(self, line):
        if not line:
            line = repr(line)
        self.args = (
         line,)
        self.line = line


class LineTooLong(HTTPException):

    def __init__(self, line_type):
        HTTPException.__init__(self, 'got more than %d bytes when reading %s' % (
         _MAXLINE, line_type))


class RemoteDisconnected(ConnectionResetError, BadStatusLine):

    def __init__(self, *pos, **kw):
        BadStatusLine.__init__(self, '')
        (ConnectionResetError.__init__)(self, *pos, **kw)


error = HTTPException