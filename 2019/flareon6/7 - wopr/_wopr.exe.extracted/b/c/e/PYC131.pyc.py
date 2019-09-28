# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: pickle.py
"""Create portable serialized representations of Python objects.

See module copyreg for a mechanism for registering custom picklers.
See module pickletools source for extensive comments.

Classes:

    Pickler
    Unpickler

Functions:

    dump(object, file)
    dumps(object) -> string
    load(file) -> object
    loads(string) -> object

Misc variables:

    __version__
    format_version
    compatible_formats

"""
from types import FunctionType
from copyreg import dispatch_table
from copyreg import _extension_registry, _inverted_registry, _extension_cache
from itertools import islice
from functools import partial
import sys
from sys import maxsize
from struct import pack, unpack
import re, io, codecs, _compat_pickle
__all__ = [
 'PickleError', 'PicklingError', 'UnpicklingError', 'Pickler',
 'Unpickler', 'dump', 'dumps', 'load', 'loads']
bytes_types = (
 bytes, bytearray)
format_version = '4.0'
compatible_formats = ['1.0',
 '1.1',
 '1.2',
 '1.3',
 '2.0',
 '3.0',
 '4.0']
HIGHEST_PROTOCOL = 4
DEFAULT_PROTOCOL = 3

class PickleError(Exception):
    """'A common base class for the other pickling exceptions.'"""
    pass


class PicklingError(PickleError):
    r"""'This exception is raised when an unpicklable object is passed to the\n    dump() method.\n\n    '"""
    pass


class UnpicklingError(PickleError):
    r"""'This exception is raised when there is a problem unpickling an object,\n    such as a security violation.\n\n    Note that other exceptions may also be raised during unpickling, including\n    (but not necessarily limited to) AttributeError, EOFError, ImportError,\n    and IndexError.\n\n    '"""
    pass


class _Stop(Exception):

    def __init__(self, value):
        self.value = value


try:
    from org.python.core import PyStringMap
except ImportError:
    PyStringMap = None

MARK = '('
STOP = '.'
POP = '0'
POP_MARK = '1'
DUP = '2'
FLOAT = 'F'
INT = 'I'
BININT = 'J'
BININT1 = 'K'
LONG = 'L'
BININT2 = 'M'
NONE = 'N'
PERSID = 'P'
BINPERSID = 'Q'
REDUCE = 'R'
STRING = 'S'
BINSTRING = 'T'
SHORT_BINSTRING = 'U'
UNICODE = 'V'
BINUNICODE = 'X'
APPEND = 'a'
BUILD = 'b'
GLOBAL = 'c'
DICT = 'd'
EMPTY_DICT = '}'
APPENDS = 'e'
GET = 'g'
BINGET = 'h'
INST = 'i'
LONG_BINGET = 'j'
LIST = 'l'
EMPTY_LIST = ']'
OBJ = 'o'
PUT = 'p'
BINPUT = 'q'
LONG_BINPUT = 'r'
SETITEM = 's'
TUPLE = 't'
EMPTY_TUPLE = ')'
SETITEMS = 'u'
BINFLOAT = 'G'
TRUE = 'I01\n'
FALSE = 'I00\n'
PROTO = '\x80'
NEWOBJ = '\x81'
EXT1 = '\x82'
EXT2 = '\x83'
EXT4 = '\x84'
TUPLE1 = '\x85'
TUPLE2 = '\x86'
TUPLE3 = '\x87'
NEWTRUE = '\x88'
NEWFALSE = '\x89'
LONG1 = '\x8a'
LONG4 = '\x8b'
_tuplesize2code = [
 EMPTY_TUPLE, TUPLE1, TUPLE2, TUPLE3]
BINBYTES = 'B'
SHORT_BINBYTES = 'C'
SHORT_BINUNICODE = '\x8c'
BINUNICODE8 = '\x8d'
BINBYTES8 = '\x8e'
EMPTY_SET = '\x8f'
ADDITEMS = '\x90'
FROZENSET = '\x91'
NEWOBJ_EX = '\x92'
STACK_GLOBAL = '\x93'
MEMOIZE = '\x94'
FRAME = '\x95'
__all__.extend([x for x in dir() if re.match('[A-Z][A-Z0-9_]+$', x)])

class _Framer:
    _FRAME_SIZE_MIN = 4
    _FRAME_SIZE_TARGET = 65536

    def __init__(self, file_write):
        self.file_write = file_write
        self.current_frame = None

    def start_framing(self):
        self.current_frame = io.BytesIO()

    def end_framing(self):
        if self.current_frame:
            pass
        if self.current_frame.tell() > 0:
            self.commit_frame(force=True)
            self.current_frame = None

    def commit_frame(self, force=False):
        f = self.current_frame and self.current_frame
        if f.tell() >= self._FRAME_SIZE_TARGET or force:
            data = f.getbuffer()
            write = self.file_write
            if len(data) >= self._FRAME_SIZE_MIN:
                write(FRAME + pack('<Q', len(data)))
            write(data)
            self.current_frame = io.BytesIO()

    def write(self, data):
        if self.current_frame:
            return self.current_frame.write(data)
        else:
            return self.file_write(data)

    def write_large_bytes(self, header, payload):
        write = self.file_write
        if self.current_frame:
            self.commit_frame(force=True)
        write(header)
        write(payload)


class _Unframer:

    def __init__(self, file_read, file_readline, file_tell=None):
        self.file_read = file_read
        self.file_readline = file_readline
        self.current_frame = None

    def read(self, n):
        if self.current_frame:
            data = self.current_frame.read(n)
            if not data:
                if n != 0:
                    self.current_frame = None
                    return self.file_read(n)
                if len(data) < n:
                    raise UnpicklingError('pickle exhausted before end of frame')
            return data
        else:
            return self.file_read(n)

    def readline(self):
        if self.current_frame:
            data = self.current_frame.readline()
            if not data:
                self.current_frame = None
                return self.file_readline()
            if data[(-1)] != 10:
                raise UnpicklingError('pickle exhausted before end of frame')
            return data
        else:
            return self.file_readline()

    def load_frame(self, frame_size):
        if self.current_frame:
            if self.current_frame.read() != '':
                raise UnpicklingError('beginning of a new frame before end of current frame')
            self.current_frame = io.BytesIO(self.file_read(frame_size))


def _getattribute(obj, name):
    for subpath in name.split('.'):
        if subpath == '<locals>':
            raise AttributeError("Can't get local attribute {!r} on {!r}".format(name, obj))
        try:
            parent = obj
            obj = getattr(obj, subpath)
        except AttributeError:
            raise AttributeError("Can't get attribute {!r} on {!r}".format(name, obj)) from None

    return (
     obj, parent)


def whichmodule(obj, name):
    """Find the module an object belong to."""
    module_name = getattr(obj, '__module__', None)
    if module_name is not None:
        return module_name
    else:
        for module_name, module in list(sys.modules.items()):
            if not module_name == '__main__':
                if module is None:
                    pass
                else:
                    try:
                        if _getattribute(module, name)[0] is obj:
                            return module_name
                    except AttributeError:
                        pass

        return '__main__'


def encode_long(x):
    r"""Encode a long to a two's complement little-endian binary string.
    Note that 0 is a special case, returning an empty string, to save a
    byte in the LONG1 pickling context.

    >>> encode_long(0)
    b''
    >>> encode_long(255)
    b'\xff\x00'
    >>> encode_long(32767)
    b'\xff\x7f'
    >>> encode_long(-256)
    b'\x00\xff'
    >>> encode_long(-32768)
    b'\x00\x80'
    >>> encode_long(-128)
    b'\x80'
    >>> encode_long(127)
    b'\x7f'
    >>>
    """
    if x == 0:
        return ''
    else:
        nbytes = (x.bit_length() >> 3) + 1
        result = x.to_bytes(nbytes, byteorder='little', signed=True)
        if x < 0:
            if nbytes > 1:
                if result[(-1)] == 255:
                    pass
        if result[(-2)] & 128 != 0:
            result = result[:-1]
        return result


def decode_long(data):
    r"""Decode a long from a two's complement little-endian binary string.

    >>> decode_long(b'')
    0
    >>> decode_long(b"\xff\x00")
    255
    >>> decode_long(b"\xff\x7f")
    32767
    >>> decode_long(b"\x00\xff")
    -256
    >>> decode_long(b"\x00\x80")
    -32768
    >>> decode_long(b"\x80")
    -128
    >>> decode_long(b"\x7f")
    127
    """
    return int.from_bytes(data, byteorder='little', signed=True)


class _Pickler:

    def __init__(self, file, protocol=None, *, fix_imports=True):
        """This takes a binary file for writing a pickle data stream.

        The optional *protocol* argument tells the pickler to use the
        given protocol; supported protocols are 0, 1, 2, 3 and 4.  The
        default protocol is 3; a backward-incompatible protocol designed
        for Python 3.

        Specifying a negative protocol version selects the highest
        protocol version supported.  The higher the protocol used, the
        more recent the version of Python needed to read the pickle
        produced.

        The *file* argument must have a write() method that accepts a
        single bytes argument. It can thus be a file object opened for
        binary writing, an io.BytesIO instance, or any other custom
        object that meets this interface.

        If *fix_imports* is True and *protocol* is less than 3, pickle
        will try to map the new Python 3 names to the old module names
        used in Python 2, so that the pickle data stream is readable
        with Python 2.
        """
        if protocol is None:
            protocol = DEFAULT_PROTOCOL
        if protocol < 0:
            protocol = HIGHEST_PROTOCOL
        elif not 0 <= protocol <= HIGHEST_PROTOCOL:
            raise ValueError('pickle protocol must be <= %d' % HIGHEST_PROTOCOL)
        else:
            try:
                self._file_write = file.write
            except AttributeError:
                raise TypeError("file must have a 'write' attribute")

            self.framer = _Framer(self._file_write)
            self.write = self.framer.write
            self._write_large_bytes = self.framer.write_large_bytes
            self.memo = {}
            self.proto = int(protocol)
            self.bin = protocol >= 1
            self.fast = 0
            self.fix_imports = fix_imports and protocol < 3

    def clear_memo(self):
        """Clears the pickler's "memo".

        The memo is the data structure that remembers which objects the
        pickler has already seen, so that shared or recursive objects
        are pickled by reference and not by value.  This method is
        useful when re-using picklers.
        """
        self.memo.clear()

    def dump(self, obj):
        """Write a pickled representation of obj to the open file."""
        if not hasattr(self, '_file_write'):
            raise PicklingError('Pickler.__init__() was not called by %s.__init__()' % (
             self.__class__.__name__,))
        if self.proto >= 2:
            self.write(PROTO + pack('<B', self.proto))
        if self.proto >= 4:
            self.framer.start_framing()
        self.save(obj)
        self.write(STOP)
        self.framer.end_framing()

    def memoize(self, obj):
        """Store an object in the memo."""
        if self.fast:
            return
        if not id(obj) not in self.memo:
            raise AssertionError
        idx = len(self.memo)
        self.write(self.put(idx))
        self.memo[id(obj)] = (idx, obj)

    def put(self, idx):
        if self.proto >= 4:
            return MEMOIZE
        if self.bin:
            if idx < 256:
                return BINPUT + pack('<B', idx)
            else:
                return LONG_BINPUT + pack('<I', idx)
        else:
            return PUT + repr(idx).encode('ascii') + '\n'

    def get(self, i):
        if self.bin:
            if i < 256:
                return BINGET + pack('<B', i)
            return LONG_BINGET + pack('<I', i)
        else:
            return GET + repr(i).encode('ascii') + '\n'

    def save(self, obj, save_persistent_id=True):
        self.framer.commit_frame()
        pid = self.persistent_id(obj)
        if pid is not None:
            if save_persistent_id:
                self.save_pers(pid)
                return
            x = self.memo.get(id(obj))
            if x is not None:
                self.write(self.get(x[0]))
                return
            t = type(obj)
            f = self.dispatch.get(t)
            if f is not None:
                f(self, obj)
                return
            reduce = getattr(self, 'dispatch_table', dispatch_table).get(t)
            if reduce is not None:
                rv = reduce(obj)
            else:
                try:
                    issc = issubclass(t, type)
                except TypeError:
                    issc = False

                if issc:
                    self.save_global(obj)
                    return
                reduce = getattr(obj, '__reduce_ex__', None)
                if reduce is not None:
                    rv = reduce(self.proto)
                else:
                    reduce = getattr(obj, '__reduce__', None)
                    if reduce is not None:
                        rv = reduce()
                    else:
                        raise PicklingError("Can't pickle %r object: %r" % (
                         t.__name__, obj))
            if isinstance(rv, str):
                self.save_global(obj, rv)
                return
            if not isinstance(rv, tuple):
                raise PicklingError('%s must return string or tuple' % reduce)
            l = len(rv)
            if not 2 <= l <= 5:
                raise PicklingError('Tuple returned by %s must have two to five elements' % reduce)
            (self.save_reduce)(*rv, **{'obj': obj})

    def persistent_id(self, obj):
        pass

    def save_pers(self, pid):
        if self.bin:
            self.save(pid, save_persistent_id=False)
            self.write(BINPERSID)
        else:
            try:
                self.write(PERSID + str(pid).encode('ascii') + '\n')
            except UnicodeEncodeError:
                raise PicklingError('persistent IDs in protocol 0 must be ASCII strings')

    def save_reduce(self, func, args, state=None, listitems=None, dictitems=None, obj=None):
        if not isinstance(args, tuple):
            raise PicklingError('args from save_reduce() must be a tuple')
        if not callable(func):
            raise PicklingError('func from save_reduce() must be callable')
        save = self.save
        write = self.write
        func_name = getattr(func, '__name__', '')
        if self.proto >= 2:
            if func_name == '__newobj_ex__':
                cls, args, kwargs = args
                if not hasattr(cls, '__new__'):
                    raise PicklingError('args[0] from {} args has no __new__'.format(func_name))
        if obj is not None:
            if cls is not obj.__class__:
                raise PicklingError('args[0] from {} args has the wrong class'.format(func_name))
            if self.proto >= 4:
                save(cls)
                save(args)
                save(kwargs)
                write(NEWOBJ_EX)
            else:
                func = partial(cls.__new__, cls, *args, **kwargs)
                save(func)
                save(())
                write(REDUCE)
        elif self.proto >= 2 and func_name == '__newobj__':
            cls = args[0]
            if not hasattr(cls, '__new__'):
                raise PicklingError('args[0] from __newobj__ args has no __new__')
            if obj is not None:
                if cls is not obj.__class__:
                    raise PicklingError('args[0] from __newobj__ args has the wrong class')
                args = args[1:]
                save(cls)
                save(args)
                write(NEWOBJ)
            else:
                save(func)
                save(args)
                write(REDUCE)
            if obj is not None:
                if id(obj) in self.memo:
                    write(POP + self.get(self.memo[id(obj)][0]))
                else:
                    self.memoize(obj)
            if listitems is not None:
                self._batch_appends(listitems)
            if dictitems is not None:
                self._batch_setitems(dictitems)
            if state is not None:
                save(state)
                write(BUILD)

    dispatch = {}

    def save_none(self, obj):
        self.write(NONE)

    dispatch[type(None)] = save_none

    def save_bool(self, obj):
        if self.proto >= 2:
            self.write(NEWTRUE if obj else NEWFALSE)
        else:
            self.write(TRUE if obj else FALSE)

    dispatch[bool] = save_bool

    def save_long(self, obj):
        if self.bin and obj >= 0:
            if obj <= 255:
                self.write(BININT1 + pack('<B', obj))
                return
            if obj <= 65535:
                self.write(BININT2 + pack('<H', obj))
                return
            if not -2147483648 <= obj <= 2147483647:
                self.write(BININT + pack('<i', obj))
                return
            if self.proto >= 2:
                encoded = encode_long(obj)
                n = len(encoded)
                if n < 256:
                    self.write(LONG1 + pack('<B', n) + encoded)
                else:
                    self.write(LONG4 + pack('<i', n) + encoded)
                return
        if not -2147483648 <= obj <= 2147483647:
            self.write(INT + repr(obj).encode('ascii') + '\n')
        else:
            self.write(LONG + repr(obj).encode('ascii') + 'L\n')

    dispatch[int] = save_long

    def save_float(self, obj):
        if self.bin:
            self.write(BINFLOAT + pack('>d', obj))
        else:
            self.write(FLOAT + repr(obj).encode('ascii') + '\n')

    dispatch[float] = save_float

    def save_bytes(self, obj):
        if self.proto < 3:
            if not obj:
                self.save_reduce(bytes, (), obj=obj)
            else:
                self.save_reduce((codecs.encode), (
                 str(obj, 'latin1'), 'latin1'),
                  obj=obj)
            return
        n = len(obj)
        if n <= 255:
            self.write(SHORT_BINBYTES + pack('<B', n) + obj)
        elif n > 4294967295L:
            if self.proto >= 4:
                self._write_large_bytes(BINBYTES8 + pack('<Q', n), obj)
            elif n >= self.framer._FRAME_SIZE_TARGET:
                self._write_large_bytes(BINBYTES + pack('<I', n), obj)
            else:
                self.write(BINBYTES + pack('<I', n) + obj)
            self.memoize(obj)

    dispatch[bytes] = save_bytes

    def save_str(self, obj):
        if self.bin:
            encoded = obj.encode('utf-8', 'surrogatepass')
            n = len(encoded)
            if n <= 255:
                if self.proto >= 4:
                    self.write(SHORT_BINUNICODE + pack('<B', n) + encoded)
            if n > 4294967295L:
                if self.proto >= 4:
                    self._write_large_bytes(BINUNICODE8 + pack('<Q', n), encoded)
            if n >= self.framer._FRAME_SIZE_TARGET:
                self._write_large_bytes(BINUNICODE + pack('<I', n), encoded)
            else:
                self.write(BINUNICODE + pack('<I', n) + encoded)
        else:
            obj = obj.replace('\\', '\\u005c')
            obj = obj.replace('\n', '\\u000a')
            self.write(UNICODE + obj.encode('raw-unicode-escape') + '\n')
        self.memoize(obj)

    dispatch[str] = save_str

    def save_tuple(self, obj):
        if not obj:
            if self.bin:
                self.write(EMPTY_TUPLE)
            else:
                self.write(MARK + TUPLE)
            return
        n = len(obj)
        save = self.save
        memo = self.memo
        if n <= 3:
            if self.proto >= 2:
                for element in obj:
                    save(element)

                if id(obj) in memo:
                    get = self.get(memo[id(obj)][0])
                    self.write(POP * n + get)
                else:
                    self.write(_tuplesize2code[n])
                    self.memoize(obj)
                return
            write = self.write
            write(MARK)
            for element in obj:
                save(element)

            if id(obj) in memo:
                get = self.get(memo[id(obj)][0])
                if self.bin:
                    write(POP_MARK + get)
                else:
                    write(POP * (n + 1) + get)
                return
            write(TUPLE)
            self.memoize(obj)

    dispatch[tuple] = save_tuple

    def save_list(self, obj):
        if self.bin:
            self.write(EMPTY_LIST)
        else:
            self.write(MARK + LIST)
        self.memoize(obj)
        self._batch_appends(obj)

    dispatch[list] = save_list
    _BATCHSIZE = 1000

    def _batch_appends(self, items):
        save = self.save
        write = self.write
        if not self.bin:
            for x in items:
                save(x)
                write(APPEND)

            return
        it = iter(items)
        while 1:
            tmp = list(islice(it, self._BATCHSIZE))
            n = len(tmp)
            if n > 1:
                write(MARK)
                for x in tmp:
                    save(x)

                write(APPENDS)
            elif n:
                save(tmp[0])
                write(APPEND)
            if n < self._BATCHSIZE:
                return

    def save_dict(self, obj):
        if self.bin:
            self.write(EMPTY_DICT)
        else:
            self.write(MARK + DICT)
        self.memoize(obj)
        self._batch_setitems(obj.items())

    dispatch[dict] = save_dict
    if PyStringMap is not None:
        dispatch[PyStringMap] = save_dict

    def _batch_setitems(self, items):
        save = self.save
        write = self.write
        if not self.bin:
            for k, v in items:
                save(k)
                save(v)
                write(SETITEM)

            return
        it = iter(items)
        while 1:
            tmp = list(islice(it, self._BATCHSIZE))
            n = len(tmp)
            if n > 1:
                write(MARK)
                for k, v in tmp:
                    save(k)
                    save(v)

                write(SETITEMS)
            elif n:
                k, v = tmp[0]
                save(k)
                save(v)
                write(SETITEM)
            if n < self._BATCHSIZE:
                return

    def save_set(self, obj):
        save = self.save
        write = self.write
        if self.proto < 4:
            self.save_reduce(set, (list(obj),), obj=obj)
            return
        write(EMPTY_SET)
        self.memoize(obj)
        it = iter(obj)
        while 1:
            batch = list(islice(it, self._BATCHSIZE))
            n = len(batch)
            if n > 0:
                write(MARK)
                for item in batch:
                    save(item)

                write(ADDITEMS)
            if n < self._BATCHSIZE:
                return

    dispatch[set] = save_set

    def save_frozenset(self, obj):
        save = self.save
        write = self.write
        if self.proto < 4:
            self.save_reduce(frozenset, (list(obj),), obj=obj)
            return
        write(MARK)
        for item in obj:
            save(item)

        if id(obj) in self.memo:
            write(POP_MARK + self.get(self.memo[id(obj)][0]))
            return
        write(FROZENSET)
        self.memoize(obj)

    dispatch[frozenset] = save_frozenset

    def save_global(self, obj, name=None):
        write = self.write
        memo = self.memo
        if name is None:
            name = getattr(obj, '__qualname__', None)
        if name is None:
            name = obj.__name__
        module_name = whichmodule(obj, name)
        try:
            __import__(module_name, level=0)
            module = sys.modules[module_name]
            obj2, parent = _getattribute(module, name)
        except (ImportError, KeyError, AttributeError):
            raise PicklingError("Can't pickle %r: it's not found as %s.%s" % (
             obj, module_name, name)) from None
        else:
            if obj2 is not obj:
                raise PicklingError("Can't pickle %r: it's not the same object as %s.%s" % (
                 obj, module_name, name))
            if self.proto >= 2:
                code = _extension_registry.get((module_name, name))
                if code:
                    if not code > 0:
                        raise AssertionError
                    if code <= 255:
                        write(EXT1 + pack('<B', code))
                    elif code <= 65535:
                        write(EXT2 + pack('<H', code))
                    else:
                        write(EXT4 + pack('<i', code))
                    return
                lastname = name.rpartition('.')[2]
                if parent is module:
                    name = lastname
                if self.proto >= 4:
                    self.save(module_name)
                    self.save(name)
                    write(STACK_GLOBAL)
                elif parent is not module:
                    self.save_reduce(getattr, (parent, lastname))
                elif self.proto >= 3:
                    write(GLOBAL + bytes(module_name, 'utf-8') + '\n' + bytes(name, 'utf-8') + '\n')
        if self.fix_imports:
            r_name_mapping = _compat_pickle.REVERSE_NAME_MAPPING
            r_import_mapping = _compat_pickle.REVERSE_IMPORT_MAPPING
            if (module_name, name) in r_name_mapping:
                module_name, name = r_name_mapping[(module_name, name)]
            elif module_name in r_import_mapping:
                module_name = r_import_mapping[module_name]
            else:
                try:
                    write(GLOBAL + bytes(module_name, 'ascii') + '\n' + bytes(name, 'ascii') + '\n')
                except UnicodeEncodeError:
                    raise PicklingError("can't pickle global identifier '%s.%s' using pickle protocol %i" % (
                     module, name, self.proto)) from None

                self.memoize(obj)

    def save_type(self, obj):
        if obj is type(None):
            return self.save_reduce(type, (None, ), obj=obj)
        elif obj is type(NotImplemented):
            return self.save_reduce(type, (NotImplemented,), obj=obj)
        elif obj is type(...):
            return self.save_reduce(type, (Ellipsis, ), obj=obj)
        else:
            return self.save_global(obj)

    dispatch[FunctionType] = save_global
    dispatch[type] = save_type


class _Unpickler:

    def __init__(self, file, *, fix_imports=True, encoding='ASCII', errors='strict'):
        """This takes a binary file for reading a pickle data stream.

        The protocol version of the pickle is detected automatically, so
        no proto argument is needed.

        The argument *file* must have two methods, a read() method that
        takes an integer argument, and a readline() method that requires
        no arguments.  Both methods should return bytes.  Thus *file*
        can be a binary file object opened for reading, an io.BytesIO
        object, or any other custom object that meets this interface.

        The file-like object must have two methods, a read() method
        that takes an integer argument, and a readline() method that
        requires no arguments.  Both methods should return bytes.
        Thus file-like object can be a binary file object opened for
        reading, a BytesIO object, or any other custom object that
        meets this interface.

        Optional keyword arguments are *fix_imports*, *encoding* and
        *errors*, which are used to control compatibility support for
        pickle stream generated by Python 2.  If *fix_imports* is True,
        pickle will try to map the old Python 2 names to the new names
        used in Python 3.  The *encoding* and *errors* tell pickle how
        to decode 8-bit string instances pickled by Python 2; these
        default to 'ASCII' and 'strict', respectively. *encoding* can be
        'bytes' to read theses 8-bit string instances as bytes objects.
        """
        self._file_readline = file.readline
        self._file_read = file.read
        self.memo = {}
        self.encoding = encoding
        self.errors = errors
        self.proto = 0
        self.fix_imports = fix_imports

    def load(self):
        """Read a pickled object representation from the open file.

        Return the reconstituted object hierarchy specified in the file.
        """
        if not hasattr(self, '_file_read'):
            raise UnpicklingError('Unpickler.__init__() was not called by %s.__init__()' % (
             self.__class__.__name__,))
        self._unframer = _Unframer(self._file_read, self._file_readline)
        self.read = self._unframer.read
        self.readline = self._unframer.readline
        self.metastack = []
        self.stack = []
        self.append = self.stack.append
        self.proto = 0
        read = self.read
        dispatch = self.dispatch
        try:
            while True:
                key = read(1)
                if not key:
                    raise EOFError
                if not isinstance(key, bytes_types):
                    raise AssertionError
                dispatch[key[0]](self)

        except _Stop as stopinst:
            try:
                return stopinst.value
            finally:
                stopinst = None
                del stopinst

    def pop_mark(self):
        items = self.stack
        self.stack = self.metastack.pop()
        self.append = self.stack.append
        return items

    def persistent_load(self, pid):
        raise UnpicklingError('unsupported persistent id encountered')

    dispatch = {}

    def load_proto(self):
        proto = self.read(1)[0]
        if not 0 <= proto <= HIGHEST_PROTOCOL:
            raise ValueError('unsupported pickle protocol: %d' % proto)
        self.proto = proto

    dispatch[PROTO[0]] = load_proto

    def load_frame(self):
        frame_size, = unpack('<Q', self.read(8))
        if frame_size > sys.maxsize:
            raise ValueError('frame size > sys.maxsize: %d' % frame_size)
        self._unframer.load_frame(frame_size)

    dispatch[FRAME[0]] = load_frame

    def load_persid(self):
        try:
            pid = self.readline()[:-1].decode('ascii')
        except UnicodeDecodeError:
            raise UnpicklingError('persistent IDs in protocol 0 must be ASCII strings')

        self.append(self.persistent_load(pid))

    dispatch[PERSID[0]] = load_persid

    def load_binpersid(self):
        pid = self.stack.pop()
        self.append(self.persistent_load(pid))

    dispatch[BINPERSID[0]] = load_binpersid

    def load_none(self):
        self.append(None)

    dispatch[NONE[0]] = load_none

    def load_false(self):
        self.append(False)

    dispatch[NEWFALSE[0]] = load_false

    def load_true(self):
        self.append(True)

    dispatch[NEWTRUE[0]] = load_true

    def load_int(self):
        data = self.readline()
        if data == FALSE[1:]:
            val = False
        elif data == TRUE[1:]:
            val = True
        else:
            val = int(data, 0)
        self.append(val)

    dispatch[INT[0]] = load_int

    def load_binint(self):
        self.append(unpack('<i', self.read(4))[0])

    dispatch[BININT[0]] = load_binint

    def load_binint1(self):
        self.append(self.read(1)[0])

    dispatch[BININT1[0]] = load_binint1

    def load_binint2(self):
        self.append(unpack('<H', self.read(2))[0])

    dispatch[BININT2[0]] = load_binint2

    def load_long(self):
        val = self.readline()[:-1]
        if val:
            if val[(-1)] == 76:
                val = val[:-1]
            self.append(int(val, 0))

    dispatch[LONG[0]] = load_long

    def load_long1(self):
        n = self.read(1)[0]
        data = self.read(n)
        self.append(decode_long(data))

    dispatch[LONG1[0]] = load_long1

    def load_long4(self):
        n, = unpack('<i', self.read(4))
        if n < 0:
            raise UnpicklingError('LONG pickle has negative byte count')
        data = self.read(n)
        self.append(decode_long(data))

    dispatch[LONG4[0]] = load_long4

    def load_float(self):
        self.append(float(self.readline()[:-1]))

    dispatch[FLOAT[0]] = load_float

    def load_binfloat(self):
        self.append(unpack('>d', self.read(8))[0])

    dispatch[BINFLOAT[0]] = load_binfloat

    def _decode_string(self, value):
        if self.encoding == 'bytes':
            return value
        else:
            return value.decode(self.encoding, self.errors)

    def load_string(self):
        data = self.readline()[:-1]
        if len(data) >= 2:
            pass
        if data[0] == data[(-1)]:
            if data[0] in '"\'':
                data = data[1:-1]
            else:
                raise UnpicklingError('the STRING opcode argument must be quoted')
            self.append(self._decode_string(codecs.escape_decode(data)[0]))

    dispatch[STRING[0]] = load_string

    def load_binstring(self):
        len, = unpack('<i', self.read(4))
        if len < 0:
            raise UnpicklingError('BINSTRING pickle has negative byte count')
        data = self.read(len)
        self.append(self._decode_string(data))

    dispatch[BINSTRING[0]] = load_binstring

    def load_binbytes(self):
        len, = unpack('<I', self.read(4))
        if len > maxsize:
            raise UnpicklingError("BINBYTES exceeds system's maximum size of %d bytes" % maxsize)
        self.append(self.read(len))

    dispatch[BINBYTES[0]] = load_binbytes

    def load_unicode(self):
        self.append(str(self.readline()[:-1], 'raw-unicode-escape'))

    dispatch[UNICODE[0]] = load_unicode

    def load_binunicode(self):
        len, = unpack('<I', self.read(4))
        if len > maxsize:
            raise UnpicklingError("BINUNICODE exceeds system's maximum size of %d bytes" % maxsize)
        self.append(str(self.read(len), 'utf-8', 'surrogatepass'))

    dispatch[BINUNICODE[0]] = load_binunicode

    def load_binunicode8(self):
        len, = unpack('<Q', self.read(8))
        if len > maxsize:
            raise UnpicklingError("BINUNICODE8 exceeds system's maximum size of %d bytes" % maxsize)
        self.append(str(self.read(len), 'utf-8', 'surrogatepass'))

    dispatch[BINUNICODE8[0]] = load_binunicode8

    def load_binbytes8(self):
        len, = unpack('<Q', self.read(8))
        if len > maxsize:
            raise UnpicklingError("BINBYTES8 exceeds system's maximum size of %d bytes" % maxsize)
        self.append(self.read(len))

    dispatch[BINBYTES8[0]] = load_binbytes8

    def load_short_binstring(self):
        len = self.read(1)[0]
        data = self.read(len)
        self.append(self._decode_string(data))

    dispatch[SHORT_BINSTRING[0]] = load_short_binstring

    def load_short_binbytes(self):
        len = self.read(1)[0]
        self.append(self.read(len))

    dispatch[SHORT_BINBYTES[0]] = load_short_binbytes

    def load_short_binunicode(self):
        len = self.read(1)[0]
        self.append(str(self.read(len), 'utf-8', 'surrogatepass'))

    dispatch[SHORT_BINUNICODE[0]] = load_short_binunicode

    def load_tuple(self):
        items = self.pop_mark()
        self.append(tuple(items))

    dispatch[TUPLE[0]] = load_tuple

    def load_empty_tuple(self):
        self.append(())

    dispatch[EMPTY_TUPLE[0]] = load_empty_tuple

    def load_tuple1(self):
        self.stack[-1] = (
         self.stack[(-1)],)

    dispatch[TUPLE1[0]] = load_tuple1

    def load_tuple2(self):
        self.stack[-2:] = [
         (
          self.stack[(-2)], self.stack[(-1)])]

    dispatch[TUPLE2[0]] = load_tuple2

    def load_tuple3(self):
        self.stack[-3:] = [
         (
          self.stack[(-3)], self.stack[(-2)], self.stack[(-1)])]

    dispatch[TUPLE3[0]] = load_tuple3

    def load_empty_list(self):
        self.append([])

    dispatch[EMPTY_LIST[0]] = load_empty_list

    def load_empty_dictionary(self):
        self.append({})

    dispatch[EMPTY_DICT[0]] = load_empty_dictionary

    def load_empty_set(self):
        self.append(set())

    dispatch[EMPTY_SET[0]] = load_empty_set

    def load_frozenset(self):
        items = self.pop_mark()
        self.append(frozenset(items))

    dispatch[FROZENSET[0]] = load_frozenset

    def load_list(self):
        items = self.pop_mark()
        self.append(items)

    dispatch[LIST[0]] = load_list

    def load_dict(self):
        items = self.pop_mark()
        d = {items[i]:items[(i + 1)] for i in range(0, len(items), 2)}
        self.append(d)

    dispatch[DICT[0]] = load_dict

    def _instantiate(self, klass, args):
        if args or isinstance(klass, type) and hasattr(klass, '__getinitargs__'):
            try:
                value = klass(*args)
            except TypeError as err:
                try:
                    raise TypeError('in constructor for %s: %s' % (
                     klass.__name__, str(err)), sys.exc_info()[2])
                finally:
                    err = None
                    del err

        else:
            value = klass.__new__(klass)
        self.append(value)

    def load_inst(self):
        module = self.readline()[:-1].decode('ascii')
        name = self.readline()[:-1].decode('ascii')
        klass = self.find_class(module, name)
        self._instantiate(klass, self.pop_mark())

    dispatch[INST[0]] = load_inst

    def load_obj(self):
        args = self.pop_mark()
        cls = args.pop(0)
        self._instantiate(cls, args)

    dispatch[OBJ[0]] = load_obj

    def load_newobj(self):
        args = self.stack.pop()
        cls = self.stack.pop()
        obj = (cls.__new__)(cls, *args)
        self.append(obj)

    dispatch[NEWOBJ[0]] = load_newobj

    def load_newobj_ex(self):
        kwargs = self.stack.pop()
        args = self.stack.pop()
        cls = self.stack.pop()
        obj = (cls.__new__)(cls, *args, **kwargs)
        self.append(obj)

    dispatch[NEWOBJ_EX[0]] = load_newobj_ex

    def load_global(self):
        module = self.readline()[:-1].decode('utf-8')
        name = self.readline()[:-1].decode('utf-8')
        klass = self.find_class(module, name)
        self.append(klass)

    dispatch[GLOBAL[0]] = load_global

    def load_stack_global(self):
        name = self.stack.pop()
        module = self.stack.pop()
        if type(name) is not str or type(module) is not str:
            raise UnpicklingError('STACK_GLOBAL requires str')
        self.append(self.find_class(module, name))

    dispatch[STACK_GLOBAL[0]] = load_stack_global

    def load_ext1(self):
        code = self.read(1)[0]
        self.get_extension(code)

    dispatch[EXT1[0]] = load_ext1

    def load_ext2(self):
        code, = unpack('<H', self.read(2))
        self.get_extension(code)

    dispatch[EXT2[0]] = load_ext2

    def load_ext4(self):
        code, = unpack('<i', self.read(4))
        self.get_extension(code)

    dispatch[EXT4[0]] = load_ext4

    def get_extension(self, code):
        nil = []
        obj = _extension_cache.get(code, nil)
        if obj is not nil:
            self.append(obj)
            return
        key = _inverted_registry.get(code)
        if not key:
            if code <= 0:
                raise UnpicklingError('EXT specifies code <= 0')
            raise ValueError('unregistered extension code %d' % code)
        obj = (self.find_class)(*key)
        _extension_cache[code] = obj
        self.append(obj)

    def find_class(self, module, name):
        if self.proto < 3:
            if self.fix_imports:
                if (
                 module, name) in _compat_pickle.NAME_MAPPING:
                    module, name = _compat_pickle.NAME_MAPPING[(module, name)]
                elif module in _compat_pickle.IMPORT_MAPPING:
                    module = _compat_pickle.IMPORT_MAPPING[module]
                else:
                    __import__(module, level=0)

            return self.proto >= 4 and _getattribute(sys.modules[module], name)[0]
        else:
            return getattr(sys.modules[module], name)

    def load_reduce(self):
        stack = self.stack
        args = stack.pop()
        func = stack[(-1)]
        stack[-1] = func(*args)

    dispatch[REDUCE[0]] = load_reduce

    def load_pop(self):
        if self.stack:
            del self.stack[-1]
        else:
            self.pop_mark()

    dispatch[POP[0]] = load_pop

    def load_pop_mark(self):
        self.pop_mark()

    dispatch[POP_MARK[0]] = load_pop_mark

    def load_dup(self):
        self.append(self.stack[(-1)])

    dispatch[DUP[0]] = load_dup

    def load_get(self):
        i = int(self.readline()[:-1])
        self.append(self.memo[i])

    dispatch[GET[0]] = load_get

    def load_binget(self):
        i = self.read(1)[0]
        self.append(self.memo[i])

    dispatch[BINGET[0]] = load_binget

    def load_long_binget(self):
        i, = unpack('<I', self.read(4))
        self.append(self.memo[i])

    dispatch[LONG_BINGET[0]] = load_long_binget

    def load_put(self):
        i = int(self.readline()[:-1])
        if i < 0:
            raise ValueError('negative PUT argument')
        self.memo[i] = self.stack[(-1)]

    dispatch[PUT[0]] = load_put

    def load_binput(self):
        i = self.read(1)[0]
        if i < 0:
            raise ValueError('negative BINPUT argument')
        self.memo[i] = self.stack[(-1)]

    dispatch[BINPUT[0]] = load_binput

    def load_long_binput(self):
        i, = unpack('<I', self.read(4))
        if i > maxsize:
            raise ValueError('negative LONG_BINPUT argument')
        self.memo[i] = self.stack[(-1)]

    dispatch[LONG_BINPUT[0]] = load_long_binput

    def load_memoize(self):
        memo = self.memo
        memo[len(memo)] = self.stack[(-1)]

    dispatch[MEMOIZE[0]] = load_memoize

    def load_append(self):
        stack = self.stack
        value = stack.pop()
        list = stack[(-1)]
        list.append(value)

    dispatch[APPEND[0]] = load_append

    def load_appends(self):
        items = self.pop_mark()
        list_obj = self.stack[(-1)]
        try:
            extend = list_obj.extend
        except AttributeError:
            pass
        else:
            extend(items)
            return
            append = list_obj.append
            for item in items:
                append(item)

    dispatch[APPENDS[0]] = load_appends

    def load_setitem(self):
        stack = self.stack
        value = stack.pop()
        key = stack.pop()
        dict = stack[(-1)]
        dict[key] = value

    dispatch[SETITEM[0]] = load_setitem

    def load_setitems(self):
        items = self.pop_mark()
        dict = self.stack[(-1)]
        for i in range(0, len(items), 2):
            dict[items[i]] = items[(i + 1)]

    dispatch[SETITEMS[0]] = load_setitems

    def load_additems(self):
        items = self.pop_mark()
        set_obj = self.stack[(-1)]
        if isinstance(set_obj, set):
            set_obj.update(items)
        else:
            add = set_obj.add
            for item in items:
                add(item)

    dispatch[ADDITEMS[0]] = load_additems

    def load_build(self):
        stack = self.stack
        state = stack.pop()
        inst = stack[(-1)]
        setstate = getattr(inst, '__setstate__', None)
        if setstate is not None:
            setstate(state)
            return
        slotstate = None
        if isinstance(state, tuple):
            if len(state) == 2:
                state, slotstate = state
            if state:
                inst_dict = inst.__dict__
                intern = sys.intern
                for k, v in state.items():
                    if type(k) is str:
                        inst_dict[intern(k)] = v
                    else:
                        inst_dict[k] = v

            if slotstate:
                for k, v in slotstate.items():
                    setattr(inst, k, v)

    dispatch[BUILD[0]] = load_build

    def load_mark(self):
        self.metastack.append(self.stack)
        self.stack = []
        self.append = self.stack.append

    dispatch[MARK[0]] = load_mark

    def load_stop(self):
        value = self.stack.pop()
        raise _Stop(value)

    dispatch[STOP[0]] = load_stop


def _dump(obj, file, protocol=None, *, fix_imports=True):
    _Pickler(file, protocol, fix_imports=fix_imports).dump(obj)


def _dumps(obj, protocol=None, *, fix_imports=True):
    f = io.BytesIO()
    _Pickler(f, protocol, fix_imports=fix_imports).dump(obj)
    res = f.getvalue()
    if not isinstance(res, bytes_types):
        raise AssertionError
    return res


def _load(file, *, fix_imports=True, encoding='ASCII', errors='strict'):
    return _Unpickler(file, fix_imports=fix_imports, encoding=encoding,
      errors=errors).load()


def _loads(s, *, fix_imports=True, encoding='ASCII', errors='strict'):
    if isinstance(s, str):
        raise TypeError("Can't load pickle from unicode string")
    file = io.BytesIO(s)
    return _Unpickler(file, fix_imports=fix_imports, encoding=encoding,
      errors=errors).load()


try:
    from _pickle import PickleError, PicklingError, UnpicklingError, Pickler, Unpickler, dump, dumps, load, loads
except ImportError:
    Pickler, Unpickler = _Pickler, _Unpickler
    dump, dumps, load, loads = (_dump, _dumps, _load, _loads)

def _test():
    import doctest
    return doctest.testmod()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='display contents of the pickle files')
    parser.add_argument('pickle_file',
      type=(argparse.FileType('br')), nargs='*',
      help='the pickle file')
    parser.add_argument('-t',
      '--test', action='store_true', help='run self-test suite')
    parser.add_argument('-v',
      action='store_true', help='run verbosely; only affects self-test run')
    args = parser.parse_args()
    if args.test:
        _test()
    elif not args.pickle_file:
        parser.print_help()
    else:
        import pprint
        for f in args.pickle_file:
            obj = load(f)
            pprint.pprint(obj)