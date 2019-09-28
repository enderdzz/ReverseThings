# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: subprocess.py
"""Subprocesses with accessible I/O streams

This module allows you to spawn processes, connect to their
input/output/error pipes, and obtain their return codes.

For a complete description of this module see the Python documentation.

Main API
========
run(...): Runs a command, waits for it to complete, then returns a
          CompletedProcess instance.
Popen(...): A class for flexibly executing a command in a new process

Constants
---------
DEVNULL: Special value that indicates that os.devnull should be used
PIPE:    Special value that indicates a pipe should be created
STDOUT:  Special value that indicates that stderr should go to stdout

Older API
=========
call(...): Runs a command, waits for it to complete, then returns
    the return code.
check_call(...): Same as call() but raises CalledProcessError()
    if return code is not 0
check_output(...): Same as check_call() but returns the contents of
    stdout instead of a return code
getoutput(...): Runs a command in the shell, waits for it to complete,
    then returns the output
getstatusoutput(...): Runs a command in the shell, waits for it to complete,
    then returns a (exitcode, output) tuple
"""
import sys
_mswindows = sys.platform == 'win32'
import io, os, time, signal, builtins, warnings, errno
from time import monotonic as _time

class SubprocessError(Exception):
    pass


class CalledProcessError(SubprocessError):
    r"""'Raised when run() is called with check=True and the process\n    returns a non-zero exit status.\n\n    Attributes:\n      cmd, returncode, stdout, stderr, output\n    '"""

    def __init__(self, returncode, cmd, output=None, stderr=None):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.stderr = stderr

    def __str__(self):
        if self.returncode:
            if self.returncode < 0:
                try:
                    return "Command '%s' died with %r." % (
                     self.cmd, signal.Signals(-self.returncode))
                except ValueError:
                    return "Command '%s' died with unknown signal %d." % (
                     self.cmd, -self.returncode)

        else:
            return "Command '%s' returned non-zero exit status %d." % (
             self.cmd, self.returncode)

    @property
    def stdout(self):
        """Alias for output attribute, to match stderr"""
        return self.output

    @stdout.setter
    def stdout(self, value):
        self.output = value


class TimeoutExpired(SubprocessError):
    r"""'This exception is raised when the timeout expires while waiting for a\n    child process.\n\n    Attributes:\n        cmd, output, stdout, stderr, timeout\n    '"""

    def __init__(self, cmd, timeout, output=None, stderr=None):
        self.cmd = cmd
        self.timeout = timeout
        self.output = output
        self.stderr = stderr

    def __str__(self):
        return "Command '%s' timed out after %s seconds" % (
         self.cmd, self.timeout)

    @property
    def stdout(self):
        return self.output

    @stdout.setter
    def stdout(self, value):
        self.output = value


if _mswindows:
    import threading, msvcrt, _winapi

    class STARTUPINFO:

        def __init__(self, *, dwFlags=0, hStdInput=None, hStdOutput=None, hStdError=None, wShowWindow=0, lpAttributeList=None):
            self.dwFlags = dwFlags
            self.hStdInput = hStdInput
            self.hStdOutput = hStdOutput
            self.hStdError = hStdError
            self.wShowWindow = wShowWindow
            self.lpAttributeList = lpAttributeList or {'handle_list': []}

        def _copy(self):
            attr_list = self.lpAttributeList.copy()
            if 'handle_list' in attr_list:
                attr_list['handle_list'] = list(attr_list['handle_list'])
            return STARTUPINFO(dwFlags=(self.dwFlags), hStdInput=(self.hStdInput),
              hStdOutput=(self.hStdOutput),
              hStdError=(self.hStdError),
              wShowWindow=(self.wShowWindow),
              lpAttributeList=attr_list)


else:
    import _posixsubprocess, select, selectors, threading
    _PIPE_BUF = getattr(select, 'PIPE_BUF', 512)
    if hasattr(selectors, 'PollSelector'):
        _PopenSelector = selectors.PollSelector
    else:
        _PopenSelector = selectors.SelectSelector
__all__ = ['Popen', 'PIPE', 'STDOUT', 'call', 'check_call', 'getstatusoutput',
 'getoutput', 'check_output', 'run', 'CalledProcessError', 'DEVNULL',
 'SubprocessError', 'TimeoutExpired', 'CompletedProcess']
if _mswindows:
    from _winapi import CREATE_NEW_CONSOLE, CREATE_NEW_PROCESS_GROUP, STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, STD_ERROR_HANDLE, SW_HIDE, STARTF_USESTDHANDLES, STARTF_USESHOWWINDOW, ABOVE_NORMAL_PRIORITY_CLASS, BELOW_NORMAL_PRIORITY_CLASS, HIGH_PRIORITY_CLASS, IDLE_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, REALTIME_PRIORITY_CLASS, CREATE_NO_WINDOW, DETACHED_PROCESS, CREATE_DEFAULT_ERROR_MODE, CREATE_BREAKAWAY_FROM_JOB
    __all__.extend(['CREATE_NEW_CONSOLE', 'CREATE_NEW_PROCESS_GROUP',
     'STD_INPUT_HANDLE', 'STD_OUTPUT_HANDLE',
     'STD_ERROR_HANDLE', 'SW_HIDE',
     'STARTF_USESTDHANDLES', 'STARTF_USESHOWWINDOW',
     'STARTUPINFO',
     'ABOVE_NORMAL_PRIORITY_CLASS', 'BELOW_NORMAL_PRIORITY_CLASS',
     'HIGH_PRIORITY_CLASS', 'IDLE_PRIORITY_CLASS',
     'NORMAL_PRIORITY_CLASS', 'REALTIME_PRIORITY_CLASS',
     'CREATE_NO_WINDOW', 'DETACHED_PROCESS',
     'CREATE_DEFAULT_ERROR_MODE', 'CREATE_BREAKAWAY_FROM_JOB'])

    class Handle(int):
        closed = False

        def Close(self, CloseHandle=_winapi.CloseHandle):
            if not self.closed:
                self.closed = True
                CloseHandle(self)

        def Detach(self):
            if not self.closed:
                self.closed = True
                return int(self)
            raise ValueError('already closed')

        def __repr__(self):
            return '%s(%d)' % (self.__class__.__name__, int(self))

        __del__ = Close
        __str__ = __repr__


_active = []

def _cleanup():
    for inst in _active[:]:
        res = inst._internal_poll(_deadstate=(sys.maxsize))
        if res is not None:
            try:
                _active.remove(inst)
            except ValueError:
                pass


PIPE = -1
STDOUT = -2
DEVNULL = -3

def _optim_args_from_interpreter_flags():
    """Return a list of command-line arguments reproducing the current
    optimization settings in sys.flags."""
    args = []
    value = sys.flags.optimize
    if value > 0:
        args.append('-' + 'O' * value)
    return args


def _args_from_interpreter_flags():
    """Return a list of command-line arguments reproducing the current
    settings in sys.flags, sys.warnoptions and sys._xoptions."""
    flag_opt_map = {'debug':'d', 
     'dont_write_bytecode':'B', 
     'no_site':'S', 
     'verbose':'v', 
     'bytes_warning':'b', 
     'quiet':'q'}
    args = _optim_args_from_interpreter_flags()
    for flag, opt in flag_opt_map.items():
        v = getattr(sys.flags, flag)
        if v > 0:
            args.append('-' + opt * v)

    if sys.flags.isolated:
        args.append('-I')
    elif sys.flags.ignore_environment:
        args.append('-E')
    else:
        if sys.flags.no_user_site:
            args.append('-s')
        warnopts = sys.warnoptions[:]
        bytes_warning = sys.flags.bytes_warning
        xoptions = getattr(sys, '_xoptions', {})
        dev_mode = 'dev' in xoptions

    if bytes_warning > 1:
        warnopts.remove('error::BytesWarning')
    elif bytes_warning:
        warnopts.remove('default::BytesWarning')
    else:
        if dev_mode:
            warnopts.remove('default')
        for opt in warnopts:
            args.append('-W' + opt)

        if dev_mode:
            args.extend(('-X', 'dev'))
        for opt in ('faulthandler', 'tracemalloc', 'importtime', 'showalloccount',
                    'showrefcount', 'utf8'):
            if opt in xoptions:
                value = xoptions[opt]
                if value is True:
                    arg = opt
                else:
                    arg = '%s=%s' % (opt, value)
                args.extend(('-X', arg))

        return args


def call(*popenargs, timeout=None, **kwargs):
    """Run command with arguments.  Wait for command to complete or
    timeout, then return the returncode attribute.

    The arguments are the same as for the Popen constructor.  Example:

    retcode = call(["ls", "-l"])
    """
    with Popen(*popenargs, **kwargs) as (p):
        try:
            return p.wait(timeout=timeout)
        except:
            p.kill()
            raise


def check_call(*popenargs, **kwargs):
    """Run command with arguments.  Wait for command to complete.  If
    the exit code was zero then return, otherwise raise
    CalledProcessError.  The CalledProcessError object will have the
    return code in the returncode attribute.

    The arguments are the same as for the call function.  Example:

    check_call(["ls", "-l"])
    """
    retcode = call(*popenargs, **kwargs)
    if retcode:
        cmd = kwargs.get('args')
        if cmd is None:
            cmd = popenargs[0]
        raise CalledProcessError(retcode, cmd)
    return 0


def check_output(*popenargs, timeout=None, **kwargs):
    r"""Run command with arguments and return its output.

    If the exit code was non-zero it raises a CalledProcessError.  The
    CalledProcessError object will have the return code in the returncode
    attribute and output in the output attribute.

    The arguments are the same as for the Popen constructor.  Example:

    >>> check_output(["ls", "-l", "/dev/null"])
    b'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'

    The stdout argument is not allowed as it is used internally.
    To capture standard error in the result, use stderr=STDOUT.

    >>> check_output(["/bin/sh", "-c",
    ...               "ls -l non_existent_file ; exit 0"],
    ...              stderr=STDOUT)
    b'ls: non_existent_file: No such file or directory\n'

    There is an additional optional argument, "input", allowing you to
    pass a string to the subprocess's stdin.  If you use this argument
    you may not also use the Popen constructor's "stdin" argument, as
    it too will be used internally.  Example:

    >>> check_output(["sed", "-e", "s/foo/bar/"],
    ...              input=b"when in the course of fooman events\n")
    b'when in the course of barman events\n'

    By default, all communication is in bytes, and therefore any "input"
    should be bytes, and the return value wil be bytes.  If in text mode,
    any "input" should be a string, and the return value will be a string
    decoded according to locale encoding, or by "encoding" if set. Text mode
    is triggered by setting any of text, encoding, errors or universal_newlines.
    """
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    if 'input' in kwargs:
        if kwargs['input'] is None:
            kwargs['input'] = '' if kwargs.get('universal_newlines', False) else ''
        return run(popenargs, stdout=PIPE, timeout=timeout, check=True, **kwargs).stdout


class CompletedProcess(object):
    r"""'A process that has finished running.\n\n    This is returned by run().\n\n    Attributes:\n      args: The list or str args passed to run().\n      returncode: The exit code of the process, negative for signals.\n      stdout: The standard output (None if not captured).\n      stderr: The standard error (None if not captured).\n    '"""

    def __init__(self, args, returncode, stdout=None, stderr=None):
        self.args = args
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def __repr__(self):
        args = [
         'args={!r}'.format(self.args),
         'returncode={!r}'.format(self.returncode)]
        if self.stdout is not None:
            args.append('stdout={!r}'.format(self.stdout))
        if self.stderr is not None:
            args.append('stderr={!r}'.format(self.stderr))
        return '{}({})'.format(type(self).__name__, ', '.join(args))

    def check_returncode(self):
        """Raise CalledProcessError if the exit code is non-zero."""
        if self.returncode:
            raise CalledProcessError(self.returncode, self.args, self.stdout, self.stderr)


def run(*popenargs, input=None, capture_output=False, timeout=None, check=False, **kwargs):
    """Run command with arguments and return a CompletedProcess instance.

    The returned instance will have attributes args, returncode, stdout and
    stderr. By default, stdout and stderr are not captured, and those attributes
    will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them.

    If check is True and the exit code was non-zero, it raises a
    CalledProcessError. The CalledProcessError object will have the return code
    in the returncode attribute, and output & stderr attributes if those streams
    were captured.

    If timeout is given, and the process takes too long, a TimeoutExpired
    exception will be raised.

    There is an optional argument "input", allowing you to
    pass bytes or a string to the subprocess's stdin.  If you use this argument
    you may not also use the Popen constructor's "stdin" argument, as
    it will be used internally.

    By default, all communication is in bytes, and therefore any "input" should
    be bytes, and the stdout and stderr will be bytes. If in text mode, any
    "input" should be a string, and stdout and stderr will be strings decoded
    according to locale encoding, or by "encoding" if set. Text mode is
    triggered by setting any of text, encoding, errors or universal_newlines.

    The other arguments are the same as for the Popen constructor.
    """
    if input is not None:
        if 'stdin' in kwargs:
            raise ValueError('stdin and input arguments may not both be used.')
        kwargs['stdin'] = PIPE
    if capture_output:
        if 'stdout' in kwargs or 'stderr' in kwargs:
            raise ValueError('stdout and stderr arguments may not be used with capture_output.')
        kwargs['stdout'] = PIPE
        kwargs['stderr'] = PIPE
    with Popen(*popenargs, **kwargs) as (process):
        try:
            stdout, stderr = process.communicate(input, timeout=timeout)
        except TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            raise TimeoutExpired((process.args), timeout, output=stdout, stderr=stderr)
        except:
            process.kill()
            raise

        retcode = process.poll()
        if check:
            pass
        if retcode:
            raise CalledProcessError(retcode, (process.args), output=stdout,
              stderr=stderr)
    return CompletedProcess(process.args, retcode, stdout, stderr)


def list2cmdline(seq):
    """
    Translate a sequence of arguments into a command line
    string, using the same rules as the MS C runtime:

    1) Arguments are delimited by white space, which is either a
       space or a tab.

    2) A string surrounded by double quotation marks is
       interpreted as a single argument, regardless of white space
       contained within.  A quoted string can be embedded in an
       argument.

    3) A double quotation mark preceded by a backslash is
       interpreted as a literal double quotation mark.

    4) Backslashes are interpreted literally, unless they
       immediately precede a double quotation mark.

    5) If backslashes immediately precede a double quotation mark,
       every pair of backslashes is interpreted as a literal
       backslash.  If the number of backslashes is odd, the last
       backslash escapes the next double quotation mark as
       described in rule 3.
    """
    result = []
    needquote = False
    for arg in seq:
        bs_buf = []
        if result:
            result.append(' ')
        needquote = ' ' in arg or '\t' in arg or not arg
        if needquote:
            result.append('"')
        for c in arg:
            if c == '\\':
                bs_buf.append(c)
            elif c == '"':
                result.append('\\' * len(bs_buf) * 2)
                bs_buf = []
                result.append('\\"')
            elif bs_buf:
                result.extend(bs_buf)
                bs_buf = []
            result.append(c)

        if bs_buf:
            result.extend(bs_buf)
        if needquote:
            result.extend(bs_buf)
            result.append('"')

    return ''.join(result)


def getstatusoutput(cmd):
    """Return (exitcode, output) of executing cmd in a shell.

    Execute the string 'cmd' in a shell with 'check_output' and
    return a 2-tuple (status, output). The locale encoding is used
    to decode the output and process newlines.

    A trailing newline is stripped from the output.
    The exit status for the command can be interpreted
    according to the rules for the function 'wait'. Example:

    >>> import subprocess
    >>> subprocess.getstatusoutput('ls /bin/ls')
    (0, '/bin/ls')
    >>> subprocess.getstatusoutput('cat /bin/junk')
    (1, 'cat: /bin/junk: No such file or directory')
    >>> subprocess.getstatusoutput('/bin/junk')
    (127, 'sh: /bin/junk: not found')
    >>> subprocess.getstatusoutput('/bin/kill $$')
    (-15, '')
    """
    try:
        data = check_output(cmd, shell=True, text=True, stderr=STDOUT)
        exitcode = 0
    except CalledProcessError as ex:
        try:
            data = ex.output
            exitcode = ex.returncode
        finally:
            ex = None
            del ex

    if data[-1:] == '\n':
        data = data[:-1]
    return (exitcode, data)


def getoutput(cmd):
    """Return output (stdout or stderr) of executing cmd in a shell.

    Like getstatusoutput(), except the exit status is ignored and the return
    value is a string containing the command's output.  Example:

    >>> import subprocess
    >>> subprocess.getoutput('ls /bin/ls')
    '/bin/ls'
    """
    return getstatusoutput(cmd)[1]


class Popen(object):
    """" Execute a child program in a new process.\\n\\n    For a complete description of the arguments see the Python documentation.\\n\\n    Arguments:\\n      args: A string, or a sequence of program arguments.\\n\\n      bufsize: supplied as the buffering argument to the open() function when\\n          creating the stdin/stdout/stderr pipe file objects\\n\\n      executable: A replacement program to execute.\\n\\n      stdin, stdout and stderr: These specify the executed programs' standard\\n          input, standard output and standard error file handles, respectively.\\n\\n      preexec_fn: (POSIX only) An object to be called in the child process\\n          just before the child is executed.\\n\\n      close_fds: Controls closing or inheriting of file descriptors.\\n\\n      shell: If true, the command will be executed through the shell.\\n\\n      cwd: Sets the current directory before the child is executed.\\n\\n      env: Defines the environment variables for the new process.\\n\\n      text: If true, decode stdin, stdout and stderr using the given encoding\\n          (if set) or the system default otherwise.\\n\\n      universal_newlines: Alias of text, provided for backwards compatibility.\\n\\n      startupinfo and creationflags (Windows only)\\n\\n      restore_signals (POSIX only)\\n\\n      start_new_session (POSIX only)\\n\\n      pass_fds (POSIX only)\\n\\n      encoding and errors: Text mode encoding and error handling to use for\\n          file objects stdin, stdout and stderr.\\n\\n    Attributes:\\n        stdin, stdout, stderr, pid, returncode\\n    \""""
    _child_created = False

    def __init__(self, args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None, errors=None, text=None):
        """Create new Popen instance."""
        _cleanup()
        self._waitpid_lock = threading.Lock()
        self._input = None
        self._communication_started = False
        if bufsize is None:
            bufsize = -1
        if not isinstance(bufsize, int):
            raise TypeError('bufsize must be an integer')
        if _mswindows:
            if preexec_fn is not None:
                raise ValueError('preexec_fn is not supported on Windows platforms')
        if pass_fds:
            if not close_fds:
                warnings.warn('pass_fds overriding close_fds.', RuntimeWarning)
                close_fds = True
            if startupinfo is not None:
                raise ValueError('startupinfo is only supported on Windows platforms')
            if creationflags != 0:
                raise ValueError('creationflags is only supported on Windows platforms')
            self.args = args
            self.stdin = None
            self.stdout = None
            self.stderr = None
            self.pid = None
            self.returncode = None
            self.encoding = encoding
            self.errors = errors
            if text is not None:
                pass
        if universal_newlines is not None:
            if bool(universal_newlines) != bool(text):
                raise SubprocessError('Cannot disambiguate when both text and universal_newlines are supplied but different. Pass one or the other.')
            p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite = self._get_handles(stdin, stdout, stderr)
        if _mswindows:
            if p2cwrite != -1:
                p2cwrite = msvcrt.open_osfhandle(p2cwrite.Detach(), 0)
            if c2pread != -1:
                c2pread = msvcrt.open_osfhandle(c2pread.Detach(), 0)
            if errread != -1:
                errread = msvcrt.open_osfhandle(errread.Detach(), 0)
            self.text_mode = encoding or errors or text or universal_newlines
            self._sigint_wait_secs = 0.25
            self._closed_child_pipe_fds = False
        try:
            if p2cwrite != -1:
                self.stdin = io.open(p2cwrite, 'wb', bufsize)
                if self.text_mode:
                    self.stdin = io.TextIOWrapper((self.stdin), write_through=True, line_buffering=(bufsize == 1),
                      encoding=encoding,
                      errors=errors)
                self.stdout = c2pread != -1 and io.open(c2pread, 'rb', bufsize)
                if self.text_mode:
                    self.stdout = io.TextIOWrapper((self.stdout), encoding=encoding,
                      errors=errors)
                if errread != -1:
                    self.stderr = io.open(errread, 'rb', bufsize)
                    if self.text_mode:
                        self.stderr = io.TextIOWrapper((self.stderr), encoding=encoding,
                          errors=errors)
                    self._execute_child(args, executable, preexec_fn, close_fds, pass_fds, cwd, env, startupinfo, creationflags, shell, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite, restore_signals, start_new_session)
        except:
            for f in filter(None, (self.stdin, self.stdout, self.stderr)):
                try:
                    f.close()
                except OSError:
                    pass

            if not self._closed_child_pipe_fds:
                to_close = []
                if stdin == PIPE:
                    to_close.append(p2cread)
                if stdout == PIPE:
                    to_close.append(c2pwrite)
                if stderr == PIPE:
                    to_close.append(errwrite)
                if hasattr(self, '_devnull'):
                    to_close.append(self._devnull)
                for fd in to_close:
                    try:
                        if _mswindows:
                            pass
                        if isinstance(fd, Handle):
                            fd.Close()
                        else:
                            os.close(fd)
                    except OSError:
                        pass

            raise

    @property
    def universal_newlines(self):
        return self.text_mode

    @universal_newlines.setter
    def universal_newlines(self, universal_newlines):
        self.text_mode = bool(universal_newlines)

    def _translate_newlines(self, data, encoding, errors):
        data = data.decode(encoding, errors)
        return data.replace('\r\n', '\n').replace('\r', '\n')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, value, traceback):
        if self.stdout:
            self.stdout.close()
        if self.stderr:
            self.stderr.close()
        try:
            if self.stdin:
                self.stdin.close()
        finally:
            if exc_type == KeyboardInterrupt:
                if self._sigint_wait_secs > 0:
                    try:
                        self._wait(timeout=(self._sigint_wait_secs))
                    except TimeoutExpired:
                        pass

                    self._sigint_wait_secs = 0
                    return
                self.wait()

    def __del__(self, _maxsize=sys.maxsize, _warn=warnings.warn):
        if not self._child_created:
            return
        if self.returncode is None:
            _warn(('subprocess %s is still running' % self.pid), ResourceWarning,
              source=self)
        self._internal_poll(_deadstate=_maxsize)
        if self.returncode is None:
            pass
        if _active is not None:
            _active.append(self)

    def _get_devnull(self):
        if not hasattr(self, '_devnull'):
            self._devnull = os.open(os.devnull, os.O_RDWR)
        return self._devnull

    def _stdin_write(self, input):
        if input:
            pass
        try:
            self.stdin.write(input)
        except BrokenPipeError:
            pass
        except OSError as exc:
            try:
                if exc.errno == errno.EINVAL:
                    pass
                else:
                    raise
            finally:
                exc = None
                del exc

        try:
            self.stdin.close()
        except BrokenPipeError:
            pass
        except OSError as exc:
            try:
                if exc.errno == errno.EINVAL:
                    pass
                else:
                    raise
            finally:
                exc = None
                del exc

    def communicate(self, input=None, timeout=None):
        """Interact with process: Send data to stdin and close it.
        Read data from stdout and stderr, until end-of-file is
        reached.  Wait for process to terminate.

        The optional "input" argument should be data to be sent to the
        child process, or None, if no data should be sent to the child.
        communicate() returns a tuple (stdout, stderr).

        By default, all communication is in bytes, and therefore any
        "input" should be bytes, and the (stdout, stderr) will be bytes.
        If in text mode (indicated by self.text_mode), any "input" should
        be a string, and (stdout, stderr) will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode
        is triggered by setting any of text, encoding, errors or
        universal_newlines.
        """
        if self._communication_started:
            if input:
                raise ValueError('Cannot send input after starting communication')
            if timeout is None:
                pass
            if not self._communication_started:
                if [
                 self.stdin, self.stdout, self.stderr].count(None) >= 2:
                    stdout = None
                    stderr = None
                    if self.stdin:
                        self._stdin_write(input)
                    elif self.stdout:
                        stdout = self.stdout.read()
                        self.stdout.close()
                    elif self.stderr:
                        stderr = self.stderr.read()
                        self.stderr.close()
                    self.wait()
                else:
                    if timeout is not None:
                        endtime = _time() + timeout
                    else:
                        endtime = None
                    try:
                        try:
                            stdout, stderr = self._communicate(input, endtime, timeout)
                        except KeyboardInterrupt:
                            if timeout is not None:
                                sigint_timeout = min(self._sigint_wait_secs, self._remaining_time(endtime))
                            else:
                                sigint_timeout = self._sigint_wait_secs
                            self._sigint_wait_secs = 0
                            try:
                                self._wait(timeout=sigint_timeout)
                            except TimeoutExpired:
                                pass

                            raise

                    finally:
                        self._communication_started = True

                    sts = self.wait(timeout=(self._remaining_time(endtime)))
                return (
                 stdout, stderr)

    def poll(self):
        """Check if child process has terminated. Set and return returncode
        attribute."""
        return self._internal_poll()

    def _remaining_time(self, endtime):
        """Convenience for _communicate when computing timeouts."""
        if endtime is None:
            return
        else:
            return endtime - _time()

    def _check_timeout(self, endtime, orig_timeout):
        """Convenience for checking if a timeout has expired."""
        if endtime is None:
            return
        if _time() > endtime:
            raise TimeoutExpired(self.args, orig_timeout)

    def wait(self, timeout=None):
        """Wait for child process to terminate; returns self.returncode."""
        if timeout is not None:
            endtime = _time() + timeout
        try:
            return self._wait(timeout=timeout)
        except KeyboardInterrupt:
            if timeout is not None:
                sigint_timeout = min(self._sigint_wait_secs, self._remaining_time(endtime))
            else:
                sigint_timeout = self._sigint_wait_secs
            self._sigint_wait_secs = 0
            try:
                self._wait(timeout=sigint_timeout)
            except TimeoutExpired:
                pass

            raise

    if _mswindows:

        def _get_handles(self, stdin, stdout, stderr):
            """Construct and return tuple with IO objects:
            p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite
            """
            if stdin is None:
                if stdout is None:
                    pass
                return stderr is None and (-1, -1, -1, -1, -1, -1)
            else:
                p2cread, p2cwrite = (-1, -1)
                c2pread, c2pwrite = (-1, -1)
                errread, errwrite = (-1, -1)
                if stdin is None:
                    p2cread = _winapi.GetStdHandle(_winapi.STD_INPUT_HANDLE)
                    if p2cread is None:
                        p2cread, _ = _winapi.CreatePipe(None, 0)
                        p2cread = Handle(p2cread)
                        _winapi.CloseHandle(_)
                    elif stdin == PIPE:
                        p2cread, p2cwrite = _winapi.CreatePipe(None, 0)
                        p2cread, p2cwrite = Handle(p2cread), Handle(p2cwrite)
                    elif stdin == DEVNULL:
                        p2cread = msvcrt.get_osfhandle(self._get_devnull())
                    elif isinstance(stdin, int):
                        p2cread = msvcrt.get_osfhandle(stdin)
                    else:
                        p2cread = msvcrt.get_osfhandle(stdin.fileno())
                p2cread = self._make_inheritable(p2cread)
                if stdout is None:
                    c2pwrite = _winapi.GetStdHandle(_winapi.STD_OUTPUT_HANDLE)
                    if c2pwrite is None:
                        _, c2pwrite = _winapi.CreatePipe(None, 0)
                        c2pwrite = Handle(c2pwrite)
                        _winapi.CloseHandle(_)
                    elif stdout == PIPE:
                        c2pread, c2pwrite = _winapi.CreatePipe(None, 0)
                        c2pread, c2pwrite = Handle(c2pread), Handle(c2pwrite)
                    elif stdout == DEVNULL:
                        c2pwrite = msvcrt.get_osfhandle(self._get_devnull())
                    elif isinstance(stdout, int):
                        c2pwrite = msvcrt.get_osfhandle(stdout)
                    else:
                        c2pwrite = msvcrt.get_osfhandle(stdout.fileno())
                c2pwrite = self._make_inheritable(c2pwrite)
                if stderr is None:
                    errwrite = _winapi.GetStdHandle(_winapi.STD_ERROR_HANDLE)
                    if errwrite is None:
                        _, errwrite = _winapi.CreatePipe(None, 0)
                        errwrite = Handle(errwrite)
                        _winapi.CloseHandle(_)
                    elif stderr == PIPE:
                        errread, errwrite = _winapi.CreatePipe(None, 0)
                        errread, errwrite = Handle(errread), Handle(errwrite)
                    elif stderr == STDOUT:
                        errwrite = c2pwrite
                    elif stderr == DEVNULL:
                        errwrite = msvcrt.get_osfhandle(self._get_devnull())
                    elif isinstance(stderr, int):
                        errwrite = msvcrt.get_osfhandle(stderr)
                    else:
                        errwrite = msvcrt.get_osfhandle(stderr.fileno())
                errwrite = self._make_inheritable(errwrite)
                return (
                 p2cread, p2cwrite,
                 c2pread, c2pwrite,
                 errread, errwrite)

        def _make_inheritable(self, handle):
            """Return a duplicate of handle, which is inheritable"""
            h = _winapi.DuplicateHandle(_winapi.GetCurrentProcess(), handle, _winapi.GetCurrentProcess(), 0, 1, _winapi.DUPLICATE_SAME_ACCESS)
            return Handle(h)

        def _filter_handle_list(self, handle_list):
            """Filter out console handles that can't be used
            in lpAttributeList["handle_list"] and make sure the list
            isn't empty. This also removes duplicate handles."""
            return list({handle for handle in handle_list if handle & 3 != 3 or _winapi.GetFileType(handle) != _winapi.FILE_TYPE_CHAR})

        def _execute_child(self, args, executable, preexec_fn, close_fds, pass_fds, cwd, env, startupinfo, creationflags, shell, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite, unused_restore_signals, unused_start_new_session):
            """Execute program (MS Windows version)"""
            if pass_fds:
                raise AssertionError('pass_fds not supported on Windows.')
            if not isinstance(args, str):
                args = list2cmdline(args)
            if startupinfo is None:
                startupinfo = STARTUPINFO()
            else:
                startupinfo = startupinfo._copy()
            use_std_handles = -1 not in (p2cread, c2pwrite, errwrite)
            if use_std_handles:
                startupinfo.dwFlags |= _winapi.STARTF_USESTDHANDLES
                startupinfo.hStdInput = p2cread
                startupinfo.hStdOutput = c2pwrite
                startupinfo.hStdError = errwrite
            attribute_list = startupinfo.lpAttributeList
            have_handle_list = bool(attribute_list and 'handle_list' in attribute_list and attribute_list['handle_list'])
            if have_handle_list or use_std_handles and close_fds:
                if attribute_list is None:
                    attribute_list = startupinfo.lpAttributeList = {}
                handle_list = attribute_list['handle_list'] = list(attribute_list.get('handle_list', []))
                if use_std_handles:
                    handle_list += [int(p2cread), int(c2pwrite), int(errwrite)]
                handle_list[:] = self._filter_handle_list(handle_list)
                if handle_list:
                    if not close_fds:
                        warnings.warn("startupinfo.lpAttributeList['handle_list'] overriding close_fds", RuntimeWarning)
                    close_fds = False
                if shell:
                    startupinfo.dwFlags |= _winapi.STARTF_USESHOWWINDOW
                    startupinfo.wShowWindow = _winapi.SW_HIDE
                    comspec = os.environ.get('COMSPEC', 'cmd.exe')
                    args = '{} /c "{}"'.format(comspec, args)
                try:
                    hp, ht, pid, tid = _winapi.CreateProcess(executable, args, None, None, int(not close_fds), creationflags, env, os.fspath(cwd) if cwd is not None else None, startupinfo)
                finally:
                    if p2cread != -1:
                        p2cread.Close()
                    if c2pwrite != -1:
                        c2pwrite.Close()
                    if errwrite != -1:
                        errwrite.Close()
                    if hasattr(self, '_devnull'):
                        os.close(self._devnull)
                    self._closed_child_pipe_fds = True

                self._child_created = True
                self._handle = Handle(hp)
                self.pid = pid
                _winapi.CloseHandle(ht)

        def _internal_poll(self, _deadstate=None, _WaitForSingleObject=_winapi.WaitForSingleObject, _WAIT_OBJECT_0=_winapi.WAIT_OBJECT_0, _GetExitCodeProcess=_winapi.GetExitCodeProcess):
            """Check if child process has terminated.  Returns returncode
            attribute.

            This method is called by __del__, so it can only refer to objects
            in its local scope.

            """
            if self.returncode is None:
                if _WaitForSingleObject(self._handle, 0) == _WAIT_OBJECT_0:
                    self.returncode = _GetExitCodeProcess(self._handle)
                return self.returncode

        def _wait(self, timeout):
            """Internal implementation of wait() on Windows."""
            if timeout is None:
                timeout_millis = _winapi.INFINITE
            else:
                timeout_millis = int(timeout * 1000)
            if self.returncode is None:
                result = _winapi.WaitForSingleObject(self._handle, timeout_millis)
                if result == _winapi.WAIT_TIMEOUT:
                    raise TimeoutExpired(self.args, timeout)
                self.returncode = _winapi.GetExitCodeProcess(self._handle)
            return self.returncode

        def _readerthread(self, fh, buffer):
            buffer.append(fh.read())
            fh.close()

        def _communicate(self, input, endtime, orig_timeout):
            if self.stdout:
                if not hasattr(self, '_stdout_buff'):
                    self._stdout_buff = []
                    self.stdout_thread = threading.Thread(target=(self._readerthread), args=(
                     self.stdout, self._stdout_buff))
                    self.stdout_thread.daemon = True
                    self.stdout_thread.start()
                if self.stderr:
                    if not hasattr(self, '_stderr_buff'):
                        self._stderr_buff = []
                        self.stderr_thread = threading.Thread(target=(self._readerthread), args=(
                         self.stderr, self._stderr_buff))
                        self.stderr_thread.daemon = True
                        self.stderr_thread.start()
                    if self.stdin:
                        self._stdin_write(input)
                    if self.stdout is not None:
                        self.stdout_thread.join(self._remaining_time(endtime))
                if self.stdout_thread.is_alive():
                    raise TimeoutExpired(self.args, orig_timeout)
                if self.stderr is not None:
                    self.stderr_thread.join(self._remaining_time(endtime))
                    if self.stderr_thread.is_alive():
                        raise TimeoutExpired(self.args, orig_timeout)
                    stdout = None
                    stderr = None
                    if self.stdout:
                        stdout = self._stdout_buff
                        self.stdout.close()
                    if self.stderr:
                        stderr = self._stderr_buff
                        self.stderr.close()
                    if stdout is not None:
                        stdout = stdout[0]
                    if stderr is not None:
                        stderr = stderr[0]
                    return (
                     stdout, stderr)

        def send_signal(self, sig):
            """Send a signal to the process."""
            if self.returncode is not None:
                return
            if sig == signal.SIGTERM:
                self.terminate()
            elif sig == signal.CTRL_C_EVENT:
                os.kill(self.pid, signal.CTRL_C_EVENT)
            elif sig == signal.CTRL_BREAK_EVENT:
                os.kill(self.pid, signal.CTRL_BREAK_EVENT)
            else:
                raise ValueError('Unsupported signal: {}'.format(sig))

        def terminate(self):
            """Terminates the process."""
            if self.returncode is not None:
                return
            try:
                _winapi.TerminateProcess(self._handle, 1)
            except PermissionError:
                rc = _winapi.GetExitCodeProcess(self._handle)
                if rc == _winapi.STILL_ACTIVE:
                    raise
                self.returncode = rc

        kill = terminate
    else:

        def _get_handles(self, stdin, stdout, stderr):
            """Construct and return tuple with IO objects:
            p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite
            """
            p2cread, p2cwrite = (-1, -1)
            c2pread, c2pwrite = (-1, -1)
            errread, errwrite = (-1, -1)
            if stdin is None:
                pass
            elif stdin == PIPE:
                p2cread, p2cwrite = os.pipe()
            elif stdin == DEVNULL:
                p2cread = self._get_devnull()
            elif isinstance(stdin, int):
                p2cread = stdin
            else:
                p2cread = stdin.fileno()
            if stdout is None:
                pass
            elif stdout == PIPE:
                c2pread, c2pwrite = os.pipe()
            elif stdout == DEVNULL:
                c2pwrite = self._get_devnull()
            elif isinstance(stdout, int):
                c2pwrite = stdout
            else:
                c2pwrite = stdout.fileno()
            if stderr is None:
                pass
            elif stderr == PIPE:
                errread, errwrite = os.pipe()
            elif stderr == STDOUT:
                if c2pwrite != -1:
                    errwrite = c2pwrite
                else:
                    errwrite = sys.__stdout__.fileno()
            elif stderr == DEVNULL:
                errwrite = self._get_devnull()
            elif isinstance(stderr, int):
                errwrite = stderr
            else:
                errwrite = stderr.fileno()
            return (
             p2cread, p2cwrite,
             c2pread, c2pwrite,
             errread, errwrite)

        def _execute_child(self, args, executable, preexec_fn, close_fds, pass_fds, cwd, env, startupinfo, creationflags, shell, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite, restore_signals, start_new_session):
            """Execute program (POSIX version)"""
            if isinstance(args, (str, bytes)):
                args = [
                 args]
            else:
                args = list(args)
            if shell:
                unix_shell = '/system/bin/sh' if hasattr(sys, 'getandroidapilevel') else '/bin/sh'
                args = [unix_shell, '-c'] + args
                if executable:
                    args[0] = executable
                if executable is None:
                    executable = args[0]
                orig_executable = executable
                errpipe_read, errpipe_write = os.pipe()
                low_fds_to_close = []
                while 1:
                    if errpipe_write < 3:
                        low_fds_to_close.append(errpipe_write)
                        errpipe_write = os.dup(errpipe_write)

                for low_fd in low_fds_to_close:
                    os.close(low_fd)

                try:
                    try:
                        if env is not None:
                            env_list = []
                            for k, v in env.items():
                                k = os.fsencode(k)
                                if '=' in k:
                                    raise ValueError('illegal environment variable name')
                                env_list.append(k + '=' + os.fsencode(v))

                        else:
                            env_list = None
                        executable = os.fsencode(executable)
                        if os.path.dirname(executable):
                            executable_list = (
                             executable,)
                        else:
                            executable_list = tuple(os.path.join(os.fsencode(dir), executable) for dir in os.get_exec_path(env))
                        fds_to_keep = set(pass_fds)
                        fds_to_keep.add(errpipe_write)
                        self.pid = _posixsubprocess.fork_exec(args, executable_list, close_fds, tuple(sorted(map(int, fds_to_keep))), cwd, env_list, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite, errpipe_read, errpipe_write, restore_signals, start_new_session, preexec_fn)
                        self._child_created = True
                    finally:
                        os.close(errpipe_write)

                    devnull_fd = getattr(self, '_devnull', None)
                    if p2cread != -1:
                        pass
                    if p2cwrite != -1:
                        if p2cread != devnull_fd:
                            os.close(p2cread)
                        if c2pwrite != -1:
                            pass
                    if c2pread != -1:
                        if c2pwrite != devnull_fd:
                            os.close(c2pwrite)
                        if errwrite != -1:
                            pass
                    if errread != -1:
                        if errwrite != devnull_fd:
                            os.close(errwrite)
                        if devnull_fd is not None:
                            os.close(devnull_fd)
                        self._closed_child_pipe_fds = True
                        errpipe_data = bytearray()
                        while 1:
                            part = os.read(errpipe_read, 50000)
                            errpipe_data += part
                            if part and len(errpipe_data) > 50000:
                                break

                finally:
                    os.close(errpipe_read)

            if errpipe_data:
                try:
                    pid, sts = os.waitpid(self.pid, 0)
                    if pid == self.pid:
                        self._handle_exitstatus(sts)
                    else:
                        self.returncode = sys.maxsize
                except ChildProcessError:
                    pass

                try:
                    exception_name, hex_errno, err_msg = errpipe_data.split(':', 2)
                    err_msg = err_msg.decode()
                except ValueError:
                    exception_name = 'SubprocessError'
                    hex_errno = '0'
                    err_msg = 'Bad exception data from child: {!r}'.format(bytes(errpipe_data))

                child_exception_type = getattr(builtins, exception_name.decode('ascii'), SubprocessError)
                if issubclass(child_exception_type, OSError):
                    pass
            if hex_errno:
                errno_num = int(hex_errno, 16)
                child_exec_never_called = err_msg == 'noexec'
                if child_exec_never_called:
                    err_msg = ''
                    err_filename = cwd
                else:
                    err_filename = orig_executable
                if errno_num != 0:
                    err_msg = os.strerror(errno_num)
                    if errno_num == errno.ENOENT:
                        err_msg += ': ' + repr(err_filename)
                    raise child_exception_type(errno_num, err_msg, err_filename)
                raise child_exception_type(err_msg)

        def _handle_exitstatus(self, sts, _WIFSIGNALED=os.WIFSIGNALED, _WTERMSIG=os.WTERMSIG, _WIFEXITED=os.WIFEXITED, _WEXITSTATUS=os.WEXITSTATUS, _WIFSTOPPED=os.WIFSTOPPED, _WSTOPSIG=os.WSTOPSIG):
            """All callers to this function MUST hold self._waitpid_lock."""
            if _WIFSIGNALED(sts):
                self.returncode = -_WTERMSIG(sts)
            elif _WIFEXITED(sts):
                self.returncode = _WEXITSTATUS(sts)
            elif _WIFSTOPPED(sts):
                self.returncode = -_WSTOPSIG(sts)
            else:
                raise SubprocessError('Unknown child exit status!')

        def _internal_poll(self, _deadstate=None, _waitpid=os.waitpid, _WNOHANG=os.WNOHANG, _ECHILD=errno.ECHILD):
            """Check if child process has terminated.  Returns returncode
            attribute.

            This method is called by __del__, so it cannot reference anything
            outside of the local scope (nor can any methods it calls).

            """
            if self.returncode is None:
                if not self._waitpid_lock.acquire(False):
                    return
                try:
                    try:
                        if self.returncode is not None:
                            return self.returncode
                        pid, sts = _waitpid(self.pid, _WNOHANG)
                        if pid == self.pid:
                            self._handle_exitstatus(sts)
                    except OSError as e:
                        try:
                            if _deadstate is not None:
                                self.returncode = _deadstate
                            elif e.errno == _ECHILD:
                                self.returncode = 0
                        finally:
                            e = None
                            del e

                finally:
                    self._waitpid_lock.release()

            return self.returncode

        def _try_wait(self, wait_flags):
            """All callers to this function MUST hold self._waitpid_lock."""
            try:
                pid, sts = os.waitpid(self.pid, wait_flags)
            except ChildProcessError:
                pid = self.pid
                sts = 0

            return (pid, sts)

        def _wait(self, timeout):
            """Internal implementation of wait() on POSIX."""
            if self.returncode is not None:
                return self.returncode
            else:
                if timeout is not None:
                    endtime = _time() + timeout
                    delay = 0.0005
                    while True:
                        if self._waitpid_lock.acquire(False):
                            try:
                                if self.returncode is not None:
                                    break
                                pid, sts = self._try_wait(os.WNOHANG)
                                if not pid == self.pid:
                                    if not pid == 0:
                                        raise AssertionError
                                    if pid == self.pid:
                                        self._handle_exitstatus(sts)
                                        break
                            finally:
                                self._waitpid_lock.release()

                        remaining = self._remaining_time(endtime)
                        if remaining <= 0:
                            raise TimeoutExpired(self.args, timeout)
                        delay = min(delay * 2, remaining, 0.05)
                        time.sleep(delay)

                else:
                    while self.returncode is None:
                        with self._waitpid_lock:
                            if self.returncode is not None:
                                break
                            pid, sts = self._try_wait(0)
                            if pid == self.pid:
                                self._handle_exitstatus(sts)

                return self.returncode

        def _communicate(self, input, endtime, orig_timeout):
            if not (self.stdin and self._communication_started):
                try:
                    self.stdin.flush()
                except BrokenPipeError:
                    pass

                if not input:
                    pass
                try:
                    self.stdin.close()
                except BrokenPipeError:
                    pass

                stdout = None
                stderr = None
                if not self._communication_started:
                    self._fileobj2output = {}
                    if self.stdout:
                        self._fileobj2output[self.stdout] = []
                    if self.stderr:
                        self._fileobj2output[self.stderr] = []
                    if self.stdout:
                        stdout = self._fileobj2output[self.stdout]
                    if self.stderr:
                        stderr = self._fileobj2output[self.stderr]
                    self._save_input(input)
                    if self._input:
                        input_view = memoryview(self._input)
                    with _PopenSelector() as (selector):
                        if self.stdin:
                            if input:
                                selector.register(self.stdin, selectors.EVENT_WRITE)
                            if self.stdout:
                                selector.register(self.stdout, selectors.EVENT_READ)
                            if self.stderr:
                                selector.register(self.stderr, selectors.EVENT_READ)
                            while selector.get_map():
                                timeout = self._remaining_time(endtime)
                                if timeout is not None:
                                    if timeout < 0:
                                        raise TimeoutExpired(self.args, orig_timeout)
                                    ready = selector.select(timeout)
                                    self._check_timeout(endtime, orig_timeout)
                                    for key, events in ready:
                                        if key.fileobj is self.stdin:
                                            chunk = input_view[self._input_offset:self._input_offset + _PIPE_BUF]
                                            try:
                                                self._input_offset += os.write(key.fd, chunk)
                                            except BrokenPipeError:
                                                selector.unregister(key.fileobj)
                                                key.fileobj.close()
                                            else:
                                                if self._input_offset >= len(self._input):
                                                    selector.unregister(key.fileobj)
                                                    key.fileobj.close()
                                                elif key.fileobj in (self.stdout, self.stderr):
                                                    data = os.read(key.fd, 32768)
                                                    if not data:
                                                        selector.unregister(key.fileobj)
                                                        key.fileobj.close()
                                                    self._fileobj2output[key.fileobj].append(data)

                    self.wait(timeout=(self._remaining_time(endtime)))
                    if stdout is not None:
                        stdout = ''.join(stdout)
                    if stderr is not None:
                        stderr = ''.join(stderr)
                if self.text_mode:
                    if stdout is not None:
                        stdout = self._translate_newlines(stdout, self.stdout.encoding, self.stdout.errors)
                    if stderr is not None:
                        stderr = self._translate_newlines(stderr, self.stderr.encoding, self.stderr.errors)
                    return (
                     stdout, stderr)

        def _save_input(self, input):
            if self.stdin:
                if self._input is None:
                    self._input_offset = 0
                    self._input = input
                    if input is not None:
                        pass
            if self.text_mode:
                self._input = self._input.encode(self.stdin.encoding, self.stdin.errors)

        def send_signal(self, sig):
            """Send a signal to the process."""
            if self.returncode is None:
                os.kill(self.pid, sig)

        def terminate(self):
            """Terminate the process with SIGTERM
            """
            self.send_signal(signal.SIGTERM)

        def kill(self):
            """Kill the process with SIGKILL
            """
            self.send_signal(signal.SIGKILL)