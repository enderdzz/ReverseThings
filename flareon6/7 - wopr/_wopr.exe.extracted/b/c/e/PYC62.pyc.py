# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: tarfile.py
"""Read from and write to tar format archives.
"""
version = '0.9.0'
__author__ = u'Lars Gusta\u0308bel (lars@gustaebel.de)'
__credits__ = u'Gustavo Niemeyer, Niels Gusta\u0308bel, Richard Townsend.'
from builtins import open as bltn_open
import sys, os, io, shutil, stat, time, struct, copy, re
try:
    import pwd
except ImportError:
    pwd = None

try:
    import grp
except ImportError:
    grp = None

symlink_exception = (
 AttributeError, NotImplementedError)
try:
    symlink_exception += (OSError,)
except NameError:
    pass

__all__ = [
 'TarFile', 'TarInfo', 'is_tarfile', 'TarError', 'ReadError',
 'CompressionError', 'StreamError', 'ExtractError', 'HeaderError',
 'ENCODING', 'USTAR_FORMAT', 'GNU_FORMAT', 'PAX_FORMAT',
 'DEFAULT_FORMAT', 'open']
NUL = '\x00'
BLOCKSIZE = 512
RECORDSIZE = BLOCKSIZE * 20
GNU_MAGIC = 'ustar  \x00'
POSIX_MAGIC = 'ustar\x0000'
LENGTH_NAME = 100
LENGTH_LINK = 100
LENGTH_PREFIX = 155
REGTYPE = '0'
AREGTYPE = '\x00'
LNKTYPE = '1'
SYMTYPE = '2'
CHRTYPE = '3'
BLKTYPE = '4'
DIRTYPE = '5'
FIFOTYPE = '6'
CONTTYPE = '7'
GNUTYPE_LONGNAME = 'L'
GNUTYPE_LONGLINK = 'K'
GNUTYPE_SPARSE = 'S'
XHDTYPE = 'x'
XGLTYPE = 'g'
SOLARIS_XHDTYPE = 'X'
USTAR_FORMAT = 0
GNU_FORMAT = 1
PAX_FORMAT = 2
DEFAULT_FORMAT = GNU_FORMAT
SUPPORTED_TYPES = (
 REGTYPE, AREGTYPE, LNKTYPE,
 SYMTYPE, DIRTYPE, FIFOTYPE,
 CONTTYPE, CHRTYPE, BLKTYPE,
 GNUTYPE_LONGNAME, GNUTYPE_LONGLINK,
 GNUTYPE_SPARSE)
REGULAR_TYPES = (
 REGTYPE, AREGTYPE,
 CONTTYPE, GNUTYPE_SPARSE)
GNU_TYPES = (
 GNUTYPE_LONGNAME, GNUTYPE_LONGLINK,
 GNUTYPE_SPARSE)
PAX_FIELDS = ('path', 'linkpath', 'size', 'mtime', 'uid', 'gid', 'uname', 'gname')
PAX_NAME_FIELDS = {
 'path', 'linkpath', 'uname', 'gname'}
PAX_NUMBER_FIELDS = {'atime':float, 
 'ctime':float, 
 'mtime':float, 
 'uid':int, 
 'gid':int, 
 'size':int}
if os.name == 'nt':
    ENCODING = 'utf-8'
else:
    ENCODING = sys.getfilesystemencoding()

def stn(s, length, encoding, errors):
    """Convert a string to a null-terminated bytes object.
    """
    s = s.encode(encoding, errors)
    return s[:length] + (length - len(s)) * NUL


def nts(s, encoding, errors):
    """Convert a null-terminated bytes object to a string.
    """
    p = s.find('\x00')
    if p != -1:
        s = s[:p]
    return s.decode(encoding, errors)


def nti(s):
    """Convert a number field to a python number.
    """
    if s[0] in (128, 255):
        n = 0
        for i in range(len(s) - 1):
            n <<= 8
            n += s[(i + 1)]

        if s[0] == 255:
            n = -(256 ** (len(s) - 1) - n)
        else:
            try:
                s = nts(s, 'ascii', 'strict')
                n = int(s.strip() or '0', 8)
            except ValueError:
                raise InvalidHeaderError('invalid header')

            return n


def itn--- This code section failed: ---

 203       0  LOAD_GLOBAL              int
           2  LOAD_FAST                'n'
           4  CALL_FUNCTION_1       1  ''
           6  STORE_FAST               'n'

 204       8  LOAD_CONST               0
          10  LOAD_FAST                'n'
          12  DUP_TOP          
          14  ROT_THREE        
          16  COMPARE_OP               <=
          18  POP_JUMP_IF_FALSE    36  'to 36'
          20  LOAD_CONST               8
          22  LOAD_FAST                'digits'
          24  LOAD_CONST               1
          26  BINARY_SUBTRACT  
          28  BINARY_POWER     
          30  COMPARE_OP               <
          32  POP_JUMP_IF_FALSE    68  'to 68'
          34  JUMP_FORWARD         40  'to 40'
          36  ELSE                     '40'
          36  POP_TOP          
          38  JUMP_FORWARD         68  'to 68'
        40_0  COME_FROM            34  '34'

 205      40  LOAD_GLOBAL              bytes
          42  LOAD_STR                 '%0*o'
          44  LOAD_FAST                'digits'
          46  LOAD_CONST               1
          48  BINARY_SUBTRACT  
          50  LOAD_FAST                'n'
          52  BUILD_TUPLE_2         2 
          54  BINARY_MODULO    
          56  LOAD_STR                 'ascii'
          58  CALL_FUNCTION_2       2  ''
          60  LOAD_GLOBAL              NUL
          62  BINARY_ADD       
          64  STORE_FAST               's'
          66  JUMP_FORWARD        216  'to 216'
        68_0  COME_FROM            38  '38'
        68_1  COME_FROM            32  '32'

 206      68  LOAD_FAST                'format'
          70  LOAD_GLOBAL              GNU_FORMAT
          72  COMPARE_OP               ==
          74  POP_JUMP_IF_FALSE   208  'to 208'
          76  LOAD_CONST               256
          78  LOAD_FAST                'digits'
          80  LOAD_CONST               1
          82  BINARY_SUBTRACT  
          84  BINARY_POWER     
          86  UNARY_NEGATIVE   
          88  LOAD_FAST                'n'
          90  DUP_TOP          
          92  ROT_THREE        
          94  COMPARE_OP               <=
          96  POP_JUMP_IF_FALSE   114  'to 114'
          98  LOAD_CONST               256
         100  LOAD_FAST                'digits'
         102  LOAD_CONST               1
         104  BINARY_SUBTRACT  
         106  BINARY_POWER     
         108  COMPARE_OP               <
         110  POP_JUMP_IF_FALSE   208  'to 208'
         112  JUMP_FORWARD        118  'to 118'
         114  ELSE                     '118'
         114  POP_TOP          
         116  JUMP_FORWARD        208  'to 208'
       118_0  COME_FROM           112  '112'

 207     118  LOAD_FAST                'n'
         120  LOAD_CONST               0
         122  COMPARE_OP               >=
         124  POP_JUMP_IF_FALSE   138  'to 138'

 208     126  LOAD_GLOBAL              bytearray
         128  LOAD_CONST               128
         130  BUILD_LIST_1          1 
         132  CALL_FUNCTION_1       1  ''
         134  STORE_FAST               's'
         136  JUMP_FORWARD        160  'to 160'
         138  ELSE                     '160'

 210     138  LOAD_GLOBAL              bytearray
         140  LOAD_CONST               255
         142  BUILD_LIST_1          1 
         144  CALL_FUNCTION_1       1  ''
         146  STORE_FAST               's'

 211     148  LOAD_CONST               256
         150  LOAD_FAST                'digits'
         152  BINARY_POWER     
         154  LOAD_FAST                'n'
         156  BINARY_ADD       
         158  STORE_FAST               'n'
       160_0  COME_FROM           136  '136'

 213     160  SETUP_LOOP          216  'to 216'
         162  LOAD_GLOBAL              range
         164  LOAD_FAST                'digits'
         166  LOAD_CONST               1
         168  BINARY_SUBTRACT  
         170  CALL_FUNCTION_1       1  ''
         172  GET_ITER         
         174  FOR_ITER            204  'to 204'
         176  STORE_FAST               'i'

 214     178  LOAD_FAST                's'
         180  LOAD_METHOD              insert
         182  LOAD_CONST               1
         184  LOAD_FAST                'n'
         186  LOAD_CONST               255
         188  BINARY_AND       
         190  CALL_METHOD_2         2  ''
         192  POP_TOP          

 215     194  LOAD_FAST                'n'
         196  LOAD_CONST               8
         198  INPLACE_RSHIFT   
         200  STORE_FAST               'n'
         202  JUMP_BACK           174  'to 174'
         204  POP_BLOCK        
         206  JUMP_FORWARD        216  'to 216'
       208_0  COME_FROM           116  '116'
       208_1  COME_FROM           110  '110'
       208_2  COME_FROM            74  '74'

 217     208  LOAD_GLOBAL              ValueError
         210  LOAD_STR                 'overflow in number field'
         212  CALL_FUNCTION_1       1  ''
         214  RAISE_VARARGS_1       1  ''
       216_0  COME_FROM           206  '206'
       216_1  COME_FROM_LOOP      160  '160'
       216_2  COME_FROM            66  '66'

 219     216  LOAD_FAST                's'
         218  RETURN_VALUE     
          -1  RETURN_LAST      

Parse error at or near `JUMP_FORWARD' instruction at offset 206


def calc_chksums(buf):
    """Calculate the checksum for a member's header by summing up all
       characters except for the chksum field which is treated as if
       it was filled with spaces. According to the GNU tar sources,
       some tars (Sun and NeXT) calculate chksum with signed char,
       which will be different if there are chars in the buffer with
       the high bit set. So we calculate two checksums, unsigned and
       signed.
    """
    unsigned_chksum = 256 + sum(struct.unpack_from('148B8x356B', buf))
    signed_chksum = 256 + sum(struct.unpack_from('148b8x356b', buf))
    return (
     unsigned_chksum, signed_chksum)


def copyfileobj(src, dst, length=None, exception=OSError, bufsize=None):
    """Copy length bytes from fileobj src to fileobj dst.
       If length is None, copy the entire content.
    """
    bufsize = bufsize or 16384
    if length == 0:
        return
    if length is None:
        shutil.copyfileobj(src, dst, bufsize)
        return
    blocks, remainder = divmod(length, bufsize)
    for b in range(blocks):
        buf = src.read(bufsize)
        if len(buf) < bufsize:
            raise exception('unexpected end of data')
        dst.write(buf)

    if remainder != 0:
        buf = src.read(remainder)
        if len(buf) < remainder:
            raise exception('unexpected end of data')
        dst.write(buf)


def filemode(mode):
    """Deprecated in this location; use stat.filemode."""
    import warnings
    warnings.warn('deprecated in favor of stat.filemode', DeprecationWarning, 2)
    return stat.filemode(mode)


def _safe_print(s):
    encoding = getattr(sys.stdout, 'encoding', None)
    if encoding is not None:
        s = s.encode(encoding, 'backslashreplace').decode(encoding)
    print(s, end=' ')


class TarError(Exception):
    """'Base exception.'"""
    pass


class ExtractError(TarError):
    """'General exception for extract errors.'"""
    pass


class ReadError(TarError):
    """'Exception for unreadable tar archives.'"""
    pass


class CompressionError(TarError):
    """'Exception for unavailable compression methods.'"""
    pass


class StreamError(TarError):
    """'Exception for unsupported operations on stream-like TarFiles.'"""
    pass


class HeaderError(TarError):
    """'Base exception for header errors.'"""
    pass


class EmptyHeaderError(HeaderError):
    """'Exception for empty headers.'"""
    pass


class TruncatedHeaderError(HeaderError):
    """'Exception for truncated headers.'"""
    pass


class EOFHeaderError(HeaderError):
    """'Exception for end of file headers.'"""
    pass


class InvalidHeaderError(HeaderError):
    """'Exception for invalid headers.'"""
    pass


class SubsequentHeaderError(HeaderError):
    """'Exception for missing and invalid extended headers.'"""
    pass


class _LowLevelFile:
    r"""'Low-level file object. Supports reading and writing.\n       It is used instead of a regular file object for streaming\n       access.\n    '"""

    def __init__(self, name, mode):
        mode = {'r':os.O_RDONLY, 
         'w':os.O_WRONLY | os.O_CREAT | os.O_TRUNC}[mode]
        if hasattr(os, 'O_BINARY'):
            mode |= os.O_BINARY
        self.fd = os.open(name, mode, 438)

    def close(self):
        os.close(self.fd)

    def read(self, size):
        return os.read(self.fd, size)

    def write(self, s):
        os.write(self.fd, s)


class _Stream:
    r"""'Class that serves as an adapter between TarFile and\n       a stream-like object.  The stream-like object only\n       needs to have a read() or write() method and is accessed\n       blockwise.  Use of gzip or bzip2 compression is possible.\n       A stream-like object could be for example: sys.stdin,\n       sys.stdout, a socket, a tape device etc.\n\n       _Stream is intended to be used only internally.\n    '"""

    def __init__(self, name, mode, comptype, fileobj, bufsize):
        """Construct a _Stream object.
        """
        self._extfileobj = True
        if fileobj is None:
            fileobj = _LowLevelFile(name, mode)
            self._extfileobj = False
        if comptype == '*':
            fileobj = _StreamProxy(fileobj)
            comptype = fileobj.getcomptype()
        self.name = name or ''
        self.mode = mode
        self.comptype = comptype
        self.fileobj = fileobj
        self.bufsize = bufsize
        self.buf = ''
        self.pos = 0
        self.closed = False
        try:
            if comptype == 'gz':
                try:
                    import zlib
                except ImportError:
                    raise CompressionError('zlib module is not available')

                self.zlib = zlib
                self.crc = zlib.crc32('')
                if mode == 'r':
                    self._init_read_gz()
                    self.exception = zlib.error
                else:
                    self._init_write_gz()
            elif comptype == 'bz2':
                try:
                    import bz2
                except ImportError:
                    raise CompressionError('bz2 module is not available')

                if mode == 'r':
                    self.dbuf = ''
                    self.cmp = bz2.BZ2Decompressor()
                    self.exception = OSError
                else:
                    self.cmp = bz2.BZ2Compressor()
            elif comptype == 'xz':
                try:
                    import lzma
                except ImportError:
                    raise CompressionError('lzma module is not available')

                if mode == 'r':
                    self.dbuf = ''
                    self.cmp = lzma.LZMADecompressor()
                    self.exception = lzma.LZMAError
                else:
                    self.cmp = lzma.LZMACompressor()
            elif comptype != 'tar':
                raise CompressionError('unknown compression type %r' % comptype)
        except:
            if not self._extfileobj:
                self.fileobj.close()
            self.closed = True
            raise

    def __del__(self):
        if hasattr(self, 'closed'):
            pass
        if not self.closed:
            self.close()

    def _init_write_gz(self):
        """Initialize for writing with gzip compression.
        """
        self.cmp = self.zlib.compressobj(9, self.zlib.DEFLATED, -self.zlib.MAX_WBITS, self.zlib.DEF_MEM_LEVEL, 0)
        timestamp = struct.pack('<L', int(time.time()))
        self._Stream__write('\x1f\x8b\x08\x08' + timestamp + '\x02\xff')
        if self.name.endswith('.gz'):
            self.name = self.name[:-3]
        self._Stream__write(self.name.encode('iso-8859-1', 'replace') + NUL)

    def write(self, s):
        """Write string s to the stream.
        """
        if self.comptype == 'gz':
            self.crc = self.zlib.crc32(s, self.crc)
        self.pos += len(s)
        if self.comptype != 'tar':
            s = self.cmp.compress(s)
        self._Stream__write(s)

    def __write(self, s):
        """Write string s to the stream if a whole new block
           is ready to be written.
        """
        self.buf += s
        while 1:
            if len(self.buf) > self.bufsize:
                self.fileobj.write(self.buf[:self.bufsize])
                self.buf = self.buf[self.bufsize:]

    def close(self):
        """Close the _Stream object. No operation should be
           done on it afterwards.
        """
        if self.closed:
            return
        self.closed = True
        try:
            if self.mode == 'w':
                if self.comptype != 'tar':
                    self.buf += self.cmp.flush()
                if self.mode == 'w':
                    if self.buf:
                        self.fileobj.write(self.buf)
                self.buf = ''
                if self.comptype == 'gz':
                    self.fileobj.write(struct.pack('<L', self.crc))
                    self.fileobj.write(struct.pack('<L', self.pos & 4294967295L))
        finally:
            if not self._extfileobj:
                self.fileobj.close()

    def _init_read_gz(self):
        """Initialize for reading a gzip compressed fileobj.
        """
        self.cmp = self.zlib.decompressobj(-self.zlib.MAX_WBITS)
        self.dbuf = ''
        if self._Stream__read(2) != '\x1f\x8b':
            raise ReadError('not a gzip file')
        if self._Stream__read(1) != '\x08':
            raise CompressionError('unsupported compression method')
        flag = ord(self._Stream__read(1))
        self._Stream__read(6)
        if flag & 4:
            xlen = ord(self._Stream__read(1)) + 256 * ord(self._Stream__read(1))
            self.read(xlen)
        if flag & 8:
            while 1:
                s = self._Stream__read(1)
                if s and s == NUL:
                    break

        if flag & 16:
            while 1:
                s = self._Stream__read(1)
                if s and s == NUL:
                    break

        if flag & 2:
            self._Stream__read(2)

    def tell(self):
        """Return the stream's file pointer position.
        """
        return self.pos

    def seek(self, pos=0):
        """Set the stream's file pointer to pos. Negative seeking
           is forbidden.
        """
        if pos - self.pos >= 0:
            blocks, remainder = divmod(pos - self.pos, self.bufsize)
            for i in range(blocks):
                self.read(self.bufsize)

            self.read(remainder)
        else:
            raise StreamError('seeking backwards is not allowed')
        return self.pos

    def read(self, size=None):
        """Return the next size number of bytes from the stream.
           If size is not defined, return all bytes of the stream
           up to EOF.
        """
        if size is None:
            t = []
            while True:
                buf = self._read(self.bufsize)
                if not buf:
                    break
                t.append(buf)

            buf = ''.join(t)
        else:
            buf = self._read(size)
        self.pos += len(buf)
        return buf

    def _read(self, size):
        """Return size bytes from the stream.
        """
        if self.comptype == 'tar':
            return self._Stream__read(size)
        else:
            c = len(self.dbuf)
            t = [self.dbuf]
            while 1:
                if c < size:
                    buf = self._Stream__read(self.bufsize)
                    if not buf:
                        break
                    try:
                        buf = self.cmp.decompress(buf)
                    except self.exception:
                        raise ReadError('invalid compressed data')

                    t.append(buf)
                    c += len(buf)

            t = ''.join(t)
            self.dbuf = t[size:]
            return t[:size]

    def __read(self, size):
        """Return size bytes from stream. If internal buffer is empty,
           read another block from the stream.
        """
        c = len(self.buf)
        t = [self.buf]
        while 1:
            if c < size:
                buf = self.fileobj.read(self.bufsize)
                if not buf:
                    break
                t.append(buf)
                c += len(buf)

        t = ''.join(t)
        self.buf = t[size:]
        return t[:size]


class _StreamProxy(object):
    """"Small proxy class that enables transparent compression\\n       detection for the Stream interface (mode 'r|*').\\n    \""""

    def __init__(self, fileobj):
        self.fileobj = fileobj
        self.buf = self.fileobj.read(BLOCKSIZE)

    def read(self, size):
        self.read = self.fileobj.read
        return self.buf

    def getcomptype(self):
        if self.buf.startswith('\x1f\x8b\x08'):
            return 'gz'
        else:
            if self.buf[0:3] == 'BZh':
                if self.buf[4:10] == '1AY&SY':
                    return 'bz2'
                if self.buf.startswith((']\x00\x00\x80', '\xfd7zXZ')):
                    return 'xz'
            return 'tar'

    def close(self):
        self.fileobj.close()


class _FileInFile(object):
    r"""'A thin wrapper around an existing file object that\n       provides a part of its data as an individual file\n       object.\n    '"""

    def __init__(self, fileobj, offset, size, blockinfo=None):
        self.fileobj = fileobj
        self.offset = offset
        self.size = size
        self.position = 0
        self.name = getattr(fileobj, 'name', None)
        self.closed = False
        if blockinfo is None:
            blockinfo = [
             (
              0, size)]
        self.map_index = 0
        self.map = []
        lastpos = 0
        realpos = self.offset
        for offset, size in blockinfo:
            if offset > lastpos:
                self.map.append((False, lastpos, offset, None))
            self.map.append((True, offset, offset + size, realpos))
            realpos += size
            lastpos = offset + size

        if lastpos < self.size:
            self.map.append((False, lastpos, self.size, None))

    def flush(self):
        pass

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return self.fileobj.seekable()

    def tell(self):
        """Return the current file position.
        """
        return self.position

    def seek(self, position, whence=io.SEEK_SET):
        """Seek to a position in the file.
        """
        if whence == io.SEEK_SET:
            self.position = min(max(position, 0), self.size)
        elif whence == io.SEEK_CUR:
            if position < 0:
                self.position = max(self.position + position, 0)
            else:
                self.position = min(self.position + position, self.size)
        elif whence == io.SEEK_END:
            self.position = max(min(self.size + position, self.size), 0)
        else:
            raise ValueError('Invalid argument')
        return self.position

    def read(self, size=None):
        """Read data from the file.
        """
        if size is None:
            size = self.size - self.position
        else:
            size = min(size, self.size - self.position)
        buf = ''
        while size > 0:
            while 1:
                data, start, stop, offset = self.map[self.map_index]
                if not start <= self.position < stop:
                    break
                else:
                    self.map_index += 1
                    if self.map_index == len(self.map):
                        self.map_index = 0

            length = min(size, stop - self.position)
            if data:
                self.fileobj.seek(offset + (self.position - start))
                b = self.fileobj.read(length)
                if len(b) != length:
                    raise ReadError('unexpected end of data')
                buf += b
            else:
                buf += NUL * length
            size -= length
            self.position += length

        return buf

    def readinto(self, b):
        buf = self.read(len(b))
        b[:len(buf)] = buf
        return len(buf)

    def close(self):
        self.closed = True


class ExFileObject(io.BufferedReader):

    def __init__(self, tarfile, tarinfo):
        fileobj = _FileInFile(tarfile.fileobj, tarinfo.offset_data, tarinfo.size, tarinfo.sparse)
        super().__init__(fileobj)


class TarInfo(object):
    r"""'Informational class which holds the details about an\n       archive member given by a tar header block.\n       TarInfo objects are returned by TarFile.getmember(),\n       TarFile.getmembers() and TarFile.gettarinfo() and are\n       usually created internally.\n    '"""
    __slots__ = ('name', 'mode', 'uid', 'gid', 'size', 'mtime', 'chksum', 'type', 'linkname',
                 'uname', 'gname', 'devmajor', 'devminor', 'offset', 'offset_data',
                 'pax_headers', 'sparse', 'tarfile', '_sparse_structs', '_link_target')

    def __init__(self, name=''):
        """Construct a TarInfo object. name is the optional name
           of the member.
        """
        self.name = name
        self.mode = 420
        self.uid = 0
        self.gid = 0
        self.size = 0
        self.mtime = 0
        self.chksum = 0
        self.type = REGTYPE
        self.linkname = ''
        self.uname = ''
        self.gname = ''
        self.devmajor = 0
        self.devminor = 0
        self.offset = 0
        self.offset_data = 0
        self.sparse = None
        self.pax_headers = {}

    @property
    def path(self):
        return self.name

    @path.setter
    def path(self, name):
        self.name = name

    @property
    def linkpath(self):
        return self.linkname

    @linkpath.setter
    def linkpath(self, linkname):
        self.linkname = linkname

    def __repr__(self):
        return '<%s %r at %#x>' % (self.__class__.__name__, self.name, id(self))

    def get_info(self):
        """Return the TarInfo's attributes as a dictionary.
        """
        info = {'name':self.name, 
         'mode':self.mode & 4095, 
         'uid':self.uid, 
         'gid':self.gid, 
         'size':self.size, 
         'mtime':self.mtime, 
         'chksum':self.chksum, 
         'type':self.type, 
         'linkname':self.linkname, 
         'uname':self.uname, 
         'gname':self.gname, 
         'devmajor':self.devmajor, 
         'devminor':self.devminor}
        if info['type'] == DIRTYPE:
            if not info['name'].endswith('/'):
                info['name'] += '/'
            return info

    def tobuf(self, format=DEFAULT_FORMAT, encoding=ENCODING, errors='surrogateescape'):
        """Return a tar header as a string of 512 byte blocks.
        """
        info = self.get_info()
        if format == USTAR_FORMAT:
            return self.create_ustar_header(info, encoding, errors)
        if format == GNU_FORMAT:
            return self.create_gnu_header(info, encoding, errors)
        if format == PAX_FORMAT:
            return self.create_pax_header(info, encoding)
        raise ValueError('invalid format')

    def create_ustar_header(self, info, encoding, errors):
        """Return the object as a ustar header block.
        """
        info['magic'] = POSIX_MAGIC
        if len(info['linkname'].encode(encoding, errors)) > LENGTH_LINK:
            raise ValueError('linkname is too long')
        if len(info['name'].encode(encoding, errors)) > LENGTH_NAME:
            info['prefix'], info['name'] = self._posix_split_name(info['name'], encoding, errors)
        return self._create_header(info, USTAR_FORMAT, encoding, errors)

    def create_gnu_header(self, info, encoding, errors):
        """Return the object as a GNU header block sequence.
        """
        info['magic'] = GNU_MAGIC
        buf = ''
        if len(info['linkname'].encode(encoding, errors)) > LENGTH_LINK:
            buf += self._create_gnu_long_header(info['linkname'], GNUTYPE_LONGLINK, encoding, errors)
        if len(info['name'].encode(encoding, errors)) > LENGTH_NAME:
            buf += self._create_gnu_long_header(info['name'], GNUTYPE_LONGNAME, encoding, errors)
        return buf + self._create_header(info, GNU_FORMAT, encoding, errors)

    def create_pax_header--- This code section failed: ---

 854       0  LOAD_GLOBAL              POSIX_MAGIC
           2  LOAD_FAST                'info'
           4  LOAD_STR                 'magic'
           6  STORE_SUBSCR     

 855       8  LOAD_FAST                'self'
          10  LOAD_ATTR                pax_headers
          12  LOAD_METHOD              copy
          14  CALL_METHOD_0         0  ''
          16  STORE_FAST               'pax_headers'

 859      18  SETUP_LOOP          152  'to 152'

 860      20  LOAD_STR                 'name'
          22  LOAD_STR                 'path'
          24  LOAD_GLOBAL              LENGTH_NAME
          26  BUILD_TUPLE_3         3 
          28  LOAD_STR                 'linkname'
          30  LOAD_STR                 'linkpath'
          32  LOAD_GLOBAL              LENGTH_LINK
          34  BUILD_TUPLE_3         3 

 861      36  LOAD_CONST               ('uname', 'uname', 32)
          38  LOAD_CONST               ('gname', 'gname', 32)
          40  BUILD_TUPLE_4         4 
          42  GET_ITER         
          44  FOR_ITER            150  'to 150'
          46  UNPACK_SEQUENCE_3     3 
          48  STORE_FAST               'name'
          50  STORE_FAST               'hname'
          52  STORE_FAST               'length'

 863      54  LOAD_FAST                'hname'
          56  LOAD_FAST                'pax_headers'
          58  COMPARE_OP               in
          60  POP_JUMP_IF_FALSE    64  'to 64'

 865      62  CONTINUE             44  'to 44'
          64  ELSE                     '148'

 868      64  SETUP_EXCEPT         86  'to 86'

 869      66  LOAD_FAST                'info'
          68  LOAD_FAST                'name'
          70  BINARY_SUBSCR    
          72  LOAD_METHOD              encode
          74  LOAD_STR                 'ascii'
          76  LOAD_STR                 'strict'
          78  CALL_METHOD_2         2  ''
          80  POP_TOP          
          82  POP_BLOCK        
          84  JUMP_FORWARD        120  'to 120'
        86_0  COME_FROM_EXCEPT     64  '64'

 870      86  DUP_TOP          
          88  LOAD_GLOBAL              UnicodeEncodeError
          90  COMPARE_OP               exception-match
          92  POP_JUMP_IF_FALSE   118  'to 118'
          94  POP_TOP          
          96  POP_TOP          
          98  POP_TOP          

 871     100  LOAD_FAST                'info'
         102  LOAD_FAST                'name'
         104  BINARY_SUBSCR    
         106  LOAD_FAST                'pax_headers'
         108  LOAD_FAST                'hname'
         110  STORE_SUBSCR     

 872     112  CONTINUE_LOOP        44  'to 44'
         114  POP_EXCEPT       
         116  JUMP_FORWARD        120  'to 120'
         118  END_FINALLY      
       120_0  COME_FROM           116  '116'
       120_1  COME_FROM            84  '84'

 874     120  LOAD_GLOBAL              len
         122  LOAD_FAST                'info'
         124  LOAD_FAST                'name'
         126  BINARY_SUBSCR    
         128  CALL_FUNCTION_1       1  ''
         130  LOAD_FAST                'length'
         132  COMPARE_OP               >
         134  POP_JUMP_IF_FALSE    44  'to 44'

 875     136  LOAD_FAST                'info'
         138  LOAD_FAST                'name'
         140  BINARY_SUBSCR    
         142  LOAD_FAST                'pax_headers'
         144  LOAD_FAST                'hname'
         146  STORE_SUBSCR     
         148  JUMP_BACK            44  'to 44'
         150  POP_BLOCK        
       152_0  COME_FROM_LOOP       18  '18'

 879     152  SETUP_LOOP          258  'to 258'
         154  LOAD_CONST               (('uid', 8), ('gid', 8), ('size', 12), ('mtime', 12))
         156  GET_ITER         
         158  FOR_ITER            256  'to 256'
         160  UNPACK_SEQUENCE_2     2 
         162  STORE_FAST               'name'
         164  STORE_FAST               'digits'

 880     166  LOAD_FAST                'name'
         168  LOAD_FAST                'pax_headers'
         170  COMPARE_OP               in
         172  POP_JUMP_IF_FALSE   184  'to 184'

 882     174  LOAD_CONST               0
         176  LOAD_FAST                'info'
         178  LOAD_FAST                'name'
         180  STORE_SUBSCR     

 883     182  CONTINUE            158  'to 158'

 885     184  LOAD_FAST                'info'
         186  LOAD_FAST                'name'
         188  BINARY_SUBSCR    
         190  STORE_FAST               'val'

 886     192  LOAD_CONST               0
         194  LOAD_FAST                'val'
         196  DUP_TOP          
         198  ROT_THREE        
         200  COMPARE_OP               <=
         202  POP_JUMP_IF_FALSE   220  'to 220'
         204  LOAD_CONST               8
         206  LOAD_FAST                'digits'
         208  LOAD_CONST               1
         210  BINARY_SUBTRACT  
         212  BINARY_POWER     
         214  COMPARE_OP               <
         216  POP_JUMP_IF_FALSE   234  'to 234'
         218  JUMP_FORWARD        224  'to 224'
         220  ELSE                     '224'
         220  POP_TOP          
         222  JUMP_FORWARD        234  'to 234'
       224_0  COME_FROM           218  '218'
         224  LOAD_GLOBAL              isinstance
         226  LOAD_FAST                'val'
         228  LOAD_GLOBAL              float
         230  CALL_FUNCTION_2       2  ''
       232_0  COME_FROM           216  '216'
         232  POP_JUMP_IF_FALSE   158  'to 158'
       234_0  COME_FROM           222  '222'

 887     234  LOAD_GLOBAL              str
         236  LOAD_FAST                'val'
         238  CALL_FUNCTION_1       1  ''
         240  LOAD_FAST                'pax_headers'
         242  LOAD_FAST                'name'
         244  STORE_SUBSCR     

 888     246  LOAD_CONST               0
         248  LOAD_FAST                'info'
         250  LOAD_FAST                'name'
         252  STORE_SUBSCR     
         254  JUMP_BACK           158  'to 158'
         256  POP_BLOCK        
       258_0  COME_FROM_LOOP      152  '152'

 891     258  LOAD_FAST                'pax_headers'
         260  POP_JUMP_IF_FALSE   280  'to 280'

 892     264  LOAD_FAST                'self'
         266  LOAD_METHOD              _create_pax_generic_header
         268  LOAD_FAST                'pax_headers'
         270  LOAD_GLOBAL              XHDTYPE
         272  LOAD_FAST                'encoding'
         274  CALL_METHOD_3         3  ''
         276  STORE_FAST               'buf'
         278  JUMP_FORWARD        284  'to 284'
         280  ELSE                     '284'

 894     280  LOAD_STR                 ''
         282  STORE_FAST               'buf'
       284_0  COME_FROM           278  '278'

 896     284  LOAD_FAST                'buf'
         286  LOAD_FAST                'self'
         288  LOAD_METHOD              _create_header
         290  LOAD_FAST                'info'
         292  LOAD_GLOBAL              USTAR_FORMAT
         294  LOAD_STR                 'ascii'
         296  LOAD_STR                 'replace'
         298  CALL_METHOD_4         4  ''
         300  BINARY_ADD       
         302  RETURN_VALUE     
          -1  RETURN_LAST      

Parse error at or near `COME_FROM' instruction at offset 232_0

    @classmethod
    def create_pax_global_header(cls, pax_headers):
        """Return the object as a pax global header block sequence.
        """
        return cls._create_pax_generic_header(pax_headers, XGLTYPE, 'utf-8')

    def _posix_split_name(self, name, encoding, errors):
        """Split a name longer than 100 chars into a prefix
           and a name part.
        """
        components = name.split('/')
        for i in range(1, len(components)):
            prefix = '/'.join(components[:i])
            name = '/'.join(components[i:])
            if len(prefix.encode(encoding, errors)) <= LENGTH_PREFIX:
                if len(name.encode(encoding, errors)) <= LENGTH_NAME:
                    break
        else:
            raise ValueError('name is too long')

        return (
         prefix, name)

    @staticmethod
    def _create_header(info, format, encoding, errors):
        """Return a header block. info is a dictionary with file
           information, format must be one of the *_FORMAT constants.
        """
        parts = [
         stn(info.get('name', ''), 100, encoding, errors),
         itn(info.get('mode', 0) & 4095, 8, format),
         itn(info.get('uid', 0), 8, format),
         itn(info.get('gid', 0), 8, format),
         itn(info.get('size', 0), 12, format),
         itn(info.get('mtime', 0), 12, format),
         '        ',
         info.get('type', REGTYPE),
         stn(info.get('linkname', ''), 100, encoding, errors),
         info.get('magic', POSIX_MAGIC),
         stn(info.get('uname', ''), 32, encoding, errors),
         stn(info.get('gname', ''), 32, encoding, errors),
         itn(info.get('devmajor', 0), 8, format),
         itn(info.get('devminor', 0), 8, format),
         stn(info.get('prefix', ''), 155, encoding, errors)]
        buf = struct.pack('%ds' % BLOCKSIZE, ''.join(parts))
        chksum = calc_chksums(buf[-BLOCKSIZE:])[0]
        buf = buf[:-364] + bytes('%06o\x00' % chksum, 'ascii') + buf[-357:]
        return buf

    @staticmethod
    def _create_payload(payload):
        """Return the string payload filled with zero bytes
           up to the next 512 byte border.
        """
        blocks, remainder = divmod(len(payload), BLOCKSIZE)
        if remainder > 0:
            payload += (BLOCKSIZE - remainder) * NUL
        return payload

    @classmethod
    def _create_gnu_long_header(cls, name, type, encoding, errors):
        """Return a GNUTYPE_LONGNAME or GNUTYPE_LONGLINK sequence
           for name.
        """
        name = name.encode(encoding, errors) + NUL
        info = {}
        info['name'] = '././@LongLink'
        info['type'] = type
        info['size'] = len(name)
        info['magic'] = GNU_MAGIC
        return cls._create_header(info, USTAR_FORMAT, encoding, errors) + cls._create_payload(name)

    @classmethod
    def _create_pax_generic_header(cls, pax_headers, type, encoding):
        """Return a POSIX.1-2008 extended or global header sequence
           that contains a list of keyword, value pairs. The values
           must be strings.
        """
        binary = False
        for keyword, value in pax_headers.items():
            try:
                value.encode('utf-8', 'strict')
            except UnicodeEncodeError:
                binary = True
                break

        records = ''
        if binary:
            records += '21 hdrcharset=BINARY\n'
        for keyword, value in pax_headers.items():
            keyword = keyword.encode('utf-8')
            if binary:
                value = value.encode(encoding, 'surrogateescape')
            else:
                value = value.encode('utf-8')
            l = len(keyword) + len(value) + 3
            n = p = 0
            while True:
                n = l + len(str(p))
                if n == p:
                    break
                p = n

            records += bytes(str(p), 'ascii') + ' ' + keyword + '=' + value + '\n'

        info = {}
        info['name'] = '././@PaxHeader'
        info['type'] = type
        info['size'] = len(records)
        info['magic'] = POSIX_MAGIC
        return cls._create_header(info, USTAR_FORMAT, 'ascii', 'replace') + cls._create_payload(records)

    @classmethod
    def frombuf(cls, buf, encoding, errors):
        """Construct a TarInfo object from a 512 byte bytes object.
        """
        if len(buf) == 0:
            raise EmptyHeaderError('empty header')
        if len(buf) != BLOCKSIZE:
            raise TruncatedHeaderError('truncated header')
        if buf.count(NUL) == BLOCKSIZE:
            raise EOFHeaderError('end of file header')
        chksum = nti(buf[148:156])
        if chksum not in calc_chksums(buf):
            raise InvalidHeaderError('bad checksum')
        obj = cls()
        obj.name = nts(buf[0:100], encoding, errors)
        obj.mode = nti(buf[100:108])
        obj.uid = nti(buf[108:116])
        obj.gid = nti(buf[116:124])
        obj.size = nti(buf[124:136])
        obj.mtime = nti(buf[136:148])
        obj.chksum = chksum
        obj.type = buf[156:157]
        obj.linkname = nts(buf[157:257], encoding, errors)
        obj.uname = nts(buf[265:297], encoding, errors)
        obj.gname = nts(buf[297:329], encoding, errors)
        obj.devmajor = nti(buf[329:337])
        obj.devminor = nti(buf[337:345])
        prefix = nts(buf[345:500], encoding, errors)
        if obj.type == AREGTYPE:
            if obj.name.endswith('/'):
                obj.type = DIRTYPE
            if obj.type == GNUTYPE_SPARSE:
                pos = 386
                structs = []
                for i in range(4):
                    try:
                        offset = nti(buf[pos:pos + 12])
                        numbytes = nti(buf[pos + 12:pos + 24])
                    except ValueError:
                        break

                    structs.append((offset, numbytes))
                    pos += 24

                isextended = bool(buf[482])
                origsize = nti(buf[483:495])
                obj._sparse_structs = (structs, isextended, origsize)
            if obj.isdir():
                obj.name = obj.name.rstrip('/')
        if prefix:
            if obj.type not in GNU_TYPES:
                obj.name = prefix + '/' + obj.name
            return obj

    @classmethod
    def fromtarfile(cls, tarfile):
        """Return the next TarInfo object from TarFile object
           tarfile.
        """
        buf = tarfile.fileobj.read(BLOCKSIZE)
        obj = cls.frombuf(buf, tarfile.encoding, tarfile.errors)
        obj.offset = tarfile.fileobj.tell() - BLOCKSIZE
        return obj._proc_member(tarfile)

    def _proc_member(self, tarfile):
        """Choose the right processing method depending on
           the type and call it.
        """
        if self.type in (GNUTYPE_LONGNAME, GNUTYPE_LONGLINK):
            return self._proc_gnulong(tarfile)
        elif self.type == GNUTYPE_SPARSE:
            return self._proc_sparse(tarfile)
        elif self.type in (XHDTYPE, XGLTYPE, SOLARIS_XHDTYPE):
            return self._proc_pax(tarfile)
        else:
            return self._proc_builtin(tarfile)

    def _proc_builtin(self, tarfile):
        """Process a builtin type or an unknown type which
           will be treated as a regular file.
        """
        self.offset_data = tarfile.fileobj.tell()
        offset = self.offset_data
        if self.isreg() or self.type not in SUPPORTED_TYPES:
            offset += self._block(self.size)
        tarfile.offset = offset
        self._apply_pax_info(tarfile.pax_headers, tarfile.encoding, tarfile.errors)
        return self

    def _proc_gnulong(self, tarfile):
        """Process the blocks that hold a GNU longname
           or longlink member.
        """
        buf = tarfile.fileobj.read(self._block(self.size))
        try:
            next = self.fromtarfile(tarfile)
        except HeaderError:
            raise SubsequentHeaderError('missing or bad subsequent header')

        next.offset = self.offset
        if self.type == GNUTYPE_LONGNAME:
            next.name = nts(buf, tarfile.encoding, tarfile.errors)
        elif self.type == GNUTYPE_LONGLINK:
            next.linkname = nts(buf, tarfile.encoding, tarfile.errors)
        else:
            return next

    def _proc_sparse(self, tarfile):
        """Process a GNU sparse header plus extra headers.
        """
        structs, isextended, origsize = self._sparse_structs
        del self._sparse_structs
        while 1:
            if isextended:
                buf = tarfile.fileobj.read(BLOCKSIZE)
                pos = 0
                for i in range(21):
                    try:
                        offset = nti(buf[pos:pos + 12])
                        numbytes = nti(buf[pos + 12:pos + 24])
                    except ValueError:
                        break

                    if offset:
                        if numbytes:
                            structs.append((offset, numbytes))
                        pos += 24

                isextended = bool(buf[504])

        self.sparse = structs
        self.offset_data = tarfile.fileobj.tell()
        tarfile.offset = self.offset_data + self._block(self.size)
        self.size = origsize
        return self

    def _proc_pax(self, tarfile):
        """Process an extended or global header as described in
           POSIX.1-2008.
        """
        buf = tarfile.fileobj.read(self._block(self.size))
        if self.type == XGLTYPE:
            pax_headers = tarfile.pax_headers
        else:
            pax_headers = tarfile.pax_headers.copy()
        match = re.search('\\d+ hdrcharset=([^\\n]+)\\n', buf)
        if match is not None:
            pax_headers['hdrcharset'] = match.group(1).decode('utf-8')
        hdrcharset = pax_headers.get('hdrcharset')
        if hdrcharset == 'BINARY':
            encoding = tarfile.encoding
        else:
            encoding = 'utf-8'
        regex = re.compile('(\\d+) ([^=]+)=')
        pos = 0
        while True:
            match = regex.match(buf, pos)
            if not match:
                break
            length, keyword = match.groups()
            length = int(length)
            value = buf[match.end(2) + 1:match.start(1) + length - 1]
            keyword = self._decode_pax_field(keyword, 'utf-8', 'utf-8', tarfile.errors)
            if keyword in PAX_NAME_FIELDS:
                value = self._decode_pax_field(value, encoding, tarfile.encoding, tarfile.errors)
            else:
                value = self._decode_pax_field(value, 'utf-8', 'utf-8', tarfile.errors)
            pax_headers[keyword] = value
            pos += length

        try:
            next = self.fromtarfile(tarfile)
        except HeaderError:
            raise SubsequentHeaderError('missing or bad subsequent header')

        if 'GNU.sparse.map' in pax_headers:
            self._proc_gnusparse_01(next, pax_headers)
        elif 'GNU.sparse.size' in pax_headers:
            self._proc_gnusparse_00(next, pax_headers, buf)
        elif pax_headers.get('GNU.sparse.major') == '1':
            pass
        if pax_headers.get('GNU.sparse.minor') == '0':
            self._proc_gnusparse_10(next, pax_headers, tarfile)
        if self.type in (XHDTYPE, SOLARIS_XHDTYPE):
            next._apply_pax_info(pax_headers, tarfile.encoding, tarfile.errors)
            next.offset = self.offset
            if 'size' in pax_headers:
                offset = next.offset_data
                if next.isreg() or next.type not in SUPPORTED_TYPES:
                    offset += next._block(next.size)
                tarfile.offset = offset
            return next

    def _proc_gnusparse_00(self, next, pax_headers, buf):
        """Process a GNU tar extended sparse header, version 0.0.
        """
        offsets = []
        for match in re.finditer('\\d+ GNU.sparse.offset=(\\d+)\\n', buf):
            offsets.append(int(match.group(1)))

        numbytes = []
        for match in re.finditer('\\d+ GNU.sparse.numbytes=(\\d+)\\n', buf):
            numbytes.append(int(match.group(1)))

        next.sparse = list(zip(offsets, numbytes))

    def _proc_gnusparse_01(self, next, pax_headers):
        """Process a GNU tar extended sparse header, version 0.1.
        """
        sparse = [int(x) for x in pax_headers['GNU.sparse.map'].split(',')]
        next.sparse = list(zip(sparse[::2], sparse[1::2]))

    def _proc_gnusparse_10(self, next, pax_headers, tarfile):
        """Process a GNU tar extended sparse header, version 1.0.
        """
        fields = None
        sparse = []
        buf = tarfile.fileobj.read(BLOCKSIZE)
        fields, buf = buf.split('\n', 1)
        fields = int(fields)
        while 1:
            if len(sparse) < fields * 2:
                if '\n' not in buf:
                    buf += tarfile.fileobj.read(BLOCKSIZE)
                number, buf = buf.split('\n', 1)
                sparse.append(int(number))

        next.offset_data = tarfile.fileobj.tell()
        next.sparse = list(zip(sparse[::2], sparse[1::2]))

    def _apply_pax_info(self, pax_headers, encoding, errors):
        """Replace fields with supplemental information from a previous
           pax extended or global header.
        """
        for keyword, value in pax_headers.items():
            if keyword == 'GNU.sparse.name':
                setattr(self, 'path', value)
            elif keyword == 'GNU.sparse.size':
                setattr(self, 'size', int(value))
            elif keyword == 'GNU.sparse.realsize':
                setattr(self, 'size', int(value))
            else:
                if keyword in PAX_FIELDS:
                    pass
                if keyword in PAX_NUMBER_FIELDS:
                    try:
                        value = PAX_NUMBER_FIELDS[keyword](value)
                    except ValueError:
                        value = 0

                    if keyword == 'path':
                        value = value.rstrip('/')
                    setattr(self, keyword, value)

        self.pax_headers = pax_headers.copy()

    def _decode_pax_field(self, value, encoding, fallback_encoding, fallback_errors):
        """Decode a single field from a pax record.
        """
        try:
            return value.decode(encoding, 'strict')
        except UnicodeDecodeError:
            return value.decode(fallback_encoding, fallback_errors)

    def _block(self, count):
        """Round up a byte count by BLOCKSIZE and return it,
           e.g. _block(834) => 1024.
        """
        blocks, remainder = divmod(count, BLOCKSIZE)
        if remainder:
            blocks += 1
        return blocks * BLOCKSIZE

    def isreg(self):
        return self.type in REGULAR_TYPES

    def isfile(self):
        return self.isreg()

    def isdir(self):
        return self.type == DIRTYPE

    def issym(self):
        return self.type == SYMTYPE

    def islnk(self):
        return self.type == LNKTYPE

    def ischr(self):
        return self.type == CHRTYPE

    def isblk(self):
        return self.type == BLKTYPE

    def isfifo(self):
        return self.type == FIFOTYPE

    def issparse(self):
        return self.sparse is not None

    def isdev(self):
        return self.type in (CHRTYPE, BLKTYPE, FIFOTYPE)


class TarFile(object):
    r"""'The TarFile Class provides an interface to tar archives.\n    '"""
    debug = 0
    dereference = False
    ignore_zeros = False
    errorlevel = 1
    format = DEFAULT_FORMAT
    encoding = ENCODING
    errors = None
    tarinfo = TarInfo
    fileobject = ExFileObject

    def __init__(self, name=None, mode='r', fileobj=None, format=None, tarinfo=None, dereference=None, ignore_zeros=None, encoding=None, errors='surrogateescape', pax_headers=None, debug=None, errorlevel=None, copybufsize=None):
        """Open an (uncompressed) tar archive `name'. `mode' is either 'r' to
           read from an existing archive, 'a' to append data to an existing
           file or 'w' to create a new file overwriting an existing one. `mode'
           defaults to 'r'.
           If `fileobj' is given, it is used for reading or writing data. If it
           can be determined, `mode' is overridden by `fileobj's mode.
           `fileobj' is not closed, when TarFile is closed.
        """
        modes = {'r':'rb', 
         'a':'r+b',  'w':'wb',  'x':'xb'}
        if mode not in modes:
            raise ValueError("mode must be 'r', 'a', 'w' or 'x'")
        self.mode = mode
        self._mode = modes[mode]
        if not fileobj:
            if self.mode == 'a':
                if not os.path.exists(name):
                    self.mode = 'w'
                    self._mode = 'wb'
                fileobj = bltn_open(name, self._mode)
                self._extfileobj = False
        if name is None:
            if hasattr(fileobj, 'name'):
                if isinstance(fileobj.name, (str, bytes)):
                    name = fileobj.name
                if hasattr(fileobj, 'mode'):
                    self._mode = fileobj.mode
                self._extfileobj = True
            self.name = os.path.abspath(name) if name else None
            self.fileobj = fileobj
            if format is not None:
                self.format = format
            if tarinfo is not None:
                self.tarinfo = tarinfo
            if dereference is not None:
                self.dereference = dereference
            if ignore_zeros is not None:
                self.ignore_zeros = ignore_zeros
            if encoding is not None:
                self.encoding = encoding
            self.errors = errors
        if pax_headers is not None:
            if self.format == PAX_FORMAT:
                self.pax_headers = pax_headers
            else:
                self.pax_headers = {}
            if debug is not None:
                self.debug = debug
            if errorlevel is not None:
                self.errorlevel = errorlevel
            self.copybufsize = copybufsize
            self.closed = False
            self.members = []
            self._loaded = False
            self.offset = self.fileobj.tell()
            self.inodes = {}
        try:
            if self.mode == 'r':
                self.firstmember = None
                self.firstmember = self.next()
            if self.mode == 'a':
                while 1:
                    self.fileobj.seek(self.offset)
                    try:
                        tarinfo = self.tarinfo.fromtarfile(self)
                        self.members.append(tarinfo)
                    except EOFHeaderError:
                        self.fileobj.seek(self.offset)
                        break
                    except HeaderError as e:
                        try:
                            raise ReadError(str(e))
                        finally:
                            e = None
                            del e

            self._loaded = self.mode in ('a', 'w', 'x') and True
            if self.pax_headers:
                buf = self.tarinfo.create_pax_global_header(self.pax_headers.copy())
                self.fileobj.write(buf)
                self.offset += len(buf)
        except:
            if not self._extfileobj:
                self.fileobj.close()
            self.closed = True
            raise

    @classmethod
    def open(cls, name=None, mode='r', fileobj=None, bufsize=RECORDSIZE, **kwargs):
        """Open a tar archive for reading, writing or appending. Return
           an appropriate TarFile class.

           mode:
           'r' or 'r:*' open for reading with transparent compression
           'r:'         open for reading exclusively uncompressed
           'r:gz'       open for reading with gzip compression
           'r:bz2'      open for reading with bzip2 compression
           'r:xz'       open for reading with lzma compression
           'a' or 'a:'  open for appending, creating the file if necessary
           'w' or 'w:'  open for writing without compression
           'w:gz'       open for writing with gzip compression
           'w:bz2'      open for writing with bzip2 compression
           'w:xz'       open for writing with lzma compression

           'x' or 'x:'  create a tarfile exclusively without compression, raise
                        an exception if the file is already created
           'x:gz'       create a gzip compressed tarfile, raise an exception
                        if the file is already created
           'x:bz2'      create a bzip2 compressed tarfile, raise an exception
                        if the file is already created
           'x:xz'       create an lzma compressed tarfile, raise an exception
                        if the file is already created

           'r|*'        open a stream of tar blocks with transparent compression
           'r|'         open an uncompressed stream of tar blocks for reading
           'r|gz'       open a gzip compressed stream of tar blocks
           'r|bz2'      open a bzip2 compressed stream of tar blocks
           'r|xz'       open an lzma compressed stream of tar blocks
           'w|'         open an uncompressed stream for writing
           'w|gz'       open a gzip compressed stream for writing
           'w|bz2'      open a bzip2 compressed stream for writing
           'w|xz'       open an lzma compressed stream for writing
        """
        if not name:
            if not fileobj:
                raise ValueError('nothing to open')
            if mode in ('r', 'r:*'):

                def not_compressed(comptype):
                    return cls.OPEN_METH[comptype] == 'taropen'

                for comptype in sorted((cls.OPEN_METH), key=not_compressed):
                    func = getattr(cls, cls.OPEN_METH[comptype])
                    if fileobj is not None:
                        saved_pos = fileobj.tell()
                    try:
                        return func(name, 'r', fileobj, **kwargs)
                    except (ReadError, CompressionError):
                        if fileobj is not None:
                            fileobj.seek(saved_pos)
                        continue

                raise ReadError('file could not be opened successfully')
            elif ':' in mode:
                filemode, comptype = mode.split(':', 1)
                filemode = filemode or 'r'
                comptype = comptype or 'tar'
                if comptype in cls.OPEN_METH:
                    func = getattr(cls, cls.OPEN_METH[comptype])
                else:
                    raise CompressionError('unknown compression type %r' % comptype)
                return func(name, filemode, fileobj, **kwargs)
            if '|' in mode:
                filemode, comptype = mode.split('|', 1)
                filemode = filemode or 'r'
                comptype = comptype or 'tar'
                if filemode not in ('r', 'w'):
                    raise ValueError("mode must be 'r' or 'w'")
                stream = _Stream(name, filemode, comptype, fileobj, bufsize)
                try:
                    t = cls(name, filemode, stream, **kwargs)
                except:
                    stream.close()
                    raise

                t._extfileobj = False
                return t
            if mode in ('a', 'w', 'x'):
                return (cls.taropen)(name, mode, fileobj, **kwargs)
            raise ValueError('undiscernible mode')

    @classmethod
    def taropen(cls, name, mode='r', fileobj=None, **kwargs):
        """Open uncompressed tar archive name for reading or writing.
        """
        if mode not in ('r', 'a', 'w', 'x'):
            raise ValueError("mode must be 'r', 'a', 'w' or 'x'")
        return cls(name, mode, fileobj, **kwargs)

    @classmethod
    def gzopen(cls, name, mode='r', fileobj=None, compresslevel=9, **kwargs):
        """Open gzip compressed tar archive name for reading or writing.
           Appending is not allowed.
        """
        if mode not in ('r', 'w', 'x'):
            raise ValueError("mode must be 'r', 'w' or 'x'")
        try:
            import gzip
            gzip.GzipFile
        except (ImportError, AttributeError):
            raise CompressionError('gzip module is not available')

        try:
            fileobj = gzip.GzipFile(name, mode + 'b', compresslevel, fileobj)
        except OSError:
            if fileobj is not None:
                if mode == 'r':
                    raise ReadError('not a gzip file')
                raise

        try:
            t = (cls.taropen)(name, mode, fileobj, **kwargs)
        except OSError:
            fileobj.close()
            if mode == 'r':
                raise ReadError('not a gzip file')
            raise
        except:
            fileobj.close()
            raise

        t._extfileobj = False
        return t

    @classmethod
    def bz2open(cls, name, mode='r', fileobj=None, compresslevel=9, **kwargs):
        """Open bzip2 compressed tar archive name for reading or writing.
           Appending is not allowed.
        """
        if mode not in ('r', 'w', 'x'):
            raise ValueError("mode must be 'r', 'w' or 'x'")
        try:
            import bz2
        except ImportError:
            raise CompressionError('bz2 module is not available')

        fileobj = bz2.BZ2File((fileobj or name), mode, compresslevel=compresslevel)
        try:
            t = (cls.taropen)(name, mode, fileobj, **kwargs)
        except (OSError, EOFError):
            fileobj.close()
            if mode == 'r':
                raise ReadError('not a bzip2 file')
            raise
        except:
            fileobj.close()
            raise

        t._extfileobj = False
        return t

    @classmethod
    def xzopen(cls, name, mode='r', fileobj=None, preset=None, **kwargs):
        """Open lzma compressed tar archive name for reading or writing.
           Appending is not allowed.
        """
        if mode not in ('r', 'w', 'x'):
            raise ValueError("mode must be 'r', 'w' or 'x'")
        try:
            import lzma
        except ImportError:
            raise CompressionError('lzma module is not available')

        fileobj = lzma.LZMAFile((fileobj or name), mode, preset=preset)
        try:
            t = (cls.taropen)(name, mode, fileobj, **kwargs)
        except (lzma.LZMAError, EOFError):
            fileobj.close()
            if mode == 'r':
                raise ReadError('not an lzma file')
            raise
        except:
            fileobj.close()
            raise

        t._extfileobj = False
        return t

    OPEN_METH = {'tar':'taropen', 
     'gz':'gzopen', 
     'bz2':'bz2open', 
     'xz':'xzopen'}

    def close(self):
        """Close the TarFile. In write-mode, two finishing zero blocks are
           appended to the archive.
        """
        if self.closed:
            return
        self.closed = True
        try:
            if self.mode in ('a', 'w', 'x'):
                self.fileobj.write(NUL * (BLOCKSIZE * 2))
                self.offset += BLOCKSIZE * 2
                blocks, remainder = divmod(self.offset, RECORDSIZE)
            if remainder > 0:
                self.fileobj.write(NUL * (RECORDSIZE - remainder))
        finally:
            if not self._extfileobj:
                self.fileobj.close()

    def getmember(self, name):
        """Return a TarInfo object for member `name'. If `name' can not be
           found in the archive, KeyError is raised. If a member occurs more
           than once in the archive, its last occurrence is assumed to be the
           most up-to-date version.
        """
        tarinfo = self._getmember(name)
        if tarinfo is None:
            raise KeyError('filename %r not found' % name)
        return tarinfo

    def getmembers(self):
        """Return the members of the archive as a list of TarInfo objects. The
           list has the same order as the members in the archive.
        """
        self._check()
        if not self._loaded:
            self._load()
        return self.members

    def getnames(self):
        """Return the members of the archive as a list of their names. It has
           the same order as the list returned by getmembers().
        """
        return [tarinfo.name for tarinfo in self.getmembers()]

    def gettarinfo(self, name=None, arcname=None, fileobj=None):
        """Create a TarInfo object from the result of os.stat or equivalent
           on an existing file. The file is either named by `name', or
           specified as a file object `fileobj' with a file descriptor. If
           given, `arcname' specifies an alternative name for the file in the
           archive, otherwise, the name is taken from the 'name' attribute of
           'fileobj', or the 'name' argument. The name should be a text
           string.
        """
        self._check('awx')
        if fileobj is not None:
            name = fileobj.name
        if arcname is None:
            arcname = name
        drv, arcname = os.path.splitdrive(arcname)
        arcname = arcname.replace(os.sep, '/')
        arcname = arcname.lstrip('/')
        tarinfo = self.tarinfo()
        tarinfo.tarfile = self
        if fileobj is None:
            if hasattr(os, 'lstat'):
                if not self.dereference:
                    statres = os.lstat(name)
            statres = os.stat(name)
        else:
            statres = os.fstat(fileobj.fileno())
        linkname = ''
        stmd = statres.st_mode
        if stat.S_ISREG(stmd):
            inode = (
             statres.st_ino, statres.st_dev)
            if not self.dereference:
                pass
        if statres.st_nlink > 1:
            if inode in self.inodes:
                if arcname != self.inodes[inode]:
                    type = LNKTYPE
                    linkname = self.inodes[inode]
                else:
                    type = REGTYPE
                    if inode[0]:
                        self.inodes[inode] = arcname
            elif stat.S_ISDIR(stmd):
                type = DIRTYPE
            elif stat.S_ISFIFO(stmd):
                type = FIFOTYPE
            elif stat.S_ISLNK(stmd):
                type = SYMTYPE
                linkname = os.readlink(name)
            elif stat.S_ISCHR(stmd):
                type = CHRTYPE
            elif stat.S_ISBLK(stmd):
                type = BLKTYPE
            else:
                return
            tarinfo.name = arcname
            tarinfo.mode = stmd
            tarinfo.uid = statres.st_uid
            tarinfo.gid = statres.st_gid
            if type == REGTYPE:
                tarinfo.size = statres.st_size
            else:
                tarinfo.size = 0
            tarinfo.mtime = statres.st_mtime
            tarinfo.type = type
            tarinfo.linkname = linkname
            if pwd:
                pass
        try:
            tarinfo.uname = pwd.getpwuid(tarinfo.uid)[0]
        except KeyError:
            pass

        if grp:
            try:
                tarinfo.gname = grp.getgrgid(tarinfo.gid)[0]
            except KeyError:
                pass

            if type in (CHRTYPE, BLKTYPE):
                pass
        if hasattr(os, 'major'):
            if hasattr(os, 'minor'):
                tarinfo.devmajor = os.major(statres.st_rdev)
                tarinfo.devminor = os.minor(statres.st_rdev)
            return tarinfo

    def list(self, verbose=True, *, members=None):
        """Print a table of contents to sys.stdout. If `verbose' is False, only
           the names of the members are printed. If it is True, an `ls -l'-like
           output is produced. `members' is optional and must be a subset of the
           list returned by getmembers().
        """
        self._check()
        if members is None:
            members = self
        for tarinfo in members:
            if verbose:
                _safe_print(stat.filemode(tarinfo.mode))
                _safe_print('%s/%s' % (tarinfo.uname or tarinfo.uid,
                 tarinfo.gname or tarinfo.gid))
                if tarinfo.ischr() or tarinfo.isblk():
                    _safe_print('%10s' % ('%d,%d' % (tarinfo.devmajor, tarinfo.devminor)))
                else:
                    _safe_print('%10d' % tarinfo.size)
                _safe_print('%d-%02d-%02d %02d:%02d:%02d' % time.localtime(tarinfo.mtime)[:6])
            _safe_print(tarinfo.name + ('/' if tarinfo.isdir() else ''))
            if verbose:
                if tarinfo.issym():
                    _safe_print('-> ' + tarinfo.linkname)
                if tarinfo.islnk():
                    _safe_print('link to ' + tarinfo.linkname)
                print()

    def add(self, name, arcname=None, recursive=True, *, filter=None):
        """Add the file `name' to the archive. `name' may be any type of file
           (directory, fifo, symbolic link, etc.). If given, `arcname'
           specifies an alternative name for the file in the archive.
           Directories are added recursively by default. This can be avoided by
           setting `recursive' to False. `filter' is a function
           that expects a TarInfo object argument and returns the changed
           TarInfo object, if it returns None the TarInfo object will be
           excluded from the archive.
        """
        self._check('awx')
        if arcname is None:
            arcname = name
        if self.name is not None:
            if os.path.abspath(name) == self.name:
                self._dbg(2, 'tarfile: Skipped %r' % name)
                return
            self._dbg(1, name)
            tarinfo = self.gettarinfo(name, arcname)
            if tarinfo is None:
                self._dbg(1, 'tarfile: Unsupported type %r' % name)
                return
        if filter is not None:
            tarinfo = filter(tarinfo)
            if tarinfo is None:
                self._dbg(2, 'tarfile: Excluded %r' % name)
                return
            if tarinfo.isreg():
                with bltn_open(name, 'rb') as (f):
                    self.addfile(tarinfo, f)
        if tarinfo.isdir():
            self.addfile(tarinfo)
            if recursive:
                for f in sorted(os.listdir(name)):
                    self.add((os.path.join(name, f)), (os.path.join(arcname, f)), recursive,
                      filter=filter)

            else:
                self.addfile(tarinfo)

    def addfile(self, tarinfo, fileobj=None):
        """Add the TarInfo object `tarinfo' to the archive. If `fileobj' is
           given, it should be a binary file, and tarinfo.size bytes are read
           from it and added to the archive. You can create TarInfo objects
           directly, or by using gettarinfo().
        """
        self._check('awx')
        tarinfo = copy.copy(tarinfo)
        buf = tarinfo.tobuf(self.format, self.encoding, self.errors)
        self.fileobj.write(buf)
        self.offset += len(buf)
        bufsize = self.copybufsize
        if fileobj is not None:
            copyfileobj(fileobj, (self.fileobj), (tarinfo.size), bufsize=bufsize)
            blocks, remainder = divmod(tarinfo.size, BLOCKSIZE)
            if remainder > 0:
                self.fileobj.write(NUL * (BLOCKSIZE - remainder))
                blocks += 1
            self.offset += blocks * BLOCKSIZE
        self.members.append(tarinfo)

    def extractall(self, path='.', members=None, *, numeric_owner=False):
        """Extract all members from the archive to the current working
           directory and set owner, modification time and permissions on
           directories afterwards. `path' specifies a different directory
           to extract to. `members' is optional and must be a subset of the
           list returned by getmembers(). If `numeric_owner` is True, only
           the numbers for user/group names are used and not the names.
        """
        directories = []
        if members is None:
            members = self
        for tarinfo in members:
            if tarinfo.isdir():
                directories.append(tarinfo)
                tarinfo = copy.copy(tarinfo)
                tarinfo.mode = 448
            self.extract(tarinfo, path, set_attrs=(not tarinfo.isdir()), numeric_owner=numeric_owner)

        directories.sort(key=(lambda a: a.name))
        directories.reverse()
        for tarinfo in directories:
            dirpath = os.path.join(path, tarinfo.name)
            try:
                self.chown(tarinfo, dirpath, numeric_owner=numeric_owner)
                self.utime(tarinfo, dirpath)
                self.chmod(tarinfo, dirpath)
            except ExtractError as e:
                try:
                    if self.errorlevel > 1:
                        raise
                    else:
                        self._dbg(1, 'tarfile: %s' % e)
                finally:
                    e = None
                    del e

    def extract(self, member, path='', set_attrs=True, *, numeric_owner=False):
        """Extract a member from the archive to the current working directory,
           using its full name. Its file information is extracted as accurately
           as possible. `member' may be a filename or a TarInfo object. You can
           specify a different directory using `path'. File attributes (owner,
           mtime, mode) are set unless `set_attrs' is False. If `numeric_owner`
           is True, only the numbers for user/group names are used and not
           the names.
        """
        self._check('r')
        if isinstance(member, str):
            tarinfo = self.getmember(member)
        else:
            tarinfo = member
        if tarinfo.islnk():
            tarinfo._link_target = os.path.join(path, tarinfo.linkname)
        try:
            self._extract_member(tarinfo, (os.path.join(path, tarinfo.name)), set_attrs=set_attrs,
              numeric_owner=numeric_owner)
        except OSError as e:
            try:
                if self.errorlevel > 0:
                    raise
                elif e.filename is None:
                    self._dbg(1, 'tarfile: %s' % e.strerror)
                else:
                    self._dbg(1, 'tarfile: %s %r' % (e.strerror, e.filename))
            finally:
                e = None
                del e

        except ExtractError as e:
            try:
                if self.errorlevel > 1:
                    raise
                else:
                    self._dbg(1, 'tarfile: %s' % e)
            finally:
                e = None
                del e

    def extractfile(self, member):
        """Extract a member from the archive as a file object. `member' may be
           a filename or a TarInfo object. If `member' is a regular file or a
           link, an io.BufferedReader object is returned. Otherwise, None is
           returned.
        """
        self._check('r')
        if isinstance(member, str):
            tarinfo = self.getmember(member)
        else:
            tarinfo = member
        if tarinfo.isreg() or tarinfo.type not in SUPPORTED_TYPES:
            return self.fileobject(self, tarinfo)
        if tarinfo.islnk() or tarinfo.issym():
            if isinstance(self.fileobj, _Stream):
                raise StreamError('cannot extract (sym)link as file object')
            else:
                return self.extractfile(self._find_link_target(tarinfo))
        else:
            return

    def _extract_member(self, tarinfo, targetpath, set_attrs=True, numeric_owner=False):
        """Extract the TarInfo object tarinfo to a physical
           file called targetpath.
        """
        targetpath = targetpath.rstrip('/')
        targetpath = targetpath.replace('/', os.sep)
        upperdirs = os.path.dirname(targetpath)
        if upperdirs:
            if not os.path.exists(upperdirs):
                os.makedirs(upperdirs)
            if tarinfo.islnk() or tarinfo.issym():
                self._dbg(1, '%s -> %s' % (tarinfo.name, tarinfo.linkname))
            else:
                self._dbg(1, tarinfo.name)
            if tarinfo.isreg():
                self.makefile(tarinfo, targetpath)
            elif tarinfo.isdir():
                self.makedir(tarinfo, targetpath)
            elif tarinfo.isfifo():
                self.makefifo(tarinfo, targetpath)
            elif tarinfo.ischr() or tarinfo.isblk():
                self.makedev(tarinfo, targetpath)
            elif tarinfo.islnk() or tarinfo.issym():
                self.makelink(tarinfo, targetpath)
            elif tarinfo.type not in SUPPORTED_TYPES:
                self.makeunknown(tarinfo, targetpath)
            else:
                self.makefile(tarinfo, targetpath)
            if set_attrs:
                self.chown(tarinfo, targetpath, numeric_owner)
        if not tarinfo.issym():
            self.chmod(tarinfo, targetpath)
            self.utime(tarinfo, targetpath)

    def makedir(self, tarinfo, targetpath):
        """Make a directory called targetpath.
        """
        try:
            os.mkdir(targetpath, 448)
        except FileExistsError:
            pass

    def makefile(self, tarinfo, targetpath):
        """Make a file called targetpath.
        """
        source = self.fileobj
        source.seek(tarinfo.offset_data)
        bufsize = self.copybufsize
        with bltn_open(targetpath, 'wb') as (target):
            if tarinfo.sparse is not None:
                for offset, size in tarinfo.sparse:
                    target.seek(offset)
                    copyfileobj(source, target, size, ReadError, bufsize)

                target.seek(tarinfo.size)
                target.truncate()
            else:
                copyfileobj(source, target, tarinfo.size, ReadError, bufsize)

    def makeunknown(self, tarinfo, targetpath):
        """Make a file from a TarInfo object with an unknown type
           at targetpath.
        """
        self.makefile(tarinfo, targetpath)
        self._dbg(1, 'tarfile: Unknown file type %r, extracted as regular file.' % tarinfo.type)

    def makefifo(self, tarinfo, targetpath):
        """Make a fifo called targetpath.
        """
        if hasattr(os, 'mkfifo'):
            os.mkfifo(targetpath)
        else:
            raise ExtractError('fifo not supported by system')

    def makedev(self, tarinfo, targetpath):
        """Make a character or block device called targetpath.
        """
        if not (hasattr(os, 'mknod') and hasattr(os, 'makedev')):
            raise ExtractError('special devices not supported by system')
        mode = tarinfo.mode
        if tarinfo.isblk():
            mode |= stat.S_IFBLK
        else:
            mode |= stat.S_IFCHR
        os.mknod(targetpath, mode, os.makedev(tarinfo.devmajor, tarinfo.devminor))

    def makelink(self, tarinfo, targetpath):
        """Make a (symbolic) link called targetpath. If it cannot be created
          (platform limitation), we try to make a copy of the referenced file
          instead of a link.
        """
        try:
            if tarinfo.issym():
                os.symlink(tarinfo.linkname, targetpath)
            elif os.path.exists(tarinfo._link_target):
                os.link(tarinfo._link_target, targetpath)
            else:
                self._extract_member(self._find_link_target(tarinfo), targetpath)
        except symlink_exception:
            try:
                self._extract_member(self._find_link_target(tarinfo), targetpath)
            except KeyError:
                raise ExtractError('unable to resolve link inside archive')

    def chown(self, tarinfo, targetpath, numeric_owner):
        """Set owner of targetpath according to tarinfo. If numeric_owner
           is True, use .gid/.uid instead of .gname/.uname. If numeric_owner
           is False, fall back to .gid/.uid when the search based on name
           fails.
        """
        if hasattr(os, 'geteuid') and os.geteuid() == 0:
            g = tarinfo.gid
            u = tarinfo.uid
            if not numeric_owner:
                pass
            try:
                if grp:
                    g = grp.getgrnam(tarinfo.gname)[2]
            except KeyError:
                pass

        try:
            if pwd:
                u = pwd.getpwnam(tarinfo.uname)[2]
        except KeyError:
            pass

        try:
            if tarinfo.issym():
                pass
            if hasattr(os, 'lchown'):
                os.lchown(targetpath, u, g)
            else:
                os.chown(targetpath, u, g)
        except OSError:
            raise ExtractError('could not change owner')

    def chmod(self, tarinfo, targetpath):
        """Set file permissions of targetpath according to tarinfo.
        """
        if hasattr(os, 'chmod'):
            pass
        try:
            os.chmod(targetpath, tarinfo.mode)
        except OSError:
            raise ExtractError('could not change mode')

    def utime(self, tarinfo, targetpath):
        """Set modification time of targetpath according to tarinfo.
        """
        if not hasattr(os, 'utime'):
            return
        try:
            os.utime(targetpath, (tarinfo.mtime, tarinfo.mtime))
        except OSError:
            raise ExtractError('could not change modification time')

    def next(self):
        """Return the next member of the archive as a TarInfo object, when
           TarFile is opened for reading. Return None if there is no more
           available.
        """
        self._check('ra')
        if self.firstmember is not None:
            m = self.firstmember
            self.firstmember = None
            return m
        if self.offset != self.fileobj.tell():
            self.fileobj.seek(self.offset - 1)
            if not self.fileobj.read(1):
                raise ReadError('unexpected end of data')
            tarinfo = None
            while True:
                try:
                    tarinfo = self.tarinfo.fromtarfile(self)
                except EOFHeaderError as e:
                    try:
                        if self.ignore_zeros:
                            self._dbg(2, '0x%X: %s' % (self.offset, e))
                            self.offset += BLOCKSIZE
                            continue
                    finally:
                        e = None
                        del e

                except InvalidHeaderError as e:
                    try:
                        if self.ignore_zeros:
                            self._dbg(2, '0x%X: %s' % (self.offset, e))
                            self.offset += BLOCKSIZE
                            continue
                        elif self.offset == 0:
                            raise ReadError(str(e))
                    finally:
                        e = None
                        del e

                except EmptyHeaderError:
                    if self.offset == 0:
                        raise ReadError('empty file')
                except TruncatedHeaderError as e:
                    try:
                        if self.offset == 0:
                            raise ReadError(str(e))
                    finally:
                        e = None
                        del e

                except SubsequentHeaderError as e:
                    try:
                        raise ReadError(str(e))
                    finally:
                        e = None
                        del e

                break

            if tarinfo is not None:
                self.members.append(tarinfo)
            else:
                self._loaded = True
            return tarinfo

    def _getmember(self, name, tarinfo=None, normalize=False):
        """Find an archive member by name from bottom to top.
           If tarinfo is given, it is used as the starting point.
        """
        members = self.getmembers()
        if tarinfo is not None:
            members = members[:members.index(tarinfo)]
        if normalize:
            name = os.path.normpath(name)
        for member in reversed(members):
            if normalize:
                member_name = os.path.normpath(member.name)
            else:
                member_name = member.name
            if name == member_name:
                return member

    def _load(self):
        """Read through the entire archive file and look for readable
           members.
        """
        while 1:
            tarinfo = self.next()
            if tarinfo is None:
                break

        self._loaded = True

    def _check(self, mode=None):
        """Check if TarFile is still open, and if the operation's mode
           corresponds to TarFile's mode.
        """
        if self.closed:
            raise OSError('%s is closed' % self.__class__.__name__)
        if mode is not None:
            pass
        if self.mode not in mode:
            raise OSError('bad operation for mode %r' % self.mode)

    def _find_link_target(self, tarinfo):
        """Find the target member of a symlink or hardlink member in the
           archive.
        """
        if tarinfo.issym():
            linkname = '/'.join(filter(None, (os.path.dirname(tarinfo.name), tarinfo.linkname)))
            limit = None
        else:
            linkname = tarinfo.linkname
            limit = tarinfo
        member = self._getmember(linkname, tarinfo=limit, normalize=True)
        if member is None:
            raise KeyError('linkname %r not found' % linkname)
        return member

    def __iter__(self):
        """Provide an iterator object.
        """
        if self._loaded:
            yield from self.members
            return
        index = 0
        if self.firstmember is not None:
            tarinfo = self.next()
            index += 1
            yield tarinfo
        while True:
            if index < len(self.members):
                tarinfo = self.members[index]
            else:
                if not self._loaded:
                    tarinfo = self.next()
                    if not tarinfo:
                        self._loaded = True
                        return
                else:
                    return
                index += 1
                yield tarinfo

    def _dbg(self, level, msg):
        """Write debugging output to sys.stderr.
        """
        if level <= self.debug:
            print(msg, file=(sys.stderr))

    def __enter__(self):
        self._check()
        return self

    def __exit__(self, type, value, traceback):
        if type is None:
            self.close()
        elif not self._extfileobj:
            self.fileobj.close()
        else:
            self.closed = True


def is_tarfile(name):
    """Return True if name points to a tar archive that we
       are able to handle, else return False.
    """
    try:
        t = open(name)
        t.close()
        return True
    except TarError:
        return False


open = TarFile.open

def main():
    import argparse
    description = 'A simple command-line interface for tarfile module.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose output')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-l', '--list', metavar='<tarfile>', help='Show listing of a tarfile')
    group.add_argument('-e', '--extract', nargs='+', metavar=('<tarfile>', '<output_dir>'),
      help='Extract tarfile into target dir')
    group.add_argument('-c', '--create', nargs='+', metavar=('<name>', '<file>'),
      help='Create tarfile from sources')
    group.add_argument('-t', '--test', metavar='<tarfile>', help='Test if a tarfile is valid')
    args = parser.parse_args()
    src = args.test is not None and args.test
    if is_tarfile(src):
        with open(src, 'r') as (tar):
            tar.getmembers()
            print((tar.getmembers()), file=(sys.stderr))
        if args.verbose:
            print('{!r} is a tar archive.'.format(src))
        else:
            parser.exit(1, '{!r} is not a tar archive.\n'.format(src))
    elif args.list is not None:
        src = args.list
        if is_tarfile(src):
            with TarFile.open(src, 'r:*') as (tf):
                tf.list(verbose=(args.verbose))
        else:
            parser.exit(1, '{!r} is not a tar archive.\n'.format(src))
    elif args.extract is not None:
        if len(args.extract) == 1:
            src = args.extract[0]
            curdir = os.curdir
        elif len(args.extract) == 2:
            src, curdir = args.extract
        else:
            parser.exit(1, parser.format_help())
        if is_tarfile(src):
            with TarFile.open(src, 'r:*') as (tf):
                tf.extractall(path=curdir)
            if args.verbose:
                if curdir == '.':
                    msg = '{!r} file is extracted.'.format(src)
                else:
                    msg = '{!r} file is extracted into {!r} directory.'.format(src, curdir)
                print(msg)
            else:
                parser.exit(1, '{!r} is not a tar archive.\n'.format(src))
    if args.create is not None:
        tar_name = args.create.pop(0)
        _, ext = os.path.splitext(tar_name)
        compressions = {'.gz':'gz', 
         '.tgz':'gz', 
         '.xz':'xz', 
         '.txz':'xz', 
         '.bz2':'bz2', 
         '.tbz':'bz2', 
         '.tbz2':'bz2', 
         '.tb2':'bz2'}
        tar_mode = 'w:' + compressions[ext] if ext in compressions else 'w'
        tar_files = args.create
        with TarFile.open(tar_name, tar_mode) as (tf):
            for file_name in tar_files:
                tf.add(file_name)

    if args.verbose:
        print('{!r} file created.'.format(tar_name))


if __name__ == '__main__':
    main()