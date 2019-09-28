# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: uu.py
"""Implementation of the UUencode and UUdecode functions.

encode(in_file, out_file [,name, mode], *, backtick=False)
decode(in_file [, out_file, mode, quiet])
"""
import binascii, os, sys
__all__ = [
 'Error', 'encode', 'decode']

class Error(Exception):
    pass


def encode(in_file, out_file, name=None, mode=None, *, backtick=False):
    """Uuencode file"""
    opened_files = []
    try:
        if in_file == '-':
            in_file = sys.stdin.buffer
        elif isinstance(in_file, str):
            if name is None:
                name = os.path.basename(in_file)
            if mode is None:
                try:
                    mode = os.stat(in_file).st_mode
                except AttributeError:
                    pass

                in_file = open(in_file, 'rb')
                opened_files.append(in_file)
            if out_file == '-':
                out_file = sys.stdout.buffer
            elif isinstance(out_file, str):
                out_file = open(out_file, 'wb')
                opened_files.append(out_file)
            else:
                if name is None:
                    name = '-'
                if mode is None:
                    mode = 438
                out_file.write(('begin %o %s\n' % (mode & 511, name)).encode('ascii'))
                data = in_file.read(45)
                while len(data) > 0:
                    out_file.write(binascii.b2a_uu(data, backtick=backtick))
                    data = in_file.read(45)

                if backtick:
                    out_file.write('`\nend\n')
                else:
                    out_file.write(' \nend\n')

    finally:
        for f in opened_files:
            f.close()


def decode(in_file, out_file=None, mode=None, quiet=False):
    """Decode uuencoded file"""
    opened_files = []
    if in_file == '-':
        in_file = sys.stdin.buffer
    elif isinstance(in_file, str):
        in_file = open(in_file, 'rb')
        opened_files.append(in_file)
    else:
        try:
            while 1:
                hdr = in_file.readline()
                if not hdr:
                    raise Error('No valid begin line found in input file')
                if not hdr.startswith('begin'):
                    continue
                hdrfields = hdr.split(' ', 2)
                if len(hdrfields) == 3:
                    if hdrfields[0] == 'begin':
                        try:
                            int(hdrfields[1], 8)
                            break
                        except ValueError:
                            pass

            if out_file is None:
                out_file = hdrfields[2].rstrip(' \t\r\n\x0c').decode('ascii')
                if os.path.exists(out_file):
                    raise Error('Cannot overwrite existing file: %s' % out_file)
                if mode is None:
                    mode = int(hdrfields[1], 8)
                out_file = out_file == '-' and sys.stdout.buffer
            elif isinstance(out_file, str):
                fp = open(out_file, 'wb')
                try:
                    os.path.chmod(out_file, mode)
                except AttributeError:
                    pass

                out_file = fp
                opened_files.append(out_file)
            else:
                s = in_file.readline()
                while s and s.strip(' \t\r\n\x0c') != 'end':
                    try:
                        data = binascii.a2b_uu(s)
                    except binascii.Error as v:
                        try:
                            nbytes = ((s[0] - 32 & 63) * 4 + 5) // 3
                            data = binascii.a2b_uu(s[:nbytes])
                            if not quiet:
                                sys.stderr.write('Warning: %s\n' % v)
                        finally:
                            v = None
                            del v

                    out_file.write(data)
                    s = in_file.readline()

                if not s:
                    raise Error('Truncated input file')

        finally:
            for f in opened_files:
                f.close()


def test():
    """uuencode/uudecode main program"""
    import optparse
    parser = optparse.OptionParser(usage='usage: %prog [-d] [-t] [input [output]]')
    parser.add_option('-d', '--decode', dest='decode', help='Decode (instead of encode)?', default=False, action='store_true')
    parser.add_option('-t', '--text', dest='text', help='data is text, encoded format unix-compatible text?', default=False, action='store_true')
    options, args = parser.parse_args()
    if len(args) > 2:
        parser.error('incorrect number of arguments')
        sys.exit(1)
    input = sys.stdin.buffer
    output = sys.stdout.buffer
    if len(args) > 0:
        input = args[0]
    if len(args) > 1:
        output = args[1]
    if options.decode:
        if options.text:
            if isinstance(output, str):
                output = open(output, 'wb')
            else:
                print(sys.argv[0], ': cannot do -t to stdout')
                sys.exit(1)
        decode(input, output)
    elif options.text:
        if isinstance(input, str):
            input = open(input, 'rb')
        else:
            print(sys.argv[0], ': cannot do -t from stdin')
            sys.exit(1)
    else:
        encode(input, output)


if __name__ == '__main__':
    test()