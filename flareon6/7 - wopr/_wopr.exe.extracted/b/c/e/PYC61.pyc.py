# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: shlex.py
"""A lexical analyzer class for simple shell-like syntaxes."""
import os, re, sys
from collections import deque
from io import StringIO
__all__ = [
 'shlex', 'split', 'quote']

class shlex:
    """'A lexical analyzer class for simple shell-like syntaxes.'"""

    def __init__(self, instream=None, infile=None, posix=False, punctuation_chars=False):
        if isinstance(instream, str):
            instream = StringIO(instream)
        if instream is not None:
            self.instream = instream
            self.infile = infile
        else:
            self.instream = sys.stdin
            self.infile = None
        self.posix = posix
        if posix:
            self.eof = None
        else:
            self.eof = ''
        self.commenters = '#'
        self.wordchars = 'abcdfeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
        if self.posix:
            self.wordchars += u'\xdfa\u0300a\u0301a\u0302a\u0303a\u0308a\u030a\xe6c\u0327e\u0300e\u0301e\u0302e\u0308i\u0300i\u0301i\u0302i\u0308\xf0n\u0303o\u0300o\u0301o\u0302o\u0303o\u0308\xf8u\u0300u\u0301u\u0302u\u0308y\u0301\xfey\u0308A\u0300A\u0301A\u0302A\u0303A\u0308A\u030a\xc6C\u0327E\u0300E\u0301E\u0302E\u0308I\u0300I\u0301I\u0302I\u0308\xd0N\u0303O\u0300O\u0301O\u0302O\u0303O\u0308\xd8U\u0300U\u0301U\u0302U\u0308Y\u0301\xde'
        self.whitespace = ' \t\r\n'
        self.whitespace_split = False
        self.quotes = '\'"'
        self.escape = '\\'
        self.escapedquotes = '"'
        self.state = ' '
        self.pushback = deque()
        self.lineno = 1
        self.debug = 0
        self.token = ''
        self.filestack = deque()
        self.source = None
        if not punctuation_chars:
            punctuation_chars = ''
        elif punctuation_chars is True:
            punctuation_chars = '();<>|&'
        else:
            self.punctuation_chars = punctuation_chars
            if punctuation_chars:
                self._pushback_chars = deque()
                self.wordchars += '~-./*?='
                t = self.wordchars.maketrans(dict.fromkeys(punctuation_chars))
                self.wordchars = self.wordchars.translate(t)

    def push_token(self, tok):
        """Push a token onto the stack popped by the get_token method"""
        if self.debug >= 1:
            print('shlex: pushing token ' + repr(tok))
        self.pushback.appendleft(tok)

    def push_source(self, newstream, newfile=None):
        """Push an input source onto the lexer's input source stack."""
        if isinstance(newstream, str):
            newstream = StringIO(newstream)
        self.filestack.appendleft((self.infile, self.instream, self.lineno))
        self.infile = newfile
        self.instream = newstream
        self.lineno = 1
        if self.debug:
            if newfile is not None:
                print('shlex: pushing to file %s' % (self.infile,))
            else:
                print('shlex: pushing to stream %s' % (self.instream,))

    def pop_source(self):
        """Pop the input source stack."""
        self.instream.close()
        self.infile, self.instream, self.lineno = self.filestack.popleft()
        if self.debug:
            print('shlex: popping to %s, line %d' % (
             self.instream, self.lineno))
        self.state = ' '

    def get_token(self):
        """Get a token from the input stream (or from stack if it's nonempty)"""
        if self.pushback:
            tok = self.pushback.popleft()
            if self.debug >= 1:
                print('shlex: popping token ' + repr(tok))
            return tok
        else:
            raw = self.read_token()
            if self.source is not None:
                while 1:
                    if raw == self.source:
                        spec = self.sourcehook(self.read_token())
                        if spec:
                            newfile, newstream = spec
                            self.push_source(newstream, newfile)
                        raw = self.get_token()

            while 1:
                if raw == self.eof:
                    if not self.filestack:
                        return self.eof
                    self.pop_source()
                    raw = self.get_token()

            if self.debug >= 1:
                if raw != self.eof:
                    print('shlex: token=' + repr(raw))
                else:
                    print('shlex: token=EOF')
            return raw

    def read_token(self):
        quoted = False
        escapedstate = ' '
        while 1:
            if self.punctuation_chars:
                if self._pushback_chars:
                    nextchar = self._pushback_chars.pop()
                else:
                    nextchar = self.instream.read(1)
                if nextchar == '\n':
                    self.lineno += 1
                if self.debug >= 3:
                    print('shlex: in state %r I see character: %r' % (self.state,
                     nextchar))
                if self.state is None:
                    self.token = ''
                    break
                elif self.state == ' ':
                    if not nextchar:
                        self.state = None
                        break
                    elif nextchar in self.whitespace:
                        if self.debug >= 2:
                            print('shlex: I see whitespace in whitespace state')
                        if self.token or self.posix and quoted:
                            break
                        else:
                            continue
                    elif nextchar in self.commenters:
                        self.instream.readline()
                        self.lineno += 1
                    elif self.posix:
                        if nextchar in self.escape:
                            escapedstate = 'a'
                            self.state = nextchar
                        elif nextchar in self.wordchars:
                            self.token = nextchar
                            self.state = 'a'
                        elif nextchar in self.punctuation_chars:
                            self.token = nextchar
                            self.state = 'c'
                        elif nextchar in self.quotes:
                            if not self.posix:
                                self.token = nextchar
                            self.state = nextchar
                        elif self.whitespace_split:
                            self.token = nextchar
                            self.state = 'a'
                        else:
                            self.token = nextchar
                            if self.token or self.posix and quoted:
                                break
                            else:
                                continue
                else:
                    if self.state in self.quotes:
                        quoted = True
                        if not nextchar:
                            if self.debug >= 2:
                                print('shlex: I see EOF in quotes state')
                            raise ValueError('No closing quotation')
                        if nextchar == self.state:
                            if not self.posix:
                                self.token += nextchar
                                self.state = ' '
                                break
                            else:
                                self.state = 'a'
                        elif self.posix:
                            pass
                    if nextchar in self.escape:
                        if self.state in self.escapedquotes:
                            escapedstate = self.state
                            self.state = nextchar
                        else:
                            self.token += nextchar
                    else:
                        if self.state in self.escape:
                            if not nextchar:
                                if self.debug >= 2:
                                    print('shlex: I see EOF in escape state')
                                raise ValueError('No escaped character')
                            if escapedstate in self.quotes:
                                pass
                        if nextchar != self.state:
                            if nextchar != escapedstate:
                                self.token += self.state
                            self.token += nextchar
                            self.state = escapedstate
                        elif self.state in ('a', 'c'):
                            if not nextchar:
                                self.state = None
                                break
            elif nextchar in self.whitespace:
                if self.debug >= 2:
                    print('shlex: I see whitespace in word state')
                self.state = ' '
                if self.token or self.posix and quoted:
                    break
                else:
                    continue
            else:
                if nextchar in self.commenters:
                    self.instream.readline()
                    self.lineno += 1
                if self.posix:
                    self.state = ' '
                    if self.token or self.posix and quoted:
                        break
                    else:
                        continue
                elif self.state == 'c':
                    if nextchar in self.punctuation_chars:
                        self.token += nextchar
                    elif nextchar not in self.whitespace:
                        self._pushback_chars.append(nextchar)
                    else:
                        self.state = ' '
                        break

                else:
                    if self.posix:
                        pass
                    if nextchar in self.quotes:
                        self.state = nextchar
                    elif self.posix:
                        if nextchar in self.escape:
                            escapedstate = 'a'
                            self.state = nextchar
                        elif nextchar in self.wordchars or nextchar in self.quotes or self.whitespace_split:
                            self.token += nextchar
                        else:
                            if self.punctuation_chars:
                                self._pushback_chars.append(nextchar)
                            else:
                                self.pushback.appendleft(nextchar)
                            if self.debug >= 2:
                                print('shlex: I see punctuation in word state')
                            self.state = ' '
                            if self.token or self.posix and quoted:
                                break
                        continue

        result = self.token
        self.token = ''
        if self.posix:
            pass
        if not quoted:
            if result == '':
                result = None
            if self.debug > 1:
                if result:
                    print('shlex: raw token=' + repr(result))
                else:
                    print('shlex: raw token=EOF')
            return result

    def sourcehook(self, newfile):
        """Hook called on a filename to be sourced."""
        if newfile[0] == '"':
            newfile = newfile[1:-1]
        if isinstance(self.infile, str):
            if not os.path.isabs(newfile):
                newfile = os.path.join(os.path.dirname(self.infile), newfile)
            return (newfile, open(newfile, 'r'))

    def error_leader(self, infile=None, lineno=None):
        """Emit a C-compiler-like, Emacs-friendly error-message leader."""
        if infile is None:
            infile = self.infile
        if lineno is None:
            lineno = self.lineno
        return '"%s", line %d: ' % (infile, lineno)

    def __iter__(self):
        return self

    def __next__(self):
        token = self.get_token()
        if token == self.eof:
            raise StopIteration
        return token


def split(s, comments=False, posix=True):
    lex = shlex(s, posix=posix)
    lex.whitespace_split = True
    if not comments:
        lex.commenters = ''
    return list(lex)


_find_unsafe = re.compile('[^\\w@%+=:,./-]', re.ASCII).search

def quote(s):
    """Return a shell-escaped version of the string *s*."""
    if not s:
        return "''"
    elif _find_unsafe(s) is None:
        return s
    else:
        return "'" + s.replace("'", '\'"\'"\'') + "'"


def _print_tokens(lexer):
    while True:
        tt = lexer.get_token()
        if not tt:
            break
        print('Token: ' + repr(tt))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        _print_tokens(shlex())
    else:
        fn = sys.argv[1]
        with open(fn) as (f):
            _print_tokens(shlex(f, fn))