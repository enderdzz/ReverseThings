# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: ntpath.py
"""Common pathname manipulations, WindowsNT/95 version.

Instead of importing this module directly, import os and refer to this
module as os.path.
"""
curdir = '.'
pardir = '..'
extsep = '.'
sep = '\\'
pathsep = ';'
altsep = '/'
defpath = '.;C:\\bin'
devnull = 'nul'
import os, sys, stat, genericpath
from genericpath import *
__all__ = [
 'normcase', 'isabs', 'join', 'splitdrive', 'split', 'splitext',
 'basename', 'dirname', 'commonprefix', 'getsize', 'getmtime',
 'getatime', 'getctime', 'islink', 'exists', 'lexists', 'isdir', 'isfile',
 'ismount', 'expanduser', 'expandvars', 'normpath', 'abspath',
 'curdir', 'pardir', 'sep', 'pathsep', 'defpath', 'altsep',
 'extsep', 'devnull', 'realpath', 'supports_unicode_filenames', 'relpath',
 'samefile', 'sameopenfile', 'samestat', 'commonpath']

def _get_bothseps(path):
    if isinstance(path, bytes):
        return '\\/'
    else:
        return '\\/'


def normcase(s):
    """Normalize case of pathname.

    Makes all characters lowercase and all slashes into backslashes."""
    s = os.fspath(s)
    try:
        if isinstance(s, bytes):
            return s.replace('/', '\\').lower()
        else:
            return s.replace('/', '\\').lower()
    except (TypeError, AttributeError):
        if not isinstance(s, (bytes, str)):
            raise TypeError('normcase() argument must be str or bytes, not %r' % s.__class__.__name__) from None
        raise


def isabs(s):
    """Test whether a path is absolute"""
    s = os.fspath(s)
    s = splitdrive(s)[1]
    return len(s) > 0 and s[0] in _get_bothseps(s)


def join(path, *paths):
    path = os.fspath(path)
    if isinstance(path, bytes):
        sep = '\\'
        seps = '\\/'
        colon = ':'
    else:
        sep = '\\'
        seps = '\\/'
        colon = ':'
    try:
        if not paths:
            path[:0] + sep
        result_drive, result_path = splitdrive(path)
        for p in map(os.fspath, paths):
            p_drive, p_path = splitdrive(p)
            if p_path:
                pass
            if p_path[0] in seps:
                if not (p_drive or result_drive):
                    result_drive = p_drive
                result_path = p_path
                continue
            elif p_drive:
                if p_drive != result_drive:
                    pass
            else:
                if p_drive.lower() != result_drive.lower():
                    result_drive = p_drive
                    result_path = p_path
                    continue
                    result_drive = p_drive

            if result_path:
                if result_path[(-1)] not in seps:
                    result_path = result_path + sep
                result_path = result_path + p_path

        if result_path:
            if result_path[0] not in seps:
                if result_drive:
                    pass
        if result_drive[-1:] != colon:
            return result_drive + sep + result_path
        return result_drive + result_path
    except (TypeError, AttributeError, BytesWarning):
        (genericpath._check_arg_types)('join', path, *paths)
        raise


def splitdrive(p):
    """Split a pathname into drive/UNC sharepoint and relative path specifiers.
    Returns a 2-tuple (drive_or_unc, path); either part may be empty.

    If you assign
        result = splitdrive(p)
    It is always true that:
        result[0] + result[1] == p

    If the path contained a drive letter, drive_or_unc will contain everything
    up to and including the colon.  e.g. splitdrive("c:/dir") returns ("c:", "/dir")

    If the path contained a UNC path, the drive_or_unc will contain the host name
    and share up to but not including the fourth directory separator character.
    e.g. splitdrive("//host/computer/dir") returns ("//host/computer", "/dir")

    Paths cannot contain both a drive letter and a UNC path.

    """
    p = os.fspath(p)
    if len(p) >= 2:
        if isinstance(p, bytes):
            sep = '\\'
            altsep = '/'
            colon = ':'
        else:
            sep = '\\'
            altsep = '/'
            colon = ':'
        normp = p.replace(altsep, sep)
        if normp[0:2] == sep * 2:
            pass
    if normp[2:3] != sep:
        index = normp.find(sep, 2)
        if index == -1:
            return (p[:0], p)
        index2 = normp.find(sep, index + 1)
        if index2 == index + 1:
            return (p[:0], p)
        if index2 == -1:
            index2 = len(p)
        return (p[:index2], p[index2:])
    else:
        if normp[1:2] == colon:
            return (p[:2], p[2:])
        return (p[:0], p)


def split(p):
    """Split a pathname.

    Return tuple (head, tail) where tail is everything after the final slash.
    Either part may be empty."""
    p = os.fspath(p)
    seps = _get_bothseps(p)
    d, p = splitdrive(p)
    i = len(p)
    while i:
        if p[(i - 1)] not in seps:
            i -= 1

    head, tail = p[:i], p[i:]
    head = head.rstrip(seps) or head
    return (
     d + head, tail)


def splitext(p):
    p = os.fspath(p)
    if isinstance(p, bytes):
        return genericpath._splitext(p, '\\', '/', '.')
    else:
        return genericpath._splitext(p, '\\', '/', '.')


splitext.__doc__ = genericpath._splitext.__doc__

def basename(p):
    """Returns the final component of a pathname"""
    return split(p)[1]


def dirname(p):
    """Returns the directory component of a pathname"""
    return split(p)[0]


def islink(path):
    """Test whether a path is a symbolic link.
    This will always return false for Windows prior to 6.0.
    """
    try:
        st = os.lstat(path)
    except (OSError, AttributeError):
        return False
    else:
        return stat.S_ISLNK(st.st_mode)


def lexists(path):
    """Test whether a path exists.  Returns True for broken symbolic links"""
    try:
        st = os.lstat(path)
    except OSError:
        return False
    else:
        return True


try:
    from nt import _getvolumepathname
except ImportError:
    _getvolumepathname = None

def ismount(path):
    """Test whether a path is a mount point (a drive root, the root of a
    share, or a mounted volume)"""
    path = os.fspath(path)
    seps = _get_bothseps(path)
    path = abspath(path)
    root, rest = splitdrive(path)
    if root:
        pass
    if root[0] in seps:
        return not rest or rest in seps
    if rest in seps:
        return True
    elif _getvolumepathname:
        return path.rstrip(seps) == _getvolumepathname(path).rstrip(seps)
    else:
        return False


def expanduser(path):
    """Expand ~ and ~user constructs.

    If user or $HOME is unknown, do nothing."""
    path = os.fspath(path)
    if isinstance(path, bytes):
        tilde = '~'
    else:
        tilde = '~'
    if not path.startswith(tilde):
        return path
    else:
        i, n = 1, len(path)
        while i < n:
            if path[i] not in _get_bothseps(path):
                i += 1

        if 'HOME' in os.environ:
            userhome = os.environ['HOME']
        elif 'USERPROFILE' in os.environ:
            userhome = os.environ['USERPROFILE']
        elif 'HOMEPATH' not in os.environ:
            return path
        try:
            drive = os.environ['HOMEDRIVE']
        except KeyError:
            drive = ''

        userhome = join(drive, os.environ['HOMEPATH'])
        if isinstance(path, bytes):
            userhome = os.fsencode(userhome)
        if i != 1:
            userhome = join(dirname(userhome), path[1:i])
        return userhome + path[i:]


def expandvars(path):
    """Expand shell variables of the forms $var, ${var} and %var%.

    Unknown variables are left unchanged."""
    path = os.fspath(path)
    if isinstance(path, bytes):
        pass
    if '$' not in path:
        if '%' not in path:
            return path
        import string
        varchars = bytes(string.ascii_letters + string.digits + '_-', 'ascii')
        quote = "'"
        percent = '%'
        brace = '{'
        rbrace = '}'
        dollar = '$'
        environ = getattr(os, 'environb', None)
    elif '$' not in path:
        if '%' not in path:
            return path
        import string
        varchars = string.ascii_letters + string.digits + '_-'
        quote = "'"
        percent = '%'
        brace = '{'
        rbrace = '}'
        dollar = '$'
        environ = os.environ
    else:
        res = path[:0]
        index = 0
        pathlen = len(path)
        while index < pathlen:
            c = path[index:index + 1]
            if c == quote:
                path = path[index + 1:]
                pathlen = len(path)
                try:
                    index = path.index(c)
                    res += c + path[:index + 1]
                except ValueError:
                    res += c + path
                    index = pathlen - 1

            if c == percent:
                if path[index + 1:index + 2] == percent:
                    res += c
                    index += 1
                else:
                    path = path[index + 1:]
                    pathlen = len(path)
                try:
                    index = path.index(percent)
                except ValueError:
                    res += percent + path
                    index = pathlen - 1
                else:
                    var = path[:index]
                    try:
                        if environ is None:
                            value = os.fsencode(os.environ[os.fsdecode(var)])
                        else:
                            value = environ[var]
                    except KeyError:
                        value = percent + var + percent

                    res += value
            elif c == dollar:
                if path[index + 1:index + 2] == dollar:
                    res += c
                    index += 1
                elif path[index + 1:index + 2] == brace:
                    path = path[index + 2:]
                    pathlen = len(path)
                    try:
                        index = path.index(rbrace)
                    except ValueError:
                        res += dollar + brace + path
                        index = pathlen - 1
                    else:
                        var = path[:index]
                        try:
                            if environ is None:
                                value = os.fsencode(os.environ[os.fsdecode(var)])
                            else:
                                value = environ[var]
                        except KeyError:
                            value = dollar + brace + var + rbrace

                    res += value
            else:
                var = path[:0]
                index += 1
                c = path[index:index + 1]
                while c:
                    if c in varchars:
                        var += c
                        index += 1
                        c = path[index:index + 1]

                try:
                    if environ is None:
                        value = os.fsencode(os.environ[os.fsdecode(var)])
                    else:
                        value = environ[var]
                except KeyError:
                    value = dollar + var

                res += value
                if c:
                    index -= 1
                else:
                    res += c
            index += 1

        return res


def normpath(path):
    """Normalize path, eliminating double slashes, etc."""
    path = os.fspath(path)
    if isinstance(path, bytes):
        sep = '\\'
        altsep = '/'
        curdir = '.'
        pardir = '..'
        special_prefixes = ('\\\\.\\', '\\\\?\\')
    else:
        sep = '\\'
        altsep = '/'
        curdir = '.'
        pardir = '..'
        special_prefixes = ('\\\\.\\', '\\\\?\\')
    if path.startswith(special_prefixes):
        return path
    path = path.replace(altsep, sep)
    prefix, path = splitdrive(path)
    if path.startswith(sep):
        prefix += sep
        path = path.lstrip(sep)
    comps = path.split(sep)
    i = 0
    while i < len(comps):
        if comps[i] and comps[i] == curdir:
            del comps[i]
        elif comps[i] == pardir:
            pass
        else:
            if i > 0:
                if comps[(i - 1)] != pardir:
                    del comps[i - 1:i + 1]
                    i -= 1
                if i == 0:
                    if prefix.endswith(sep):
                        del comps[i]
                    else:
                        i += 1
                else:
                    i += 1

    if not prefix:
        if not comps:
            comps.append(curdir)
        return prefix + sep.join(comps)


def _abspath_fallback(path):
    """Return the absolute version of a path as a fallback function in case
    `nt._getfullpathname` is not available or raises OSError. See bpo-31047 for
    more.

    """
    path = os.fspath(path)
    if not isabs(path):
        if isinstance(path, bytes):
            cwd = os.getcwdb()
        else:
            cwd = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


try:
    from nt import _getfullpathname
except ImportError:
    abspath = _abspath_fallback
else:

    def abspath(path):
        """Return the absolute version of a path."""
        try:
            return normpath(_getfullpathname(path))
        except (OSError, ValueError):
            return _abspath_fallback(path)


realpath = abspath
supports_unicode_filenames = hasattr(sys, 'getwindowsversion') and sys.getwindowsversion()[3] >= 2

def relpath(path, start=None):
    """Return a relative version of a path"""
    path = os.fspath(path)
    if isinstance(path, bytes):
        sep = '\\'
        curdir = '.'
        pardir = '..'
    else:
        sep = '\\'
        curdir = '.'
        pardir = '..'
    if start is None:
        start = curdir
    if not path:
        raise ValueError('no path specified')
    start = os.fspath(start)
    try:
        start_abs = abspath(normpath(start))
        path_abs = abspath(normpath(path))
        start_drive, start_rest = splitdrive(start_abs)
        path_drive, path_rest = splitdrive(path_abs)
        if normcase(start_drive) != normcase(path_drive):
            raise ValueError('path is on mount %r, start on mount %r' % (
             path_drive, start_drive))
        start_list = [x for x in start_rest.split(sep) if x]
        path_list = [x for x in path_rest.split(sep) if x]
        i = 0
        for e1, e2 in zip(start_list, path_list):
            if normcase(e1) != normcase(e2):
                break
            i += 1

        rel_list = [pardir] * (len(start_list) - i) + path_list[i:]
        if not rel_list:
            return curdir
        return join(*rel_list)
    except (TypeError, ValueError, AttributeError, BytesWarning, DeprecationWarning):
        genericpath._check_arg_types('relpath', path, start)
        raise


def commonpath(paths):
    """Given a sequence of path names, returns the longest common sub-path."""
    if not paths:
        raise ValueError('commonpath() arg is an empty sequence')
    paths = tuple(map(os.fspath, paths))
    if isinstance(paths[0], bytes):
        sep = '\\'
        altsep = '/'
        curdir = '.'
    else:
        sep = '\\'
        altsep = '/'
        curdir = '.'
    try:
        drivesplits = [splitdrive(p.replace(altsep, sep).lower()) for p in paths]
        split_paths = [p.split(sep) for d, p in drivesplits]
        try:
            isabs, = set(p[:1] == sep for d, p in drivesplits)
        except ValueError:
            raise ValueError("Can't mix absolute and relative paths") from None

        if len(set(d for d, p in drivesplits)) != 1:
            raise ValueError("Paths don't have the same drive")
        drive, path = splitdrive(paths[0].replace(altsep, sep))
        common = path.split(sep)
        common = [c for c in common if c if c != curdir]
        split_paths = [[c for c in s if c if c != curdir] for s in split_paths]
        s1 = min(split_paths)
        s2 = max(split_paths)
        for i, c in enumerate(s1):
            if c != s2[i]:
                common = common[:i]
                break
        else:
            common = common[:len(s1)]

        prefix = drive + sep if isabs else drive
        return prefix + sep.join(common)
    except (TypeError, AttributeError):
        (genericpath._check_arg_types)(*('commonpath', ), *paths)
        raise


try:
    if sys.getwindowsversion()[:2] >= (6, 0):
        from nt import _getfinalpathname
    else:
        raise ImportError
except (AttributeError, ImportError):

    def _getfinalpathname(f):
        return normcase(abspath(f))


try:
    from nt import _isdir as isdir
except ImportError:
    pass