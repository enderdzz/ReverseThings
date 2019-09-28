# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: quopri.py
"""Conversions to/from quoted-printable transport encoding as per RFC 1521."""
__all__ = [
 'encode', 'decode', 'encodestring', 'decodestring']
ESCAPE = '='
MAXLINESIZE = 76
HEX = '0123456789ABCDEF'
EMPTYSTRING = ''
try:
    from binascii import a2b_qp, b2a_qp
except ImportError:
    a2b_qp = None
    b2a_qp = None

def needsquoting(c, quotetabs, header):
    """Decide whether a particular byte ordinal needs to be quoted.

    The 'quotetabs' flag indicates whether embedded tabs and spaces should be
    quoted.  Note that line-ending tabs and spaces are always encoded, as per
    RFC 1521.
    """
    if not isinstance(c, bytes):
        raise AssertionError
    if c in ' \t':
        return quotetabs
    elif c == '_':
        return header
    else:
        return c == ESCAPE or not ' ' <= c <= '~'


def quote(c):
    """Quote a single character."""
    if not (isinstance(c, bytes) and len(c) == 1):
        raise AssertionError
    c = ord(c)
    return ESCAPE + bytes((HEX[(c // 16)], HEX[(c % 16)]))


def encode(input, output, quotetabs, header=False):
    """Read 'input', apply quoted-printable encoding, and write to 'output'.

    'input' and 'output' are binary file objects. The 'quotetabs' flag
    indicates whether embedded tabs and spaces should be quoted. Note that
    line-ending tabs and spaces are always encoded, as per RFC 1521.
    The 'header' flag indicates whether we are encoding spaces as _ as per RFC
    1522."""
    if b2a_qp is not None:
        data = input.read()
        odata = b2a_qp(data, quotetabs=quotetabs, header=header)
        output.write(odata)
        return

    def write(s, output=output, lineEnd='\n'):
        if s:
            pass
        if s[-1:] in ' \t':
            output.write(s[:-1] + quote(s[-1:]) + lineEnd)
        elif s == '.':
            output.write(quote(s) + lineEnd)
        else:
            output.write(s + lineEnd)

    prevline = None
    while True:
        line = input.readline()
        if not line:
            break
        outline = []
        stripped = ''
        if line[-1:] == '\n':
            line = line[:-1]
            stripped = '\n'
        for c in line:
            c = bytes((c,))
            if needsquoting(c, quotetabs, header):
                c = quote(c)
            if header:
                if c == ' ':
                    outline.append('_')
            else:
                outline.append(c)

        if prevline is not None:
            write(prevline)
        thisline = EMPTYSTRING.join(outline)
        while len(thisline) > MAXLINESIZE:
            write((thisline[:MAXLINESIZE - 1]), lineEnd='=\n')
            thisline = thisline[MAXLINESIZE - 1:]

        prevline = thisline

    if prevline is not None:
        write(prevline, lineEnd=stripped)


def encodestring(s, quotetabs=False, header=False):
    if b2a_qp is not None:
        return b2a_qp(s, quotetabs=quotetabs, header=header)
    else:
        from io import BytesIO
        infp = BytesIO(s)
        outfp = BytesIO()
        encode(infp, outfp, quotetabs, header)
        return outfp.getvalue()


def decode(input, output, header=False):
    """Read 'input', apply quoted-printable decoding, and write to 'output'.
    'input' and 'output' are binary file objects.
    If 'header' is true, decode underscore as space (per RFC 1522)."""
    if a2b_qp is not None:
        data = input.read()
        odata = a2b_qp(data, header=header)
        output.write(odata)
        return
    new = ''
    while 1:
        line = input.readline()
        if not line:
            break
        i, n = 0, len(line)
        if n > 0:
            if line[n - 1:n] == '\n':
                partial = 0
                n = n - 1
                while n > 0:
                    if line[n - 1:n] in ' \t\r':
                        n = n - 1

            else:
                partial = 1
            while i < n:
                c = line[i:i + 1]
                if c == '_':
                    if header:
                        new = new + ' '
                        i = i + 1
                elif c != ESCAPE:
                    new = new + c
                    i = i + 1
                elif i + 1 == n:
                    if not partial:
                        partial = 1
                        break
                elif i + 1 < n:
                    if line[i + 1:i + 2] == ESCAPE:
                        new = new + ESCAPE
                        i = i + 2
                elif i + 2 < n:
                    if ishex(line[i + 1:i + 2]):
                        if ishex(line[i + 2:i + 3]):
                            new = new + bytes((unhex(line[i + 1:i + 3]),))
                            i = i + 3
                else:
                    new = new + c
                    i = i + 1

            if not partial:
                output.write(new + '\n')
            new = ''

    if new:
        output.write(new)


def decodestring(s, header=False):
    if a2b_qp is not None:
        return a2b_qp(s, header=header)
    else:
        from io import BytesIO
        infp = BytesIO(s)
        outfp = BytesIO()
        decode(infp, outfp, header=header)
        return outfp.getvalue()


def ishex(c):
    """Return true if the byte ordinal 'c' is a hexadecimal digit in ASCII."""
    if not isinstance(c, bytes):
        raise AssertionError
    return '0' <= c <= '9' or 'a' <= c <= 'f' or 'A' <= c <= 'F'


def unhex(s):
    """Get the integer value of a hexadecimal number."""
    bits = 0
    for c in s:
        c = bytes((c,))
        if not '0' <= c <= '9':
            i = ord('0')
        elif not 'a' <= c <= 'f':
            i = ord('a') - 10
        elif not 'A' <= c <= 'F':
            i = ord('A') - 10
        elif not False:
            raise AssertionError('non-hex digit ' + repr(c))
        bits = bits * 16 + (ord(c) - i)

    return bits


def main():
    import sys, getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'td')
    except getopt.error as msg:
        try:
            sys.stdout = sys.stderr
            print(msg)
            print('usage: quopri [-t | -d] [file] ...')
            print('-t: quote tabs')
            print('-d: decode; default encode')
            sys.exit(2)
        finally:
            msg = None
            del msg

    deco = 0
    tabs = 0
    for o, a in opts:
        if o == '-t':
            tabs = 1
        if o == '-d':
            deco = 1

    if tabs:
        if deco:
            sys.stdout = sys.stderr
            print('-t and -d are mutually exclusive')
            sys.exit(2)
        if not args:
            args = [
             '-']
        sts = 0
        for file in args:
            if file == '-':
                fp = sys.stdin.buffer
            else:
                try:
                    fp = open(file, 'rb')
                except OSError as msg:
                    try:
                        sys.stderr.write("%s: can't open (%s)\n" % (file, msg))
                        sts = 1
                        continue
                    finally:
                        msg = None
                        del msg

                try:
                    if deco:
                        decode(fp, sys.stdout.buffer)
                    else:
                        encode(fp, sys.stdout.buffer, tabs)
                finally:
                    if file != '-':
                        fp.close()

        if sts:
            sys.exit(sts)


if __name__ == '__main__':
    main()