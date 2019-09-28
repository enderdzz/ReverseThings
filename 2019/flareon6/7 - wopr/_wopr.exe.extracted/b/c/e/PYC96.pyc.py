# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: plistlib.py
r"""plistlib.py -- a tool to generate and parse MacOSX .plist files.

The property list (.plist) file format is a simple XML pickle supporting
basic object types, like dictionaries, lists, numbers and strings.
Usually the top level object is a dictionary.

To write out a plist file, use the dump(value, file)
function. 'value' is the top level object, 'file' is
a (writable) file object.

To parse a plist from a file, use the load(file) function,
with a (readable) file object as the only argument. It
returns the top level object (again, usually a dictionary).

To work with plist data in bytes objects, you can use loads()
and dumps().

Values can be strings, integers, floats, booleans, tuples, lists,
dictionaries (but only with string keys), Data, bytes, bytearray, or
datetime.datetime objects.

Generate Plist example:

    pl = dict(
        aString = "Doodah",
        aList = ["A", "B", 12, 32.1, [1, 2, 3]],
        aFloat = 0.1,
        anInt = 728,
        aDict = dict(
            anotherString = "<hello & hi there!>",
            aUnicodeValue = "M\xe4ssig, Ma\xdf",
            aTrueValue = True,
            aFalseValue = False,
        ),
        someData = b"<binary gunk>",
        someMoreData = b"<lots of binary gunk>" * 10,
        aDate = datetime.datetime.fromtimestamp(time.mktime(time.gmtime())),
    )
    with open(fileName, 'wb') as fp:
        dump(pl, fp)

Parse Plist example:

    with open(fileName, 'rb') as fp:
        pl = load(fp)
    print(pl["aKey"])
"""
__all__ = [
 'readPlist', 'writePlist', 'readPlistFromBytes', 'writePlistToBytes',
 'Data', 'InvalidFileException', 'FMT_XML', 'FMT_BINARY',
 'load', 'dump', 'loads', 'dumps']
import binascii, codecs, contextlib, datetime, enum
from io import BytesIO
import itertools, os, re, struct
from warnings import warn
from xml.parsers.expat import ParserCreate
PlistFormat = enum.Enum('PlistFormat', 'FMT_XML FMT_BINARY', module=__name__)
globals().update(PlistFormat.__members__)

@contextlib.contextmanager
def _maybe_open(pathOrFile, mode):
    if isinstance(pathOrFile, str):
        with open(pathOrFile, mode) as (fp):
            yield fp
    else:
        yield pathOrFile


def readPlist(pathOrFile):
    """
    Read a .plist from a path or file. pathOrFile should either
    be a file name, or a readable binary file object.

    This function is deprecated, use load instead.
    """
    warn('The readPlist function is deprecated, use load() instead', DeprecationWarning, 2)
    with _maybe_open(pathOrFile, 'rb') as (fp):
        return load(fp, fmt=None, use_builtin_types=False)


def writePlist(value, pathOrFile):
    """
    Write 'value' to a .plist file. 'pathOrFile' may either be a
    file name or a (writable) file object.

    This function is deprecated, use dump instead.
    """
    warn('The writePlist function is deprecated, use dump() instead', DeprecationWarning, 2)
    with _maybe_open(pathOrFile, 'wb') as (fp):
        dump(value, fp, fmt=FMT_XML, sort_keys=True, skipkeys=False)


def readPlistFromBytes(data):
    """
    Read a plist data from a bytes object. Return the root object.

    This function is deprecated, use loads instead.
    """
    warn('The readPlistFromBytes function is deprecated, use loads() instead', DeprecationWarning, 2)
    return load((BytesIO(data)), fmt=None, use_builtin_types=False)


def writePlistToBytes(value):
    """
    Return 'value' as a plist-formatted bytes object.

    This function is deprecated, use dumps instead.
    """
    warn('The writePlistToBytes function is deprecated, use dumps() instead', DeprecationWarning, 2)
    f = BytesIO()
    dump(value, f, fmt=FMT_XML, sort_keys=True, skipkeys=False)
    return f.getvalue()


class Data:
    r"""'\n    Wrapper for binary data.\n\n    This class is deprecated, use a bytes object instead.\n    '"""

    def __init__(self, data):
        if not isinstance(data, bytes):
            raise TypeError('data must be as bytes')
        self.data = data

    @classmethod
    def fromBase64(cls, data):
        return cls(_decode_base64(data))

    def asBase64(self, maxlinelength=76):
        return _encode_base64(self.data, maxlinelength)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data
        elif isinstance(other, bytes):
            return self.data == other
        else:
            return NotImplemented

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, repr(self.data))


PLISTHEADER = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
_controlCharPat = re.compile('[\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x08\\x0b\\x0c\\x0e\\x0f\\x10\\x11\\x12\\x13\\x14\\x15\\x16\\x17\\x18\\x19\\x1a\\x1b\\x1c\\x1d\\x1e\\x1f]')

def _encode_base64(s, maxlinelength=76):
    maxbinsize = maxlinelength // 4 * 3
    pieces = []
    for i in range(0, len(s), maxbinsize):
        chunk = s[i:i + maxbinsize]
        pieces.append(binascii.b2a_base64(chunk))

    return ''.join(pieces)


def _decode_base64(s):
    if isinstance(s, str):
        return binascii.a2b_base64(s.encode('utf-8'))
    else:
        return binascii.a2b_base64(s)


_dateParser = re.compile('(?P<year>\\d\\d\\d\\d)(?:-(?P<month>\\d\\d)(?:-(?P<day>\\d\\d)(?:T(?P<hour>\\d\\d)(?::(?P<minute>\\d\\d)(?::(?P<second>\\d\\d))?)?)?)?)?Z', re.ASCII)

def _date_from_string(s):
    order = ('year', 'month', 'day', 'hour', 'minute', 'second')
    gd = _dateParser.match(s).groupdict()
    lst = []
    for key in order:
        val = gd[key]
        if val is None:
            break
        lst.append(int(val))

    return (datetime.datetime)(*lst)


def _date_to_string(d):
    return '%04d-%02d-%02dT%02d:%02d:%02dZ' % (
     d.year, d.month, d.day,
     d.hour, d.minute, d.second)


def _escape(text):
    m = _controlCharPat.search(text)
    if m is not None:
        raise ValueError("strings can't contains control characters; use bytes instead")
    text = text.replace('\r\n', '\n')
    text = text.replace('\r', '\n')
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text


class _PlistParser:

    def __init__(self, use_builtin_types, dict_type):
        self.stack = []
        self.current_key = None
        self.root = None
        self._use_builtin_types = use_builtin_types
        self._dict_type = dict_type

    def parse(self, fileobj):
        self.parser = ParserCreate()
        self.parser.StartElementHandler = self.handle_begin_element
        self.parser.EndElementHandler = self.handle_end_element
        self.parser.CharacterDataHandler = self.handle_data
        self.parser.ParseFile(fileobj)
        return self.root

    def handle_begin_element(self, element, attrs):
        self.data = []
        handler = getattr(self, 'begin_' + element, None)
        if handler is not None:
            handler(attrs)

    def handle_end_element(self, element):
        handler = getattr(self, 'end_' + element, None)
        if handler is not None:
            handler()

    def handle_data(self, data):
        self.data.append(data)

    def add_object(self, value):
        if self.current_key is not None:
            if not isinstance(self.stack[(-1)], type({})):
                raise ValueError('unexpected element at line %d' % self.parser.CurrentLineNumber)
            self.stack[(-1)][self.current_key] = value
            self.current_key = None
        elif not self.stack:
            self.root = value
        elif not isinstance(self.stack[(-1)], type([])):
            raise ValueError('unexpected element at line %d' % self.parser.CurrentLineNumber)
        self.stack[(-1)].append(value)

    def get_data(self):
        data = ''.join(self.data)
        self.data = []
        return data

    def begin_dict(self, attrs):
        d = self._dict_type()
        self.add_object(d)
        self.stack.append(d)

    def end_dict(self):
        if self.current_key:
            raise ValueError("missing value for key '%s' at line %d" % (
             self.current_key, self.parser.CurrentLineNumber))
        self.stack.pop()

    def end_key(self):
        if not (self.current_key or isinstance(self.stack[(-1)], type({}))):
            raise ValueError('unexpected key at line %d' % self.parser.CurrentLineNumber)
        self.current_key = self.get_data()

    def begin_array(self, attrs):
        a = []
        self.add_object(a)
        self.stack.append(a)

    def end_array(self):
        self.stack.pop()

    def end_true(self):
        self.add_object(True)

    def end_false(self):
        self.add_object(False)

    def end_integer(self):
        self.add_object(int(self.get_data()))

    def end_real(self):
        self.add_object(float(self.get_data()))

    def end_string(self):
        self.add_object(self.get_data())

    def end_data(self):
        if self._use_builtin_types:
            self.add_object(_decode_base64(self.get_data()))
        else:
            self.add_object(Data.fromBase64(self.get_data()))

    def end_date(self):
        self.add_object(_date_from_string(self.get_data()))


class _DumbXMLWriter:

    def __init__(self, file, indent_level=0, indent='\t'):
        self.file = file
        self.stack = []
        self._indent_level = indent_level
        self.indent = indent

    def begin_element(self, element):
        self.stack.append(element)
        self.writeln('<%s>' % element)
        self._indent_level += 1

    def end_element(self, element):
        if not self._indent_level > 0:
            raise AssertionError
        if not self.stack.pop() == element:
            raise AssertionError
        self._indent_level -= 1
        self.writeln('</%s>' % element)

    def simple_element(self, element, value=None):
        if value is not None:
            value = _escape(value)
            self.writeln('<%s>%s</%s>' % (element, value, element))
        else:
            self.writeln('<%s/>' % element)

    def writeln(self, line):
        if line:
            if isinstance(line, str):
                line = line.encode('utf-8')
            self.file.write(self._indent_level * self.indent)
            self.file.write(line)
        self.file.write('\n')


class _PlistWriter(_DumbXMLWriter):

    def __init__(self, file, indent_level=0, indent='\t', writeHeader=1, sort_keys=True, skipkeys=False):
        if writeHeader:
            file.write(PLISTHEADER)
        _DumbXMLWriter.__init__(self, file, indent_level, indent)
        self._sort_keys = sort_keys
        self._skipkeys = skipkeys

    def write(self, value):
        self.writeln('<plist version="1.0">')
        self.write_value(value)
        self.writeln('</plist>')

    def write_value(self, value):
        if isinstance(value, str):
            self.simple_element('string', value)
        elif value is True:
            self.simple_element('true')
        elif value is False:
            self.simple_element('false')
        elif isinstance(value, int):
            if not -9223372036854775808L <= value < 18446744073709551616L:
                self.simple_element('integer', '%d' % value)
            else:
                raise OverflowError(value)
        elif isinstance(value, float):
            self.simple_element('real', repr(value))
        elif isinstance(value, dict):
            self.write_dict(value)
        elif isinstance(value, Data):
            self.write_data(value)
        elif isinstance(value, (bytes, bytearray)):
            self.write_bytes(value)
        elif isinstance(value, datetime.datetime):
            self.simple_element('date', _date_to_string(value))
        elif isinstance(value, (tuple, list)):
            self.write_array(value)
        else:
            raise TypeError('unsupported type: %s' % type(value))

    def write_data(self, data):
        self.write_bytes(data.data)

    def write_bytes(self, data):
        self.begin_element('data')
        self._indent_level -= 1
        maxlinelength = max(16, 76 - len(self.indent.replace('\t', '        ') * self._indent_level))
        for line in _encode_base64(data, maxlinelength).split('\n'):
            if line:
                self.writeln(line)

        self._indent_level += 1
        self.end_element('data')

    def write_dict(self, d):
        if d:
            self.begin_element('dict')
            if self._sort_keys:
                items = sorted(d.items())
            else:
                items = d.items()
            for key, value in items:
                if not isinstance(key, str):
                    if self._skipkeys:
                        pass
                    else:
                        raise TypeError('keys must be strings')
                self.simple_element('key', key)
                self.write_value(value)

            self.end_element('dict')
        else:
            self.simple_element('dict')

    def write_array(self, array):
        if array:
            self.begin_element('array')
            for value in array:
                self.write_value(value)

            self.end_element('array')
        else:
            self.simple_element('array')


def _is_fmt_xml(header):
    prefixes = ('<?xml', '<plist')
    for pfx in prefixes:
        if header.startswith(pfx):
            return True

    for bom, encoding in (
     (
      codecs.BOM_UTF8, 'utf-8'),
     (
      codecs.BOM_UTF16_BE, 'utf-16-be'),
     (
      codecs.BOM_UTF16_LE, 'utf-16-le')):
        if not header.startswith(bom):
            continue
            for start in prefixes:
                prefix = bom + start.decode('ascii').encode(encoding)
                if header[:len(prefix)] == prefix:
                    return True

    return False


class InvalidFileException(ValueError):

    def __init__(self, message='Invalid file'):
        ValueError.__init__(self, message)


_BINARY_FORMAT = {1:'B', 
 2:'H',  4:'L',  8:'Q'}
_undefined = object()

class _BinaryPlistParser:
    r"""'\n    Read or write a binary plist file, following the description of the binary\n    format.  Raise InvalidFileException in case of error, otherwise return the\n    root object.\n\n    see also: http://opensource.apple.com/source/CF/CF-744.18/CFBinaryPList.c\n    '"""

    def __init__(self, use_builtin_types, dict_type):
        self._use_builtin_types = use_builtin_types
        self._dict_type = dict_type

    def parse(self, fp):
        try:
            self._fp = fp
            self._fp.seek(-32, os.SEEK_END)
            trailer = self._fp.read(32)
            if len(trailer) != 32:
                raise InvalidFileException()
            offset_size, self._ref_size, num_objects, top_object, offset_table_offset = struct.unpack('>6xBBQQQ', trailer)
            self._fp.seek(offset_table_offset)
            self._object_offsets = self._read_ints(num_objects, offset_size)
            self._objects = [_undefined] * num_objects
            return self._read_object(top_object)
        except (OSError, IndexError, struct.error, OverflowError,
         UnicodeDecodeError):
            raise InvalidFileException()

    def _get_size(self, tokenL):
        """ return the size of the next object."""
        if tokenL == 15:
            m = self._fp.read(1)[0] & 3
            s = 1 << m
            f = '>' + _BINARY_FORMAT[s]
            return struct.unpack(f, self._fp.read(s))[0]
        else:
            return tokenL

    def _read_ints(self, n, size):
        data = self._fp.read(size * n)
        if size in _BINARY_FORMAT:
            return struct.unpack('>' + _BINARY_FORMAT[size] * n, data)
        else:
            if size and len(data) != size * n:
                raise InvalidFileException()
            return tuple(int.from_bytes(data[i:i + size], 'big') for i in range(0, size * n, size))

    def _read_refs(self, n):
        return self._read_ints(n, self._ref_size)

    def _read_object(self, ref):
        """
        read the object by reference.

        May recursively read sub-objects (content of an array/dict/set)
        """
        result = self._objects[ref]
        if result is not _undefined:
            return result
        else:
            offset = self._object_offsets[ref]
            self._fp.seek(offset)
            token = self._fp.read(1)[0]
            tokenH, tokenL = token & 240, token & 15
            if token == 0:
                result = None
            elif token == 8:
                result = False
            elif token == 9:
                result = True
            elif token == 15:
                result = ''
            elif tokenH == 16:
                result = int.from_bytes((self._fp.read(1 << tokenL)), 'big',
                  signed=(tokenL >= 3))
            elif token == 34:
                result = struct.unpack('>f', self._fp.read(4))[0]
            elif token == 35:
                result = struct.unpack('>d', self._fp.read(8))[0]
            elif token == 51:
                f = struct.unpack('>d', self._fp.read(8))[0]
                result = datetime.datetime(2001, 1, 1) + datetime.timedelta(seconds=f)
            elif tokenH == 64:
                s = self._get_size(tokenL)
                if self._use_builtin_types:
                    result = self._fp.read(s)
                else:
                    result = Data(self._fp.read(s))
            elif tokenH == 80:
                s = self._get_size(tokenL)
                result = self._fp.read(s).decode('ascii')
                result = result
            elif tokenH == 96:
                s = self._get_size(tokenL)
                result = self._fp.read(s * 2).decode('utf-16be')
            elif tokenH == 160:
                s = self._get_size(tokenL)
                obj_refs = self._read_refs(s)
                result = []
                self._objects[ref] = result
                result.extend((self._read_object(x) for x in obj_refs))
            elif tokenH == 208:
                s = self._get_size(tokenL)
                key_refs = self._read_refs(s)
                obj_refs = self._read_refs(s)
                result = self._dict_type()
                self._objects[ref] = result
                for k, o in zip(key_refs, obj_refs):
                    result[self._read_object(k)] = self._read_object(o)

            else:
                raise InvalidFileException()
            self._objects[ref] = result
            return result


def _count_to_size(count):
    if count < 256:
        return 1
    elif count < 65536:
        return 2
    elif count << 1 << 32:
        return 4
    else:
        return 8


_scalars = (
 str, int, float, datetime.datetime, bytes)

class _BinaryPlistWriter(object):

    def __init__(self, fp, sort_keys, skipkeys):
        self._fp = fp
        self._sort_keys = sort_keys
        self._skipkeys = skipkeys

    def write(self, value):
        self._objlist = []
        self._objtable = {}
        self._objidtable = {}
        self._flatten(value)
        num_objects = len(self._objlist)
        self._object_offsets = [0] * num_objects
        self._ref_size = _count_to_size(num_objects)
        self._ref_format = _BINARY_FORMAT[self._ref_size]
        self._fp.write('bplist00')
        for obj in self._objlist:
            self._write_object(obj)

        top_object = self._getrefnum(value)
        offset_table_offset = self._fp.tell()
        offset_size = _count_to_size(offset_table_offset)
        offset_format = '>' + _BINARY_FORMAT[offset_size] * num_objects
        self._fp.write((struct.pack)(offset_format, *self._object_offsets))
        sort_version = 0
        trailer = (
         sort_version, offset_size, self._ref_size, num_objects,
         top_object, offset_table_offset)
        self._fp.write((struct.pack)(*('>5xBBBQQQ', ), *trailer))

    def _flatten(self, value):
        if isinstance(value, _scalars):
            if (
             type(value), value) in self._objtable:
                return
        elif isinstance(value, Data):
            if (
             type(value.data), value.data) in self._objtable:
                return
        elif id(value) in self._objidtable:
            return
        refnum = len(self._objlist)
        self._objlist.append(value)
        if isinstance(value, _scalars):
            self._objtable[(type(value), value)] = refnum
        elif isinstance(value, Data):
            self._objtable[(type(value.data), value.data)] = refnum
        else:
            self._objidtable[id(value)] = refnum
        if isinstance(value, dict):
            keys = []
            values = []
            items = value.items()
            if self._sort_keys:
                items = sorted(items)
            for k, v in items:
                if not isinstance(k, str):
                    if self._skipkeys:
                        continue
                        raise TypeError('keys must be strings')
                    keys.append(k)
                    values.append(v)

            for o in itertools.chain(keys, values):
                self._flatten(o)

        elif isinstance(value, (list, tuple)):
            for o in value:
                self._flatten(o)

    def _getrefnum(self, value):
        if isinstance(value, _scalars):
            return self._objtable[(type(value), value)]
        elif isinstance(value, Data):
            return self._objtable[(type(value.data), value.data)]
        else:
            return self._objidtable[id(value)]

    def _write_size(self, token, size):
        if size < 15:
            self._fp.write(struct.pack('>B', token | size))
        elif size < 256:
            self._fp.write(struct.pack('>BBB', token | 15, 16, size))
        elif size < 65536:
            self._fp.write(struct.pack('>BBH', token | 15, 17, size))
        elif size < 4294967296L:
            self._fp.write(struct.pack('>BBL', token | 15, 18, size))
        else:
            self._fp.write(struct.pack('>BBQ', token | 15, 19, size))

    def _write_object(self, value):
        ref = self._getrefnum(value)
        self._object_offsets[ref] = self._fp.tell()
        if value is None:
            self._fp.write('\x00')
        elif value is False:
            self._fp.write('\x08')
        elif value is True:
            self._fp.write('\t')
        elif isinstance(value, int):
            if value < 0:
                try:
                    self._fp.write(struct.pack('>Bq', 19, value))
                except struct.error:
                    raise OverflowError(value) from None

            elif value < 256:
                self._fp.write(struct.pack('>BB', 16, value))
            elif value < 65536:
                self._fp.write(struct.pack('>BH', 17, value))
            elif value < 4294967296L:
                self._fp.write(struct.pack('>BL', 18, value))
            elif value < 9223372036854775808L:
                self._fp.write(struct.pack('>BQ', 19, value))
            elif value < 18446744073709551616L:
                self._fp.write('\x14' + value.to_bytes(16, 'big', signed=True))
            else:
                raise OverflowError(value)
        elif isinstance(value, float):
            self._fp.write(struct.pack('>Bd', 35, value))
        elif isinstance(value, datetime.datetime):
            f = (value - datetime.datetime(2001, 1, 1)).total_seconds()
            self._fp.write(struct.pack('>Bd', 51, f))
        elif isinstance(value, Data):
            self._write_size(64, len(value.data))
            self._fp.write(value.data)
        elif isinstance(value, (bytes, bytearray)):
            self._write_size(64, len(value))
            self._fp.write(value)
        elif isinstance(value, str):
            try:
                t = value.encode('ascii')
                self._write_size(80, len(value))
            except UnicodeEncodeError:
                t = value.encode('utf-16be')
                self._write_size(96, len(t) // 2)

            self._fp.write(t)
        elif isinstance(value, (list, tuple)):
            refs = [self._getrefnum(o) for o in value]
            s = len(refs)
            self._write_size(160, s)
            self._fp.write((struct.pack)('>' + self._ref_format * s, *refs))
        elif isinstance(value, dict):
            keyRefs, valRefs = [], []
            if self._sort_keys:
                rootItems = sorted(value.items())
            else:
                rootItems = value.items()
            for k, v in rootItems:
                if not isinstance(k, str):
                    if self._skipkeys:
                        pass
                    else:
                        raise TypeError('keys must be strings')
                keyRefs.append(self._getrefnum(k))
                valRefs.append(self._getrefnum(v))

            s = len(keyRefs)
            self._write_size(208, s)
            self._fp.write((struct.pack)('>' + self._ref_format * s, *keyRefs))
            self._fp.write((struct.pack)('>' + self._ref_format * s, *valRefs))
        else:
            raise TypeError(value)


def _is_fmt_binary(header):
    return header[:8] == 'bplist00'


_FORMATS = {FMT_XML: dict(detect=_is_fmt_xml,
            parser=_PlistParser,
            writer=_PlistWriter), 
 
 FMT_BINARY: dict(detect=_is_fmt_binary,
               parser=_BinaryPlistParser,
               writer=_BinaryPlistWriter)}

def load(fp, *, fmt=None, use_builtin_types=True, dict_type=dict):
    """Read a .plist file. 'fp' should be (readable) file object.
    Return the unpacked root object (which usually is a dictionary).
    """
    if fmt is None:
        header = fp.read(32)
        fp.seek(0)
        for info in _FORMATS.values():
            if info['detect'](header):
                P = info['parser']
                break
        else:
            raise InvalidFileException()

    else:
        P = _FORMATS[fmt]['parser']
    p = P(use_builtin_types=use_builtin_types, dict_type=dict_type)
    return p.parse(fp)


def loads(value, *, fmt=None, use_builtin_types=True, dict_type=dict):
    """Read a .plist file from a bytes object.
    Return the unpacked root object (which usually is a dictionary).
    """
    fp = BytesIO(value)
    return load(fp,
      fmt=fmt, use_builtin_types=use_builtin_types, dict_type=dict_type)


def dump(value, fp, *, fmt=FMT_XML, sort_keys=True, skipkeys=False):
    """Write 'value' to a .plist file. 'fp' should be a (writable)
    file object.
    """
    if fmt not in _FORMATS:
        raise ValueError('Unsupported format: %r' % (fmt,))
    writer = _FORMATS[fmt]['writer'](fp, sort_keys=sort_keys, skipkeys=skipkeys)
    writer.write(value)


def dumps(value, *, fmt=FMT_XML, skipkeys=False, sort_keys=True):
    """Return a bytes object with the contents for a .plist file.
    """
    fp = BytesIO()
    dump(value, fp, fmt=fmt, skipkeys=skipkeys, sort_keys=sort_keys)
    return fp.getvalue()