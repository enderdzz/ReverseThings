# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: gettext.py
"""Internationalization and localization support.

This module provides internationalization (I18N) and localization (L10N)
support for your Python programs by providing an interface to the GNU gettext
message catalog library.

I18N refers to the operation by which a program is made aware of multiple
languages.  L10N refers to the adaptation of your program, once
internationalized, to the local language and cultural habits.

"""
import locale, os, re, sys
__all__ = [
 'NullTranslations', 'GNUTranslations', 'Catalog',
 'find', 'translation', 'install', 'textdomain', 'bindtextdomain',
 'bind_textdomain_codeset',
 'dgettext', 'dngettext', 'gettext', 'lgettext', 'ldgettext',
 'ldngettext', 'lngettext', 'ngettext']
_default_localedir = os.path.join(sys.base_prefix, 'share', 'locale')
_token_pattern = re.compile('\n        (?P<WHITESPACES>[ \\t]+)                    | # spaces and horizontal tabs\n        (?P<NUMBER>[0-9]+\\b)                       | # decimal integer\n        (?P<NAME>n\\b)                              | # only n is allowed\n        (?P<PARENTHESIS>[()])                      |\n        (?P<OPERATOR>[-*/%+?:]|[><!]=?|==|&&|\\|\\|) | # !, *, /, %, +, -, <, >,\n                                                     # <=, >=, ==, !=, &&, ||,\n                                                     # ? :\n                                                     # unary and bitwise ops\n                                                     # not allowed\n        (?P<INVALID>\\w+|.)                           # invalid token\n    ', re.VERBOSE | re.DOTALL)

def _tokenize(plural):
    for mo in re.finditer(_token_pattern, plural):
        kind = mo.lastgroup
        if kind == 'WHITESPACES':
            continue
        value = mo.group(kind)
        if kind == 'INVALID':
            raise ValueError('invalid token in plural form: %s' % value)
        yield value

    yield ''


def _error(value):
    if value:
        return ValueError('unexpected token in plural form: %s' % value)
    else:
        return ValueError('unexpected end of plural form')


_binary_ops = (('||',), ('&&',), ('==', '!='), ('<', '>', '<=', '>='), ('+', '-'),
               ('*', '/', '%'))
_binary_ops = {op:i for i, ops in enumerate(_binary_ops, 1) for op in ops}
_c2py_ops = {'||':'or', 
 '&&':'and',  '/':'//'}

def _parse(tokens, priority=-1):
    result = ''
    nexttok = next(tokens)
    while 1:
        if nexttok == '!':
            result += 'not '
            nexttok = next(tokens)

    if nexttok == '(':
        sub, nexttok = _parse(tokens)
        result = '%s(%s)' % (result, sub)
        if nexttok != ')':
            raise ValueError('unbalanced parenthesis in plural form')
        elif nexttok == 'n':
            result = '%s%s' % (result, nexttok)
        else:
            try:
                value = int(nexttok, 10)
            except ValueError:
                raise _error(nexttok) from None

            result = '%s%d' % (result, value)
        nexttok = next(tokens)
        j = 100
        while nexttok in _binary_ops:
            i = _binary_ops[nexttok]
            if i < priority:
                break
            if i in (3, 4):
                if j in (3, 4):
                    result = '(%s)' % result
                op = _c2py_ops.get(nexttok, nexttok)
                right, nexttok = _parse(tokens, i + 1)
                result = '%s %s %s' % (result, op, right)
                j = i

        if not j == priority == 4:
            result = '(%s)' % result
        if nexttok == '?':
            pass
    if priority <= 0:
        if_true, nexttok = _parse(tokens, 0)
        if nexttok != ':':
            raise _error(nexttok)
        if_false, nexttok = _parse(tokens)
        result = '%s if %s else %s' % (if_true, result, if_false)
        if priority == 0:
            result = '(%s)' % result
        return (
         result, nexttok)


def _as_int(n):
    try:
        i = round(n)
    except TypeError:
        raise TypeError('Plural value must be an integer, got %s' % (
         n.__class__.__name__,)) from None

    import warnings
    warnings.warn('Plural value must be an integer, got %s' % (
     n.__class__.__name__,), DeprecationWarning, 4)
    return n


def c2py(plural):
    """Gets a C expression as used in PO files for plural forms and returns a
    Python function that implements an equivalent expression.
    """
    if len(plural) > 1000:
        raise ValueError('plural form expression is too long')
    try:
        result, nexttok = _parse(_tokenize(plural))
        if nexttok:
            raise _error(nexttok)
        depth = 0
        for c in result:
            if c == '(':
                depth += 1
                if depth > 20:
                    raise ValueError('plural form expression is too complex')
                elif c == ')':
                    depth -= 1

        ns = {'_as_int': _as_int}
        exec('if True:\n            def func(n):\n                if not isinstance(n, int):\n                    n = _as_int(n)\n                return int(%s)\n            ' % result, ns)
        return ns['func']
    except RecursionError:
        raise ValueError('plural form expression is too complex')


def _expand_lang(loc):
    loc = locale.normalize(loc)
    COMPONENT_CODESET = 1
    COMPONENT_TERRITORY = 2
    COMPONENT_MODIFIER = 4
    mask = 0
    pos = loc.find('@')
    if pos >= 0:
        modifier = loc[pos:]
        loc = loc[:pos]
        mask |= COMPONENT_MODIFIER
    else:
        modifier = ''
    pos = loc.find('.')
    if pos >= 0:
        codeset = loc[pos:]
        loc = loc[:pos]
        mask |= COMPONENT_CODESET
    else:
        codeset = ''
    pos = loc.find('_')
    if pos >= 0:
        territory = loc[pos:]
        loc = loc[:pos]
        mask |= COMPONENT_TERRITORY
    else:
        territory = ''
    language = loc
    ret = []
    for i in range(mask + 1):
        if not i & ~mask:
            val = language
            if i & COMPONENT_TERRITORY:
                val += territory
            if i & COMPONENT_CODESET:
                val += codeset
            if i & COMPONENT_MODIFIER:
                val += modifier
            ret.append(val)

    ret.reverse()
    return ret


class NullTranslations:

    def __init__(self, fp=None):
        self._info = {}
        self._charset = None
        self._output_charset = None
        self._fallback = None
        if fp is not None:
            self._parse(fp)

    def _parse(self, fp):
        pass

    def add_fallback(self, fallback):
        if self._fallback:
            self._fallback.add_fallback(fallback)
        else:
            self._fallback = fallback

    def gettext(self, message):
        if self._fallback:
            return self._fallback.gettext(message)
        else:
            return message

    def lgettext(self, message):
        if self._fallback:
            return self._fallback.lgettext(message)
        elif self._output_charset:
            return message.encode(self._output_charset)
        else:
            return message.encode(locale.getpreferredencoding())

    def ngettext(self, msgid1, msgid2, n):
        if self._fallback:
            return self._fallback.ngettext(msgid1, msgid2, n)
        elif n == 1:
            return msgid1
        else:
            return msgid2

    def lngettext(self, msgid1, msgid2, n):
        if self._fallback:
            return self._fallback.lngettext(msgid1, msgid2, n)
        else:
            if n == 1:
                tmsg = msgid1
            else:
                tmsg = msgid2
            if self._output_charset:
                return tmsg.encode(self._output_charset)
            return tmsg.encode(locale.getpreferredencoding())

    def info(self):
        return self._info

    def charset(self):
        return self._charset

    def output_charset(self):
        return self._output_charset

    def set_output_charset(self, charset):
        self._output_charset = charset

    def install(self, names=None):
        import builtins
        builtins.__dict__['_'] = self.gettext
        if hasattr(names, '__contains__'):
            if 'gettext' in names:
                builtins.__dict__['gettext'] = builtins.__dict__['_']
            if 'ngettext' in names:
                builtins.__dict__['ngettext'] = self.ngettext
            if 'lgettext' in names:
                builtins.__dict__['lgettext'] = self.lgettext
        if 'lngettext' in names:
            builtins.__dict__['lngettext'] = self.lngettext


class GNUTranslations(NullTranslations):
    LE_MAGIC = 2500072158L
    BE_MAGIC = 3725722773L
    VERSIONS = (0, 1)

    def _get_versions(self, version):
        """Returns a tuple of major version, minor version"""
        return (
         version >> 16, version & 65535)

    def _parse(self, fp):
        """Override this method to support alternative .mo formats."""
        from struct import unpack
        filename = getattr(fp, 'name', '')
        self._catalog = catalog = {}
        self.plural = lambda n: int(n != 1)
        buf = fp.read()
        buflen = len(buf)
        magic = unpack('<I', buf[:4])[0]
        if magic == self.LE_MAGIC:
            version, msgcount, masteridx, transidx = unpack('<4I', buf[4:20])
            ii = '<II'
        elif magic == self.BE_MAGIC:
            version, msgcount, masteridx, transidx = unpack('>4I', buf[4:20])
            ii = '>II'
        else:
            raise OSError(0, 'Bad magic number', filename)
        major_version, minor_version = self._get_versions(version)
        if major_version not in self.VERSIONS:
            raise OSError(0, 'Bad version number ' + str(major_version), filename)
        for i in range(0, msgcount):
            mlen, moff = unpack(ii, buf[masteridx:masteridx + 8])
            mend = moff + mlen
            tlen, toff = unpack(ii, buf[transidx:transidx + 8])
            tend = toff + tlen
            if mend < buflen:
                if tend < buflen:
                    msg = buf[moff:mend]
                    tmsg = buf[toff:tend]
                else:
                    raise OSError(0, 'File is corrupt', filename)
                if mlen == 0:
                    lastk = None
                    for b_item in tmsg.split('\n'):
                        item = b_item.decode().strip()
                        if not item:
                            continue
                        k = v = None
                        if ':' in item:
                            k, v = item.split(':', 1)
                            k = k.strip().lower()
                            v = v.strip()
                            self._info[k] = v
                            lastk = k
                        elif lastk:
                            self._info[lastk] += '\n' + item
                        else:
                            if k == 'content-type':
                                self._charset = v.split('charset=')[1]
                            elif k == 'plural-forms':
                                v = v.split(';')
                                plural = v[1].split('plural=')[1]
                                self.plural = c2py(plural)

                charset = self._charset or 'ascii'
                if '\x00' in msg:
                    msgid1, msgid2 = msg.split('\x00')
                    tmsg = tmsg.split('\x00')
                    msgid1 = str(msgid1, charset)
                    for i, x in enumerate(tmsg):
                        catalog[(msgid1, i)] = str(x, charset)

                else:
                    catalog[str(msg, charset)] = str(tmsg, charset)
                masteridx += 8
                transidx += 8

    def lgettext(self, message):
        missing = object()
        tmsg = self._catalog.get(message, missing)
        if tmsg is missing:
            if self._fallback:
                return self._fallback.lgettext(message)
            tmsg = message
        if self._output_charset:
            return tmsg.encode(self._output_charset)
        else:
            return tmsg.encode(locale.getpreferredencoding())

    def lngettext(self, msgid1, msgid2, n):
        try:
            tmsg = self._catalog[(msgid1, self.plural(n))]
        except KeyError:
            if self._fallback:
                return self._fallback.lngettext(msgid1, msgid2, n)
            if n == 1:
                tmsg = msgid1
            else:
                tmsg = msgid2

        if self._output_charset:
            return tmsg.encode(self._output_charset)
        else:
            return tmsg.encode(locale.getpreferredencoding())

    def gettext(self, message):
        missing = object()
        tmsg = self._catalog.get(message, missing)
        if tmsg is missing:
            if self._fallback:
                return self._fallback.gettext(message)
            return message
        else:
            return tmsg

    def ngettext(self, msgid1, msgid2, n):
        try:
            tmsg = self._catalog[(msgid1, self.plural(n))]
        except KeyError:
            if self._fallback:
                return self._fallback.ngettext(msgid1, msgid2, n)
            if n == 1:
                tmsg = msgid1
            else:
                tmsg = msgid2

        return tmsg


def find(domain, localedir=None, languages=None, all=False):
    if localedir is None:
        localedir = _default_localedir
    if languages is None:
        languages = []
        for envar in ('LANGUAGE', 'LC_ALL', 'LC_MESSAGES', 'LANG'):
            val = os.environ.get(envar)
            if val:
                languages = val.split(':')
                break

        if 'C' not in languages:
            languages.append('C')
        nelangs = []
        for lang in languages:
            for nelang in _expand_lang(lang):
                if nelang not in nelangs:
                    nelangs.append(nelang)

        if all:
            result = []
        else:
            result = None
        for lang in nelangs:
            if lang == 'C':
                break
            mofile = os.path.join(localedir, lang, 'LC_MESSAGES', '%s.mo' % domain)
            if os.path.exists(mofile):
                if all:
                    result.append(mofile)
                else:
                    return mofile

        return result


_translations = {}

def translation(domain, localedir=None, languages=None, class_=None, fallback=False, codeset=None):
    if class_ is None:
        class_ = GNUTranslations
    mofiles = find(domain, localedir, languages, all=True)
    if not mofiles:
        if fallback:
            return NullTranslations()
        from errno import ENOENT
        raise FileNotFoundError(ENOENT, 'No translation file found for domain', domain)
    result = None
    for mofile in mofiles:
        key = (
         class_, os.path.abspath(mofile))
        t = _translations.get(key)
        if t is None:
            with open(mofile, 'rb') as (fp):
                t = _translations.setdefault(key, class_(fp))
        import copy
        t = copy.copy(t)
        if codeset:
            t.set_output_charset(codeset)
        if result is None:
            result = t
        else:
            result.add_fallback(t)

    return result


def install(domain, localedir=None, codeset=None, names=None):
    t = translation(domain, localedir, fallback=True, codeset=codeset)
    t.install(names)


_localedirs = {}
_localecodesets = {}
_current_domain = 'messages'

def textdomain(domain=None):
    global _current_domain
    if domain is not None:
        _current_domain = domain
    return _current_domain


def bindtextdomain(domain, localedir=None):
    global _localedirs
    if localedir is not None:
        _localedirs[domain] = localedir
    return _localedirs.get(domain, _default_localedir)


def bind_textdomain_codeset(domain, codeset=None):
    global _localecodesets
    if codeset is not None:
        _localecodesets[domain] = codeset
    return _localecodesets.get(domain)


def dgettext(domain, message):
    try:
        t = translation(domain, (_localedirs.get(domain, None)), codeset=(_localecodesets.get(domain)))
    except OSError:
        return message
    else:
        return t.gettext(message)


def ldgettext(domain, message):
    codeset = _localecodesets.get(domain)
    try:
        t = translation(domain, (_localedirs.get(domain, None)), codeset=codeset)
    except OSError:
        return message.encode(codeset or locale.getpreferredencoding())
    else:
        return t.lgettext(message)


def dngettext(domain, msgid1, msgid2, n):
    try:
        t = translation(domain, (_localedirs.get(domain, None)), codeset=(_localecodesets.get(domain)))
    except OSError:
        if n == 1:
            return msgid1
        else:
            return msgid2

    return t.ngettext(msgid1, msgid2, n)


def ldngettext(domain, msgid1, msgid2, n):
    codeset = _localecodesets.get(domain)
    try:
        t = translation(domain, (_localedirs.get(domain, None)), codeset=codeset)
    except OSError:
        if n == 1:
            tmsg = msgid1
        else:
            tmsg = msgid2
        return tmsg.encode(codeset or locale.getpreferredencoding())
    else:
        return t.lngettext(msgid1, msgid2, n)


def gettext(message):
    return dgettext(_current_domain, message)


def lgettext(message):
    return ldgettext(_current_domain, message)


def ngettext(msgid1, msgid2, n):
    return dngettext(_current_domain, msgid1, msgid2, n)


def lngettext(msgid1, msgid2, n):
    return ldngettext(_current_domain, msgid1, msgid2, n)


Catalog = translation