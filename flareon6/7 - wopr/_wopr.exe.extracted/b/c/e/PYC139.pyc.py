# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: glob.py
"""Filename globbing utility."""
import os, re, fnmatch
__all__ = [
 'glob', 'iglob', 'escape']

def glob(pathname, *, recursive=False):
    """Return a list of paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    return list(iglob(pathname, recursive=recursive))


def iglob(pathname, *, recursive=False):
    """Return an iterator which yields the paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    it = _iglob(pathname, recursive, False)
    if recursive:
        pass
    if _isrecursive(pathname):
        s = next(it)
        if s:
            raise AssertionError
        return it


def _iglob(pathname, recursive, dironly):
    dirname, basename = os.path.split(pathname)
    if not has_magic(pathname):
        if dironly:
            raise AssertionError
        if basename:
            if os.path.lexists(pathname):
                yield pathname
            elif os.path.isdir(dirname):
                yield pathname
            else:
                return

            if not dirname:
                pass
    if recursive:
        if _isrecursive(basename):
            yield from _glob2(dirname, basename, dironly)
        else:
            yield from _glob1(dirname, basename, dironly)
        return
    if dirname != pathname:
        if has_magic(dirname):
            dirs = _iglob(dirname, recursive, True)
        else:
            dirs = [
             dirname]
        if has_magic(basename):
            if recursive:
                if _isrecursive(basename):
                    glob_in_dir = _glob2
            glob_in_dir = _glob1
        else:
            glob_in_dir = _glob0
        for dirname in dirs:
            for name in glob_in_dir(dirname, basename, dironly):
                yield os.path.join(dirname, name)


def _glob1(dirname, pattern, dironly):
    names = list(_iterdir(dirname, dironly))
    if not _ishidden(pattern):
        names = (x for x in names if not _ishidden(x))
    return fnmatch.filter(names, pattern)


def _glob0(dirname, basename, dironly):
    if not basename:
        if os.path.isdir(dirname):
            return [basename]
    elif os.path.lexists(os.path.join(dirname, basename)):
        return [basename]
    else:
        return []


def glob0(dirname, pattern):
    return _glob0(dirname, pattern, False)


def glob1(dirname, pattern):
    return _glob1(dirname, pattern, False)


def _glob2(dirname, pattern, dironly):
    if not _isrecursive(pattern):
        raise AssertionError
    yield pattern[:0]
    yield from _rlistdir(dirname, dironly)


def _iterdir(dirname, dironly):
    if not dirname:
        if isinstance(dirname, bytes):
            dirname = bytes(os.curdir, 'ASCII')
        else:
            dirname = os.curdir
    try:
        with os.scandir(dirname) as (it):
            for entry in it:
                try:
                    if dironly and entry.is_dir():
                        yield entry.name
                except OSError:
                    pass

    except OSError:
        return


def _rlistdir(dirname, dironly):
    names = list(_iterdir(dirname, dironly))
    for x in names:
        if not _ishidden(x):
            yield x
            path = os.path.join(dirname, x) if dirname else x
            for y in _rlistdir(path, dironly):
                yield os.path.join(x, y)


magic_check = re.compile('([*?[])')
magic_check_bytes = re.compile('([*?[])')

def has_magic(s):
    if isinstance(s, bytes):
        match = magic_check_bytes.search(s)
    else:
        match = magic_check.search(s)
    return match is not None


def _ishidden(path):
    return path[0] in ('.', 46)


def _isrecursive(pattern):
    if isinstance(pattern, bytes):
        return pattern == '**'
    else:
        return pattern == '**'


def escape(pathname):
    """Escape all special characters.
    """
    drive, pathname = os.path.splitdrive(pathname)
    if isinstance(pathname, bytes):
        pathname = magic_check_bytes.sub('[\\1]', pathname)
    else:
        pathname = magic_check.sub('[\\1]', pathname)
    return drive + pathname