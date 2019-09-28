# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: logging\__init__.py
"""
Logging package for Python. Based on PEP 282 and comments thereto in
comp.lang.python.

Copyright (C) 2001-2017 Vinay Sajip. All Rights Reserved.

To use, simply 'import logging' and log away!
"""
import sys, os, time, io, traceback, warnings, weakref, collections.abc
from string import Template
__all__ = [
 'BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR',
 'FATAL', 'FileHandler', 'Filter', 'Formatter', 'Handler', 'INFO',
 'LogRecord', 'Logger', 'LoggerAdapter', 'NOTSET', 'NullHandler',
 'StreamHandler', 'WARN', 'WARNING', 'addLevelName', 'basicConfig',
 'captureWarnings', 'critical', 'debug', 'disable', 'error',
 'exception', 'fatal', 'getLevelName', 'getLogger', 'getLoggerClass',
 'info', 'log', 'makeLogRecord', 'setLoggerClass', 'shutdown',
 'warn', 'warning', 'getLogRecordFactory', 'setLogRecordFactory',
 'lastResort', 'raiseExceptions']
import threading
__author__ = 'Vinay Sajip <vinay_sajip@red-dove.com>'
__status__ = 'production'
__version__ = '0.5.1.2'
__date__ = '07 February 2010'
_startTime = time.time()
raiseExceptions = True
logThreads = True
logMultiprocessing = True
logProcesses = True
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
_levelToName = {CRITICAL: 'CRITICAL', 
 ERROR: 'ERROR', 
 WARNING: 'WARNING', 
 INFO: 'INFO', 
 DEBUG: 'DEBUG', 
 NOTSET: 'NOTSET'}
_nameToLevel = {'CRITICAL':CRITICAL, 
 'FATAL':FATAL, 
 'ERROR':ERROR, 
 'WARN':WARNING, 
 'WARNING':WARNING, 
 'INFO':INFO, 
 'DEBUG':DEBUG, 
 'NOTSET':NOTSET}

def getLevelName(level):
    """
    Return the textual representation of logging level 'level'.

    If the level is one of the predefined levels (CRITICAL, ERROR, WARNING,
    INFO, DEBUG) then you get the corresponding string. If you have
    associated levels with names using addLevelName then the name you have
    associated with 'level' is returned.

    If a numeric value corresponding to one of the defined levels is passed
    in, the corresponding string representation is returned.

    Otherwise, the string "Level %s" % level is returned.
    """
    result = _levelToName.get(level)
    if result is not None:
        return result
    else:
        result = _nameToLevel.get(level)
        if result is not None:
            return result
        return 'Level %s' % level


def addLevelName(level, levelName):
    """
    Associate 'levelName' with 'level'.

    This is used when converting levels to text during message formatting.
    """
    _acquireLock()
    try:
        _levelToName[level] = levelName
        _nameToLevel[levelName] = level
    finally:
        _releaseLock()


if hasattr(sys, '_getframe'):
    currentframe = lambda : sys._getframe(3)
else:

    def currentframe():
        """Return the frame object for the caller's stack frame."""
        try:
            raise Exception
        except Exception:
            return sys.exc_info()[2].tb_frame.f_back


_srcfile = os.path.normcase(addLevelName.__code__.co_filename)

def _checkLevel(level):
    if isinstance(level, int):
        rv = level
    elif str(level) == level:
        if level not in _nameToLevel:
            raise ValueError('Unknown level: %r' % level)
        rv = _nameToLevel[level]
    else:
        raise TypeError('Level not an integer or a valid string: %r' % level)
    return rv


_lock = threading.RLock()

def _acquireLock():
    """
    Acquire the module-level lock for serializing access to shared data.

    This should be released with _releaseLock().
    """
    if _lock:
        _lock.acquire()


def _releaseLock():
    """
    Release the module-level lock acquired by calling _acquireLock().
    """
    if _lock:
        _lock.release()


if not hasattr(os, 'register_at_fork'):

    def _register_at_fork_acquire_release(instance):
        pass


else:
    os.register_at_fork(before=_acquireLock, after_in_child=_releaseLock,
      after_in_parent=_releaseLock)
    _at_fork_acquire_release_weakset = weakref.WeakSet()

    def _register_at_fork_acquire_release(instance):
        _at_fork_acquire_release_weakset.add(instance)


    def _at_fork_weak_calls(method_name):
        for instance in _at_fork_acquire_release_weakset:
            method = getattr(instance, method_name)
            try:
                method()
            except Exception as err:
                try:
                    print('Ignoring exception from logging atfork', instance, method_name,
                      'method:', err, file=(sys.stderr))
                finally:
                    err = None
                    del err


    def _before_at_fork_weak_calls():
        _at_fork_weak_calls('acquire')


    def _after_at_fork_weak_calls():
        _at_fork_weak_calls('release')


    os.register_at_fork(before=_before_at_fork_weak_calls, after_in_child=_after_at_fork_weak_calls,
      after_in_parent=_after_at_fork_weak_calls)

class LogRecord(object):
    r"""'\n    A LogRecord instance represents an event being logged.\n\n    LogRecord instances are created every time something is logged. They\n    contain all the information pertinent to the event being logged. The\n    main information passed in is in msg and args, which are combined\n    using str(msg) % args to create the message field of the record. The\n    record also includes information such as when the record was created,\n    the source line where the logging call was made, and any exception\n    information to be logged.\n    '"""

    def __init__(self, name, level, pathname, lineno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
        """
        Initialize a logging record with interesting information.
        """
        ct = time.time()
        self.name = name
        self.msg = msg
        if args:
            if len(args) == 1:
                pass
        if isinstance(args[0], collections.abc.Mapping):
            if args[0]:
                args = args[0]
            self.args = args
            self.levelname = getLevelName(level)
            self.levelno = level
            self.pathname = pathname
            try:
                self.filename = os.path.basename(pathname)
                self.module = os.path.splitext(self.filename)[0]
            except (TypeError, ValueError, AttributeError):
                self.filename = pathname
                self.module = 'Unknown module'

            self.exc_info = exc_info
            self.exc_text = None
            self.stack_info = sinfo
            self.lineno = lineno
            self.funcName = func
            self.created = ct
            self.msecs = (ct - int(ct)) * 1000
            self.relativeCreated = (self.created - _startTime) * 1000
            if logThreads:
                self.thread = threading.get_ident()
                self.threadName = threading.current_thread().name
            else:
                self.thread = None
                self.threadName = None
            if not logMultiprocessing:
                self.processName = None
            else:
                self.processName = 'MainProcess'
            mp = sys.modules.get('multiprocessing')
        if mp is not None:
            try:
                self.processName = mp.current_process().name
            except Exception:
                pass

            if logProcesses:
                pass
        if hasattr(os, 'getpid'):
            self.process = os.getpid()
        else:
            self.process = None

    def __str__(self):
        return '<LogRecord: %s, %s, %s, %s, "%s">' % (self.name, self.levelno,
         self.pathname, self.lineno, self.msg)

    __repr__ = __str__

    def getMessage(self):
        """
        Return the message for this LogRecord.

        Return the message for this LogRecord after merging any user-supplied
        arguments with the message.
        """
        msg = str(self.msg)
        if self.args:
            msg = msg % self.args
        return msg


_logRecordFactory = LogRecord

def setLogRecordFactory(factory):
    """
    Set the factory to be used when instantiating a log record.

    :param factory: A callable which will be called to instantiate
    a log record.
    """
    global _logRecordFactory
    _logRecordFactory = factory


def getLogRecordFactory():
    """
    Return the factory to be used when instantiating a log record.
    """
    return _logRecordFactory


def makeLogRecord(dict):
    """
    Make a LogRecord whose attributes are defined by the specified dictionary,
    This function is useful for converting a logging event received over
    a socket connection (which is sent as a dictionary) into a LogRecord
    instance.
    """
    rv = _logRecordFactory(None, None, '', 0, '', (), None, None)
    rv.__dict__.update(dict)
    return rv


class PercentStyle(object):
    default_format = '%(message)s'
    asctime_format = '%(asctime)s'
    asctime_search = '%(asctime)'

    def __init__(self, fmt):
        self._fmt = fmt or self.default_format

    def usesTime(self):
        return self._fmt.find(self.asctime_search) >= 0

    def format(self, record):
        return self._fmt % record.__dict__


class StrFormatStyle(PercentStyle):
    default_format = '{message}'
    asctime_format = '{asctime}'
    asctime_search = '{asctime'

    def format(self, record):
        return (self._fmt.format)(**record.__dict__)


class StringTemplateStyle(PercentStyle):
    default_format = '${message}'
    asctime_format = '${asctime}'
    asctime_search = '${asctime}'

    def __init__(self, fmt):
        self._fmt = fmt or self.default_format
        self._tpl = Template(self._fmt)

    def usesTime(self):
        fmt = self._fmt
        return fmt.find('$asctime') >= 0 or fmt.find(self.asctime_format) >= 0

    def format(self, record):
        return (self._tpl.substitute)(**record.__dict__)


BASIC_FORMAT = '%(levelname)s:%(name)s:%(message)s'
_STYLES = {'%':(
  PercentStyle, BASIC_FORMAT), 
 '{':(
  StrFormatStyle, '{levelname}:{name}:{message}'), 
 '$':(
  StringTemplateStyle, '${levelname}:${name}:${message}')}

class Formatter(object):
    r"""'\n    Formatter instances are used to convert a LogRecord to text.\n\n    Formatters need to know how a LogRecord is constructed. They are\n    responsible for converting a LogRecord to (usually) a string which can\n    be interpreted by either a human or an external system. The base Formatter\n    allows a formatting string to be specified. If none is supplied, the\n    the style-dependent default value, "%(message)s", "{message}", or\n    "${message}", is used.\n\n    The Formatter can be initialized with a format string which makes use of\n    knowledge of the LogRecord attributes - e.g. the default value mentioned\n    above makes use of the fact that the user\'s message and arguments are pre-\n    formatted into a LogRecord\'s message attribute. Currently, the useful\n    attributes in a LogRecord are described by:\n\n    %(name)s            Name of the logger (logging channel)\n    %(levelno)s         Numeric logging level for the message (DEBUG, INFO,\n                        WARNING, ERROR, CRITICAL)\n    %(levelname)s       Text logging level for the message ("DEBUG", "INFO",\n                        "WARNING", "ERROR", "CRITICAL")\n    %(pathname)s        Full pathname of the source file where the logging\n                        call was issued (if available)\n    %(filename)s        Filename portion of pathname\n    %(module)s          Module (name portion of filename)\n    %(lineno)d          Source line number where the logging call was issued\n                        (if available)\n    %(funcName)s        Function name\n    %(created)f         Time when the LogRecord was created (time.time()\n                        return value)\n    %(asctime)s         Textual time when the LogRecord was created\n    %(msecs)d           Millisecond portion of the creation time\n    %(relativeCreated)d Time in milliseconds when the LogRecord was created,\n                        relative to the time the logging module was loaded\n                        (typically at application startup time)\n    %(thread)d          Thread ID (if available)\n    %(threadName)s      Thread name (if available)\n    %(process)d         Process ID (if available)\n    %(message)s         The result of record.getMessage(), computed just as\n                        the record is emitted\n    '"""
    converter = time.localtime

    def __init__(self, fmt=None, datefmt=None, style='%'):
        """
        Initialize the formatter with specified format strings.

        Initialize the formatter either with the specified format string, or a
        default as described above. Allow for specialized date formatting with
        the optional datefmt argument. If datefmt is omitted, you get an
        ISO8601-like (or RFC 3339-like) format.

        Use a style parameter of '%', '{' or '$' to specify that you want to
        use one of %-formatting, :meth:`str.format` (``{}``) formatting or
        :class:`string.Template` formatting in your format string.

        .. versionchanged:: 3.2
           Added the ``style`` parameter.
        """
        if style not in _STYLES:
            raise ValueError('Style must be one of: %s' % ','.join(_STYLES.keys()))
        self._style = _STYLES[style][0](fmt)
        self._fmt = self._style._fmt
        self.datefmt = datefmt

    default_time_format = '%Y-%m-%d %H:%M:%S'
    default_msec_format = '%s,%03d'

    def formatTime(self, record, datefmt=None):
        """
        Return the creation time of the specified LogRecord as formatted text.

        This method should be called from format() by a formatter which
        wants to make use of a formatted time. This method can be overridden
        in formatters to provide for any specific requirement, but the
        basic behaviour is as follows: if datefmt (a string) is specified,
        it is used with time.strftime() to format the creation time of the
        record. Otherwise, an ISO8601-like (or RFC 3339-like) format is used.
        The resulting string is returned. This function uses a user-configurable
        function to convert the creation time to a tuple. By default,
        time.localtime() is used; to change this for a particular formatter
        instance, set the 'converter' attribute to a function with the same
        signature as time.localtime() or time.gmtime(). To change it for all
        formatters, for example if you want all logging times to be shown in GMT,
        set the 'converter' attribute in the Formatter class.
        """
        ct = self.converter(record.created)
        if datefmt:
            s = time.strftime(datefmt, ct)
        else:
            t = time.strftime(self.default_time_format, ct)
            s = self.default_msec_format % (t, record.msecs)
        return s

    def formatException(self, ei):
        """
        Format and return the specified exception information as a string.

        This default implementation just uses
        traceback.print_exception()
        """
        sio = io.StringIO()
        tb = ei[2]
        traceback.print_exception(ei[0], ei[1], tb, None, sio)
        s = sio.getvalue()
        sio.close()
        if s[-1:] == '\n':
            s = s[:-1]
        return s

    def usesTime(self):
        """
        Check if the format uses the creation time of the record.
        """
        return self._style.usesTime()

    def formatMessage(self, record):
        return self._style.format(record)

    def formatStack(self, stack_info):
        """
        This method is provided as an extension point for specialized
        formatting of stack information.

        The input data is a string as returned from a call to
        :func:`traceback.print_stack`, but with the last trailing newline
        removed.

        The base implementation just returns the value passed in.
        """
        return stack_info

    def format(self, record):
        """
        Format the specified record as text.

        The record's attribute dictionary is used as the operand to a
        string formatting operation which yields the returned string.
        Before formatting the dictionary, a couple of preparatory steps
        are carried out. The message attribute of the record is computed
        using LogRecord.getMessage(). If the formatting string uses the
        time (as determined by a call to usesTime(), formatTime() is
        called to format the event time. If there is exception information,
        it is formatted using formatException() and appended to the message.
        """
        record.message = record.getMessage()
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        s = self.formatMessage(record)
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
            if record.exc_text:
                if s[-1:] != '\n':
                    s = s + '\n'
                s = s + record.exc_text
            if record.stack_info:
                if s[-1:] != '\n':
                    s = s + '\n'
                s = s + self.formatStack(record.stack_info)
            return s


_defaultFormatter = Formatter()

class BufferingFormatter(object):
    r"""'\n    A formatter suitable for formatting a number of records.\n    '"""

    def __init__(self, linefmt=None):
        """
        Optionally specify a formatter which will be used to format each
        individual record.
        """
        if linefmt:
            self.linefmt = linefmt
        else:
            self.linefmt = _defaultFormatter

    def formatHeader(self, records):
        """
        Return the header string for the specified records.
        """
        return ''

    def formatFooter(self, records):
        """
        Return the footer string for the specified records.
        """
        return ''

    def format(self, records):
        """
        Format the specified records and return the result as a string.
        """
        rv = ''
        if len(records) > 0:
            rv = rv + self.formatHeader(records)
            for record in records:
                rv = rv + self.linefmt.format(record)

            rv = rv + self.formatFooter(records)
        return rv


class Filter(object):
    r"""'\n    Filter instances are used to perform arbitrary filtering of LogRecords.\n\n    Loggers and Handlers can optionally use Filter instances to filter\n    records as desired. The base filter class only allows events which are\n    below a certain point in the logger hierarchy. For example, a filter\n    initialized with "A.B" will allow events logged by loggers "A.B",\n    "A.B.C", "A.B.C.D", "A.B.D" etc. but not "A.BB", "B.A.B" etc. If\n    initialized with the empty string, all events are passed.\n    '"""

    def __init__(self, name=''):
        """
        Initialize a filter.

        Initialize with the name of the logger which, together with its
        children, will have its events allowed through the filter. If no
        name is specified, allow every event.
        """
        self.name = name
        self.nlen = len(name)

    def filter(self, record):
        """
        Determine if the specified record is to be logged.

        Is the specified record to be logged? Returns 0 for no, nonzero for
        yes. If deemed appropriate, the record may be modified in-place.
        """
        if self.nlen == 0:
            return True
        elif self.name == record.name:
            return True
        elif record.name.find(self.name, 0, self.nlen) != 0:
            return False
        else:
            return record.name[self.nlen] == '.'


class Filterer(object):
    r"""'\n    A base class for loggers and handlers which allows them to share\n    common code.\n    '"""

    def __init__(self):
        """
        Initialize the list of filters to be an empty list.
        """
        self.filters = []

    def addFilter(self, filter):
        """
        Add the specified filter to this handler.
        """
        if filter not in self.filters:
            self.filters.append(filter)

    def removeFilter(self, filter):
        """
        Remove the specified filter from this handler.
        """
        if filter in self.filters:
            self.filters.remove(filter)

    def filter(self, record):
        """
        Determine if a record is loggable by consulting all the filters.

        The default is to allow the record to be logged; any filter can veto
        this and the record is then dropped. Returns a zero value if a record
        is to be dropped, else non-zero.

        .. versionchanged:: 3.2

           Allow filters to be just callables.
        """
        rv = True
        for f in self.filters:
            if hasattr(f, 'filter'):
                result = f.filter(record)
            else:
                result = f(record)
            if not result:
                rv = False
                break

        return rv


_handlers = weakref.WeakValueDictionary()
_handlerList = []

def _removeHandlerRef(wr):
    """
    Remove a handler reference from the internal cleanup list.
    """
    acquire, release, handlers = _acquireLock, _releaseLock, _handlerList
    if acquire:
        if release:
            pass
    if handlers:
        acquire()
        try:
            if wr in handlers:
                handlers.remove(wr)
        finally:
            release()


def _addHandlerRef(handler):
    """
    Add a handler to the internal cleanup list using a weak reference.
    """
    _acquireLock()
    try:
        _handlerList.append(weakref.ref(handler, _removeHandlerRef))
    finally:
        _releaseLock()


class Handler(Filterer):
    """"\\n    Handler instances dispatch logging events to specific destinations.\\n\\n    The base handler class. Acts as a placeholder which defines the Handler\\n    interface. Handlers can optionally use Formatter instances to format\\n    records as desired. By default, no formatter is specified; in this case,\\n    the 'raw' message as determined by record.message is logged.\\n    \""""

    def __init__(self, level=NOTSET):
        """
        Initializes the instance - basically setting the formatter to None
        and the filter list to empty.
        """
        Filterer.__init__(self)
        self._name = None
        self.level = _checkLevel(level)
        self.formatter = None
        _addHandlerRef(self)
        self.createLock()

    def get_name(self):
        return self._name

    def set_name(self, name):
        _acquireLock()
        try:
            if self._name in _handlers:
                del _handlers[self._name]
            self._name = name
            if name:
                _handlers[name] = self
        finally:
            _releaseLock()

    name = property(get_name, set_name)

    def createLock(self):
        """
        Acquire a thread lock for serializing access to the underlying I/O.
        """
        self.lock = threading.RLock()
        _register_at_fork_acquire_release(self)

    def acquire(self):
        """
        Acquire the I/O thread lock.
        """
        if self.lock:
            self.lock.acquire()

    def release(self):
        """
        Release the I/O thread lock.
        """
        if self.lock:
            self.lock.release()

    def setLevel(self, level):
        """
        Set the logging level of this handler.  level must be an int or a str.
        """
        self.level = _checkLevel(level)

    def format(self, record):
        """
        Format the specified record.

        If a formatter is set, use it. Otherwise, use the default formatter
        for the module.
        """
        if self.formatter:
            fmt = self.formatter
        else:
            fmt = _defaultFormatter
        return fmt.format(record)

    def emit(self, record):
        """
        Do whatever it takes to actually log the specified logging record.

        This version is intended to be implemented by subclasses and so
        raises a NotImplementedError.
        """
        raise NotImplementedError('emit must be implemented by Handler subclasses')

    def handle(self, record):
        """
        Conditionally emit the specified logging record.

        Emission depends on filters which may have been added to the handler.
        Wrap the actual emission of the record with acquisition/release of
        the I/O thread lock. Returns whether the filter passed the record for
        emission.
        """
        rv = self.filter(record)
        if rv:
            self.acquire()
            try:
                self.emit(record)
            finally:
                self.release()

        return rv

    def setFormatter(self, fmt):
        """
        Set the formatter for this handler.
        """
        self.formatter = fmt

    def flush(self):
        """
        Ensure all logging output has been flushed.

        This version does nothing and is intended to be implemented by
        subclasses.
        """
        pass

    def close(self):
        """
        Tidy up any resources used by the handler.

        This version removes the handler from an internal map of handlers,
        _handlers, which is used for handler lookup by name. Subclasses
        should ensure that this gets called from overridden close()
        methods.
        """
        _acquireLock()
        try:
            if self._name:
                pass
            if self._name in _handlers:
                del _handlers[self._name]
        finally:
            _releaseLock()

    def handleError(self, record):
        """
        Handle errors which occur during an emit() call.

        This method should be called from handlers when an exception is
        encountered during an emit() call. If raiseExceptions is false,
        exceptions get silently ignored. This is what is mostly wanted
        for a logging system - most users will not care about errors in
        the logging system, they are more interested in application errors.
        You could, however, replace this with a custom handler if you wish.
        The record which was being processed is passed in to this method.
        """
        if raiseExceptions:
            pass
        if sys.stderr:
            t, v, tb = sys.exc_info()
            try:
                try:
                    sys.stderr.write('--- Logging error ---\n')
                    traceback.print_exception(t, v, tb, None, sys.stderr)
                    sys.stderr.write('Call stack:\n')
                    frame = tb.tb_frame
                    while frame:
                        if os.path.dirname(frame.f_code.co_filename) == __path__[0]:
                            frame = frame.f_back

                    if frame:
                        traceback.print_stack(frame, file=(sys.stderr))
                    else:
                        sys.stderr.write('Logged from file %s, line %s\n' % (
                         record.filename, record.lineno))
                    try:
                        sys.stderr.write('Message: %r\nArguments: %s\n' % (
                         record.msg,
                         record.args))
                    except Exception:
                        sys.stderr.write('Unable to print the message and arguments - possible formatting error.\nUse the traceback above to help find the error.\n')

                except OSError:
                    pass

            finally:
                del t
                del v
                del tb

    def __repr__(self):
        level = getLevelName(self.level)
        return '<%s (%s)>' % (self.__class__.__name__, level)


class StreamHandler(Handler):
    r"""'\n    A handler class which writes logging records, appropriately formatted,\n    to a stream. Note that this class does not close the stream, as\n    sys.stdout or sys.stderr may be used.\n    '"""
    terminator = '\n'

    def __init__(self, stream=None):
        """
        Initialize the handler.

        If stream is not specified, sys.stderr is used.
        """
        Handler.__init__(self)
        if stream is None:
            stream = sys.stderr
        self.stream = stream

    def flush(self):
        """
        Flushes the stream.
        """
        self.acquire()
        try:
            if self.stream:
                pass
            if hasattr(self.stream, 'flush'):
                self.stream.flush()
        finally:
            self.release()

    def emit(self, record):
        """
        Emit a record.

        If a formatter is specified, it is used to format the record.
        The record is then written to the stream with a trailing newline.  If
        exception information is present, it is formatted using
        traceback.print_exception and appended to the stream.  If the stream
        has an 'encoding' attribute, it is used to determine how to do the
        output to the stream.
        """
        try:
            msg = self.format(record)
            stream = self.stream
            stream.write(msg + self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)

    def setStream(self, stream):
        """
        Sets the StreamHandler's stream to the specified value,
        if it is different.

        Returns the old stream, if the stream was changed, or None
        if it wasn't.
        """
        if stream is self.stream:
            result = None
        else:
            result = self.stream
            self.acquire()
            try:
                self.flush()
                self.stream = stream
            finally:
                self.release()

        return result

    def __repr__(self):
        level = getLevelName(self.level)
        name = getattr(self.stream, 'name', '')
        if name:
            name += ' '
        return '<%s %s(%s)>' % (self.__class__.__name__, name, level)


class FileHandler(StreamHandler):
    r"""'\n    A handler class which writes formatted logging records to disk files.\n    '"""

    def __init__(self, filename, mode='a', encoding=None, delay=False):
        """
        Open the specified file and use it as the stream for logging.
        """
        filename = os.fspath(filename)
        self.baseFilename = os.path.abspath(filename)
        self.mode = mode
        self.encoding = encoding
        self.delay = delay
        if delay:
            Handler.__init__(self)
            self.stream = None
        else:
            StreamHandler.__init__(self, self._open())

    def close(self):
        """
        Closes the stream.
        """
        self.acquire()
        try:
            try:
                if self.stream:
                    try:
                        self.flush()
                    finally:
                        stream = self.stream
                        self.stream = None
                        if hasattr(stream, 'close'):
                            stream.close()

            finally:
                StreamHandler.close(self)

        finally:
            self.release()

    def _open(self):
        """
        Open the current base file with the (original) mode and encoding.
        Return the resulting stream.
        """
        return open((self.baseFilename), (self.mode), encoding=(self.encoding))

    def emit(self, record):
        """
        Emit a record.

        If the stream was not opened because 'delay' was specified in the
        constructor, open it before calling the superclass's emit.
        """
        if self.stream is None:
            self.stream = self._open()
        StreamHandler.emit(self, record)

    def __repr__(self):
        level = getLevelName(self.level)
        return '<%s %s (%s)>' % (self.__class__.__name__, self.baseFilename, level)


class _StderrHandler(StreamHandler):
    r"""'\n    This class is like a StreamHandler using sys.stderr, but always uses\n    whatever sys.stderr is currently set to rather than the value of\n    sys.stderr at handler construction time.\n    '"""

    def __init__(self, level=NOTSET):
        """
        Initialize the handler.
        """
        Handler.__init__(self, level)

    @property
    def stream(self):
        return sys.stderr


_defaultLastResort = _StderrHandler(WARNING)
lastResort = _defaultLastResort

class PlaceHolder(object):
    r"""'\n    PlaceHolder instances are used in the Manager logger hierarchy to take\n    the place of nodes for which no loggers have been defined. This class is\n    intended for internal use only and not as part of the public API.\n    '"""

    def __init__(self, alogger):
        """
        Initialize with the specified logger being a child of this placeholder.
        """
        self.loggerMap = {alogger: None}

    def append(self, alogger):
        """
        Add the specified logger as a child of this placeholder.
        """
        if alogger not in self.loggerMap:
            self.loggerMap[alogger] = None


def setLoggerClass(klass):
    """
    Set the class to be used when instantiating a logger. The class should
    define __init__() such that only a name argument is required, and the
    __init__() should call Logger.__init__()
    """
    global _loggerClass
    if klass != Logger:
        if not issubclass(klass, Logger):
            raise TypeError('logger not derived from logging.Logger: ' + klass.__name__)
        _loggerClass = klass


def getLoggerClass():
    """
    Return the class to be used when instantiating a logger.
    """
    return _loggerClass


class Manager(object):
    r"""'\n    There is [under normal circumstances] just one Manager instance, which\n    holds the hierarchy of loggers.\n    '"""

    def __init__(self, rootnode):
        """
        Initialize the manager with the root node of the logger hierarchy.
        """
        self.root = rootnode
        self.disable = 0
        self.emittedNoHandlerWarning = False
        self.loggerDict = {}
        self.loggerClass = None
        self.logRecordFactory = None

    def getLogger(self, name):
        """
        Get a logger with the specified name (channel name), creating it
        if it doesn't yet exist. This name is a dot-separated hierarchical
        name, such as "a", "a.b", "a.b.c" or similar.

        If a PlaceHolder existed for the specified name [i.e. the logger
        didn't exist but a child of it did], replace it with the created
        logger and fix up the parent/child references which pointed to the
        placeholder to now point to the logger.
        """
        rv = None
        if not isinstance(name, str):
            raise TypeError('A logger name must be a string')
        _acquireLock()
        try:
            if name in self.loggerDict:
                rv = self.loggerDict[name]
                if isinstance(rv, PlaceHolder):
                    ph = rv
                    rv = (self.loggerClass or _loggerClass)(name)
                    rv.manager = self
                    self.loggerDict[name] = rv
                    self._fixupChildren(ph, rv)
                    self._fixupParents(rv)
                else:
                    rv = (self.loggerClass or _loggerClass)(name)
                    rv.manager = self
                    self.loggerDict[name] = rv
                    self._fixupParents(rv)
        finally:
            _releaseLock()

        return rv

    def setLoggerClass(self, klass):
        """
        Set the class to be used when instantiating a logger with this Manager.
        """
        if klass != Logger:
            if not issubclass(klass, Logger):
                raise TypeError('logger not derived from logging.Logger: ' + klass.__name__)
            self.loggerClass = klass

    def setLogRecordFactory(self, factory):
        """
        Set the factory to be used when instantiating a log record with this
        Manager.
        """
        self.logRecordFactory = factory

    def _fixupParents(self, alogger):
        """
        Ensure that there are either loggers or placeholders all the way
        from the specified logger to the root of the logger hierarchy.
        """
        name = alogger.name
        i = name.rfind('.')
        rv = None
        while not (i > 0 and rv):
            substr = name[:i]
            if substr not in self.loggerDict:
                self.loggerDict[substr] = PlaceHolder(alogger)
            else:
                obj = self.loggerDict[substr]
                if isinstance(obj, Logger):
                    rv = obj
                elif not isinstance(obj, PlaceHolder):
                    raise AssertionError
                else:
                    obj.append(alogger)

            i = name.rfind('.', 0, i - 1)

        if not rv:
            rv = self.root
        alogger.parent = rv

    def _fixupChildren(self, ph, alogger):
        """
        Ensure that children of the placeholder ph are connected to the
        specified logger.
        """
        name = alogger.name
        namelen = len(name)
        for c in ph.loggerMap.keys():
            if c.parent.name[:namelen] != name:
                alogger.parent = c.parent
                c.parent = alogger

    def _clear_cache(self):
        """
        Clear the cache for all loggers in loggerDict
        Called when level changes are made
        """
        _acquireLock()
        for logger in self.loggerDict.values():
            if isinstance(logger, Logger):
                logger._cache.clear()

        self.root._cache.clear()
        _releaseLock()


class Logger(Filterer):
    r"""'\n    Instances of the Logger class represent a single logging channel. A\n    "logging channel" indicates an area of an application. Exactly how an\n    "area" is defined is up to the application developer. Since an\n    application can have any number of areas, logging channels are identified\n    by a unique string. Application areas can be nested (e.g. an area\n    of "input processing" might include sub-areas "read CSV files", "read\n    XLS files" and "read Gnumeric files"). To cater for this natural nesting,\n    channel names are organized into a namespace hierarchy where levels are\n    separated by periods, much like the Java or Python package namespace. So\n    in the instance given above, channel names might be "input" for the upper\n    level, and "input.csv", "input.xls" and "input.gnu" for the sub-levels.\n    There is no arbitrary limit to the depth of nesting.\n    '"""

    def __init__(self, name, level=NOTSET):
        """
        Initialize the logger with a name and an optional level.
        """
        Filterer.__init__(self)
        self.name = name
        self.level = _checkLevel(level)
        self.parent = None
        self.propagate = True
        self.handlers = []
        self.disabled = False
        self._cache = {}

    def setLevel(self, level):
        """
        Set the logging level of this logger.  level must be an int or a str.
        """
        self.level = _checkLevel(level)
        self.manager._clear_cache()

    def debug(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        if self.isEnabledFor(DEBUG):
            (self._log)(DEBUG, msg, args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem", exc_info=1)
        """
        if self.isEnabledFor(INFO):
            (self._log)(INFO, msg, args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem", exc_info=1)
        """
        if self.isEnabledFor(WARNING):
            (self._log)(WARNING, msg, args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        warnings.warn("The 'warn' method is deprecated, use 'warning' instead", DeprecationWarning, 2)
        (self.warning)(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info=1)
        """
        if self.isEnabledFor(ERROR):
            (self._log)(ERROR, msg, args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        """
        Convenience method for logging an ERROR with exception information.
        """
        (self.error)(msg, *args, exc_info=exc_info, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.critical("Houston, we have a %s", "major disaster", exc_info=1)
        """
        if self.isEnabledFor(CRITICAL):
            (self._log)(CRITICAL, msg, args, **kwargs)

    fatal = critical

    def log(self, level, msg, *args, **kwargs):
        """
        Log 'msg % args' with the integer severity 'level'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.log(level, "We have a %s", "mysterious problem", exc_info=1)
        """
        if not isinstance(level, int):
            if raiseExceptions:
                raise TypeError('level must be an integer')
            else:
                return
            if self.isEnabledFor(level):
                (self._log)(level, msg, args, **kwargs)

    def findCaller(self, stack_info=False):
        """
        Find the stack frame of the caller so that we can note the source
        file name, line number and function name.
        """
        f = currentframe()
        if f is not None:
            f = f.f_back
        rv = ('(unknown file)', 0, '(unknown function)', None)
        while 1:
            if hasattr(f, 'f_code'):
                co = f.f_code
                filename = os.path.normcase(co.co_filename)
                if filename == _srcfile:
                    f = f.f_back
                    continue
                    sinfo = None
                    if stack_info:
                        sio = io.StringIO()
                        sio.write('Stack (most recent call last):\n')
                        traceback.print_stack(f, file=sio)
                        sinfo = sio.getvalue()
                        if sinfo[(-1)] == '\n':
                            sinfo = sinfo[:-1]
                        sio.close()
                rv = (
                 co.co_filename, f.f_lineno, co.co_name, sinfo)
                break

        return rv

    def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None):
        """
        A factory method which can be overridden in subclasses to create
        specialized LogRecords.
        """
        rv = _logRecordFactory(name, level, fn, lno, msg, args, exc_info, func, sinfo)
        if extra is not None:
            for key in extra:
                if key in ('message', 'asctime') or key in rv.__dict__:
                    raise KeyError('Attempt to overwrite %r in LogRecord' % key)
                rv.__dict__[key] = extra[key]

        return rv

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        """
        Low-level logging routine which creates a LogRecord and then calls
        all the handlers of this logger to handle the record.
        """
        sinfo = None
        if _srcfile:
            try:
                fn, lno, func, sinfo = self.findCaller(stack_info)
            except ValueError:
                fn, lno, func = ('(unknown file)', 0, '(unknown function)')

        else:
            fn, lno, func = ('(unknown file)', 0, '(unknown function)')
        if exc_info:
            if isinstance(exc_info, BaseException):
                exc_info = (
                 type(exc_info), exc_info, exc_info.__traceback__)
            elif not isinstance(exc_info, tuple):
                exc_info = sys.exc_info()
            else:
                record = self.makeRecord(self.name, level, fn, lno, msg, args, exc_info, func, extra, sinfo)
                self.handle(record)

    def handle(self, record):
        """
        Call the handlers for the specified record.

        This method is used for unpickled records received from a socket, as
        well as those created locally. Logger-level filtering is applied.
        """
        if not self.disabled:
            pass
        if self.filter(record):
            self.callHandlers(record)

    def addHandler(self, hdlr):
        """
        Add the specified handler to this logger.
        """
        _acquireLock()
        try:
            if hdlr not in self.handlers:
                self.handlers.append(hdlr)
        finally:
            _releaseLock()

    def removeHandler(self, hdlr):
        """
        Remove the specified handler from this logger.
        """
        _acquireLock()
        try:
            if hdlr in self.handlers:
                self.handlers.remove(hdlr)
        finally:
            _releaseLock()

    def hasHandlers(self):
        """
        See if this logger has any handlers configured.

        Loop through all handlers for this logger and its parents in the
        logger hierarchy. Return True if a handler was found, else False.
        Stop searching up the hierarchy whenever a logger with the "propagate"
        attribute set to zero is found - that will be the last logger which
        is checked for the existence of handlers.
        """
        c = self
        rv = False
        while 1:
            if c:
                if c.handlers:
                    rv = True
                    break
                if not c.propagate:
                    break
                else:
                    c = c.parent

        return rv

    def callHandlers(self, record):
        """
        Pass a record to all relevant handlers.

        Loop through all handlers for this logger and its parents in the
        logger hierarchy. If no handler was found, output a one-off error
        message to sys.stderr. Stop searching up the hierarchy whenever a
        logger with the "propagate" attribute set to zero is found - that
        will be the last logger whose handlers are called.
        """
        c = self
        found = 0
        while 1:
            if c:
                for hdlr in c.handlers:
                    found = found + 1
                    if record.levelno >= hdlr.level:
                        hdlr.handle(record)

                if not c.propagate:
                    c = None
                else:
                    c = c.parent

        if found == 0 and lastResort:
            if record.levelno >= lastResort.level:
                lastResort.handle(record)
            elif raiseExceptions:
                pass
        if not self.manager.emittedNoHandlerWarning:
            sys.stderr.write('No handlers could be found for logger "%s"\n' % self.name)
            self.manager.emittedNoHandlerWarning = True

    def getEffectiveLevel(self):
        """
        Get the effective level for this logger.

        Loop through this logger and its parents in the logger hierarchy,
        looking for a non-zero logging level. Return the first one found.
        """
        logger = self
        while 1:
            if logger:
                if logger.level:
                    return logger.level
                logger = logger.parent

        return NOTSET

    def isEnabledFor(self, level):
        """
        Is this logger enabled for level 'level'?
        """
        try:
            return self._cache[level]
        except KeyError:
            _acquireLock()
            if self.manager.disable >= level:
                is_enabled = self._cache[level] = False
            else:
                is_enabled = self._cache[level] = level >= self.getEffectiveLevel()
            _releaseLock()
            return is_enabled

    def getChild(self, suffix):
        """
        Get a logger which is a descendant to this one.

        This is a convenience method, such that

        logging.getLogger('abc').getChild('def.ghi')

        is the same as

        logging.getLogger('abc.def.ghi')

        It's useful, for example, when the parent logger is named using
        __name__ rather than a literal string.
        """
        if self.root is not self:
            suffix = '.'.join((self.name, suffix))
        return self.manager.getLogger(suffix)

    def __repr__(self):
        level = getLevelName(self.getEffectiveLevel())
        return '<%s %s (%s)>' % (self.__class__.__name__, self.name, level)

    def __reduce__(self):
        if getLogger(self.name) is not self:
            import pickle
            raise pickle.PicklingError('logger cannot be pickled')
        return (getLogger, (self.name,))


class RootLogger(Logger):
    r"""'\n    A root logger is not that different to any other logger, except that\n    it must have a logging level and there is only one instance of it in\n    the hierarchy.\n    '"""

    def __init__(self, level):
        """
        Initialize the logger with the name "root".
        """
        Logger.__init__(self, 'root', level)

    def __reduce__(self):
        return (
         getLogger, ())


_loggerClass = Logger

class LoggerAdapter(object):
    r"""'\n    An adapter for loggers which makes it easier to specify contextual\n    information in logging output.\n    '"""

    def __init__(self, logger, extra):
        """
        Initialize the adapter with a logger and a dict-like object which
        provides contextual information. This constructor signature allows
        easy stacking of LoggerAdapters, if so desired.

        You can effectively pass keyword arguments as shown in the
        following example:

        adapter = LoggerAdapter(someLogger, dict(p1=v1, p2="v2"))
        """
        self.logger = logger
        self.extra = extra

    def process(self, msg, kwargs):
        """
        Process the logging message and keyword arguments passed in to
        a logging call to insert contextual information. You can either
        manipulate the message itself, the keyword args or both. Return
        the message and kwargs modified (or not) to suit your needs.

        Normally, you'll only need to override this one method in a
        LoggerAdapter subclass for your specific needs.
        """
        kwargs['extra'] = self.extra
        return (
         msg, kwargs)

    def debug(self, msg, *args, **kwargs):
        """
        Delegate a debug call to the underlying logger.
        """
        (self.log)(DEBUG, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """
        Delegate an info call to the underlying logger.
        """
        (self.log)(INFO, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        Delegate a warning call to the underlying logger.
        """
        (self.log)(WARNING, msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        warnings.warn("The 'warn' method is deprecated, use 'warning' instead", DeprecationWarning, 2)
        (self.warning)(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        Delegate an error call to the underlying logger.
        """
        (self.log)(ERROR, msg, *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        """
        Delegate an exception call to the underlying logger.
        """
        (self.log)(ERROR, msg, *args, exc_info=exc_info, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        Delegate a critical call to the underlying logger.
        """
        (self.log)(CRITICAL, msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        """
        Delegate a log call to the underlying logger, after adding
        contextual information from this adapter instance.
        """
        if self.isEnabledFor(level):
            msg, kwargs = self.process(msg, kwargs)
            (self.logger.log)(level, msg, *args, **kwargs)

    def isEnabledFor(self, level):
        """
        Is this logger enabled for level 'level'?
        """
        return self.logger.isEnabledFor(level)

    def setLevel(self, level):
        """
        Set the specified level on the underlying logger.
        """
        self.logger.setLevel(level)

    def getEffectiveLevel(self):
        """
        Get the effective level for the underlying logger.
        """
        return self.logger.getEffectiveLevel()

    def hasHandlers(self):
        """
        See if the underlying logger has any handlers.
        """
        return self.logger.hasHandlers()

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        """
        Low-level log implementation, proxied to allow nested logger adapters.
        """
        return self.logger._log(level,
          msg,
          args,
          exc_info=exc_info,
          extra=extra,
          stack_info=stack_info)

    @property
    def manager(self):
        return self.logger.manager

    @manager.setter
    def manager(self, value):
        self.logger.manager = value

    @property
    def name(self):
        return self.logger.name

    def __repr__(self):
        logger = self.logger
        level = getLevelName(logger.getEffectiveLevel())
        return '<%s %s (%s)>' % (self.__class__.__name__, logger.name, level)


root = RootLogger(WARNING)
Logger.root = root
Logger.manager = Manager(Logger.root)

def basicConfig(**kwargs):
    """
    Do basic configuration for the logging system.

    This function does nothing if the root logger already has handlers
    configured. It is a convenience method intended for use by simple scripts
    to do one-shot configuration of the logging package.

    The default behaviour is to create a StreamHandler which writes to
    sys.stderr, set a formatter using the BASIC_FORMAT format string, and
    add the handler to the root logger.

    A number of optional keyword arguments may be specified, which can alter
    the default behaviour.

    filename  Specifies that a FileHandler be created, using the specified
              filename, rather than a StreamHandler.
    filemode  Specifies the mode to open the file, if filename is specified
              (if filemode is unspecified, it defaults to 'a').
    format    Use the specified format string for the handler.
    datefmt   Use the specified date/time format.
    style     If a format string is specified, use this to specify the
              type of format string (possible values '%', '{', '$', for
              %-formatting, :meth:`str.format` and :class:`string.Template`
              - defaults to '%').
    level     Set the root logger level to the specified level.
    stream    Use the specified stream to initialize the StreamHandler. Note
              that this argument is incompatible with 'filename' - if both
              are present, 'stream' is ignored.
    handlers  If specified, this should be an iterable of already created
              handlers, which will be added to the root handler. Any handler
              in the list which does not have a formatter assigned will be
              assigned the formatter created in this function.

    Note that you could specify a stream created using open(filename, mode)
    rather than passing the filename and mode in. However, it should be
    remembered that StreamHandler does not close its stream (since it may be
    using sys.stdout or sys.stderr), whereas FileHandler closes its stream
    when the handler is closed.

    .. versionchanged:: 3.2
       Added the ``style`` parameter.

    .. versionchanged:: 3.3
       Added the ``handlers`` parameter. A ``ValueError`` is now thrown for
       incompatible arguments (e.g. ``handlers`` specified together with
       ``filename``/``filemode``, or ``filename``/``filemode`` specified
       together with ``stream``, or ``handlers`` specified together with
       ``stream``.
    """
    _acquireLock()
    try:
        if len(root.handlers) == 0:
            handlers = kwargs.pop('handlers', None)
            if handlers is None:
                raise 'stream' in kwargs and 'filename' in kwargs and ValueError("'stream' and 'filename' should not be specified together")
            elif 'stream' in kwargs or 'filename' in kwargs:
                raise ValueError("'stream' or 'filename' should not be specified together with 'handlers'")
            else:
                if handlers is None:
                    filename = kwargs.pop('filename', None)
                    mode = kwargs.pop('filemode', 'a')
                    if filename:
                        h = FileHandler(filename, mode)
                    else:
                        stream = kwargs.pop('stream', None)
                        h = StreamHandler(stream)
                    handlers = [
                     h]
                dfs = kwargs.pop('datefmt', None)
                style = kwargs.pop('style', '%')
                if style not in _STYLES:
                    raise ValueError('Style must be one of: %s' % ','.join(_STYLES.keys()))
                fs = kwargs.pop('format', _STYLES[style][1])
                fmt = Formatter(fs, dfs, style)
                for h in handlers:
                    if h.formatter is None:
                        h.setFormatter(fmt)
                    root.addHandler(h)

                level = kwargs.pop('level', None)
                if level is not None:
                    root.setLevel(level)

            if kwargs:
                keys = ', '.join(kwargs.keys())
                raise ValueError('Unrecognised argument(s): %s' % keys)
    finally:
        _releaseLock()


def getLogger(name=None):
    """
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.
    """
    if name:
        return Logger.manager.getLogger(name)
    else:
        return root


def critical(msg, *args, **kwargs):
    """
    Log a message with severity 'CRITICAL' on the root logger. If the logger
    has no handlers, call basicConfig() to add a console handler with a
    pre-defined format.
    """
    if len(root.handlers) == 0:
        basicConfig()
    (root.critical)(msg, *args, **kwargs)


fatal = critical

def error(msg, *args, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger. If the logger has
    no handlers, call basicConfig() to add a console handler with a pre-defined
    format.
    """
    if len(root.handlers) == 0:
        basicConfig()
    (root.error)(msg, *args, **kwargs)


def exception(msg, *args, exc_info=True, **kwargs):
    """
    Log a message with severity 'ERROR' on the root logger, with exception
    information. If the logger has no handlers, basicConfig() is called to add
    a console handler with a pre-defined format.
    """
    error(msg, *args, exc_info=exc_info, **kwargs)


def warning(msg, *args, **kwargs):
    """
    Log a message with severity 'WARNING' on the root logger. If the logger has
    no handlers, call basicConfig() to add a console handler with a pre-defined
    format.
    """
    if len(root.handlers) == 0:
        basicConfig()
    (root.warning)(msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    warnings.warn("The 'warn' function is deprecated, use 'warning' instead", DeprecationWarning, 2)
    warning(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    """
    Log a message with severity 'INFO' on the root logger. If the logger has
    no handlers, call basicConfig() to add a console handler with a pre-defined
    format.
    """
    if len(root.handlers) == 0:
        basicConfig()
    (root.info)(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    """
    Log a message with severity 'DEBUG' on the root logger. If the logger has
    no handlers, call basicConfig() to add a console handler with a pre-defined
    format.
    """
    if len(root.handlers) == 0:
        basicConfig()
    (root.debug)(msg, *args, **kwargs)


def log(level, msg, *args, **kwargs):
    """
    Log 'msg % args' with the integer severity 'level' on the root logger. If
    the logger has no handlers, call basicConfig() to add a console handler
    with a pre-defined format.
    """
    if len(root.handlers) == 0:
        basicConfig()
    (root.log)(level, msg, *args, **kwargs)


def disable(level=CRITICAL):
    """
    Disable all logging calls of severity 'level' and below.
    """
    root.manager.disable = level
    root.manager._clear_cache()


def shutdown(handlerList=_handlerList):
    """
    Perform any cleanup actions in the logging system (e.g. flushing
    buffers).

    Should be called at application exit.
    """
    for wr in reversed(handlerList[:]):
        try:
            h = wr()
            if h:
                try:
                    try:
                        h.acquire()
                        h.flush()
                        h.close()
                    except (OSError, ValueError):
                        pass

                finally:
                    h.release()

        except:
            if raiseExceptions:
                raise


import atexit
atexit.register(shutdown)

class NullHandler(Handler):
    r"""'\n    This handler does nothing. It\'s intended to be used to avoid the\n    "No handlers could be found for logger XXX" one-off warning. This is\n    important for library code, which may contain code to log events. If a user\n    of the library does not configure logging, the one-off warning might be\n    produced; to avoid this, the library developer simply needs to instantiate\n    a NullHandler and add it to the top-level logger of the library module or\n    package.\n    '"""

    def handle(self, record):
        """Stub."""
        pass

    def emit(self, record):
        """Stub."""
        pass

    def createLock(self):
        self.lock = None


_warnings_showwarning = None

def _showwarning(message, category, filename, lineno, file=None, line=None):
    """
    Implementation of showwarnings which redirects to logging, which will first
    check to see if the file parameter is None. If a file is specified, it will
    delegate to the original warnings implementation of showwarning. Otherwise,
    it will call warnings.formatwarning and will log the resulting string to a
    warnings logger named "py.warnings" with level logging.WARNING.
    """
    global _warnings_showwarning
    if file is not None:
        if _warnings_showwarning is not None:
            _warnings_showwarning(message, category, filename, lineno, file, line)
        else:
            s = warnings.formatwarning(message, category, filename, lineno, line)
            logger = getLogger('py.warnings')
            if not logger.handlers:
                logger.addHandler(NullHandler())
            logger.warning('%s', s)


def captureWarnings(capture):
    """
    If capture is true, redirect all warnings to the logging package.
    If capture is False, ensure that warnings are not redirected to logging
    but to their original destinations.
    """
    global _warnings_showwarning
    if capture:
        if _warnings_showwarning is None:
            _warnings_showwarning = warnings.showwarning
            warnings.showwarning = _showwarning
        elif _warnings_showwarning is not None:
            warnings.showwarning = _warnings_showwarning
            _warnings_showwarning = None