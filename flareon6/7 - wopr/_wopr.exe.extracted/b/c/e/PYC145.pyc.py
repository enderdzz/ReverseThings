# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: shutil.py
"""Utility functions for copying and archiving files and directory trees.

XXX The functions here don't copy the resource fork or other metadata on Mac.

"""
import os, sys, stat, fnmatch, collections, errno
try:
    import zlib
    del zlib
    _ZLIB_SUPPORTED = True
except ImportError:
    _ZLIB_SUPPORTED = False

try:
    import bz2
    del bz2
    _BZ2_SUPPORTED = True
except ImportError:
    _BZ2_SUPPORTED = False

try:
    import lzma
    del lzma
    _LZMA_SUPPORTED = True
except ImportError:
    _LZMA_SUPPORTED = False

try:
    from pwd import getpwnam
except ImportError:
    getpwnam = None

try:
    from grp import getgrnam
except ImportError:
    getgrnam = None

__all__ = ['copyfileobj', 'copyfile', 'copymode', 'copystat', 'copy', 'copy2',
 'copytree', 'move', 'rmtree', 'Error', 'SpecialFileError',
 'ExecError', 'make_archive', 'get_archive_formats',
 'register_archive_format', 'unregister_archive_format',
 'get_unpack_formats', 'register_unpack_format',
 'unregister_unpack_format', 'unpack_archive',
 'ignore_patterns', 'chown', 'which', 'get_terminal_size',
 'SameFileError']

class Error(OSError):
    pass


class SameFileError(Error):
    """'Raised when source and destination are the same file.'"""
    pass


class SpecialFileError(OSError):
    r"""'Raised when trying to do a kind of operation (e.g. copying) which is\n    not supported on a special file (e.g. a named pipe)'"""
    pass


class ExecError(OSError):
    """'Raised when a command could not be executed'"""
    pass


class ReadError(OSError):
    """'Raised when an archive cannot be read'"""
    pass


class RegistryError(Exception):
    r"""'Raised when a registry operation with the archiving\n    and unpacking registries fails'"""
    pass


def copyfileobj(fsrc, fdst, length=16384):
    """copy data from file-like object fsrc to file-like object fdst"""
    while True:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)


def _samefile(src, dst):
    if hasattr(os.path, 'samefile'):
        try:
            return os.path.samefile(src, dst)
        except OSError:
            return False

        return os.path.normcase(os.path.abspath(src)) == os.path.normcase(os.path.abspath(dst))


def copyfile(src, dst, *, follow_symlinks=True):
    """Copy data from src to dst.

    If follow_symlinks is not set and src is a symbolic link, a new
    symlink will be created instead of copying the file it points to.

    """
    if _samefile(src, dst):
        raise SameFileError('{!r} and {!r} are the same file'.format(src, dst))
    for fn in [src, dst]:
        try:
            st = os.stat(fn)
        except OSError:
            pass
        else:
            if stat.S_ISFIFO(st.st_mode):
                raise SpecialFileError('`%s` is a named pipe' % fn)

    if not follow_symlinks:
        if os.path.islink(src):
            os.symlink(os.readlink(src), dst)
        else:
            with open(src, 'rb') as (fsrc):
                with open(dst, 'wb') as (fdst):
                    copyfileobj(fsrc, fdst)
        return dst


def copymode(src, dst, *, follow_symlinks=True):
    """Copy mode bits from src to dst.

    If follow_symlinks is not set, symlinks aren't followed if and only
    if both `src` and `dst` are symlinks.  If `lchmod` isn't available
    (e.g. Linux) this method does nothing.

    """
    if not follow_symlinks:
        if os.path.islink(src):
            if os.path.islink(dst):
                if hasattr(os, 'lchmod'):
                    stat_func, chmod_func = os.lstat, os.lchmod
                else:
                    return
        else:
            if hasattr(os, 'chmod'):
                stat_func, chmod_func = os.stat, os.chmod
            else:
                return
            st = stat_func(src)
            chmod_func(dst, stat.S_IMODE(st.st_mode))


if hasattr(os, 'listxattr'):

    def _copyxattr(src, dst, *, follow_symlinks=True):
        """Copy extended filesystem attributes from `src` to `dst`.

        Overwrite existing attributes.

        If `follow_symlinks` is false, symlinks won't be followed.

        """
        try:
            names = os.listxattr(src, follow_symlinks=follow_symlinks)
        except OSError as e:
            try:
                if e.errno not in (errno.ENOTSUP, errno.ENODATA):
                    raise
                return
            finally:
                e = None
                del e

        for name in names:
            try:
                value = os.getxattr(src, name, follow_symlinks=follow_symlinks)
                os.setxattr(dst, name, value, follow_symlinks=follow_symlinks)
            except OSError as e:
                try:
                    if e.errno not in (errno.EPERM, errno.ENOTSUP, errno.ENODATA):
                        raise
                finally:
                    e = None
                    del e


else:

    def _copyxattr(*args, **kwargs):
        pass


def copystat(src, dst, *, follow_symlinks=True):
    """Copy file metadata

    Copy the permission bits, last access time, last modification time, and
    flags from `src` to `dst`. On Linux, copystat() also copies the "extended
    attributes" where possible. The file contents, owner, and group are
    unaffected. `src` and `dst` are path names given as strings.

    If the optional flag `follow_symlinks` is not set, symlinks aren't
    followed if and only if both `src` and `dst` are symlinks.
    """

    def _nop(*args, ns=None, follow_symlinks=None):
        pass

    follow = follow_symlinks or not (os.path.islink(src) and os.path.islink(dst))
    if follow:

        def lookup(name):
            return getattr(os, name, _nop)

    else:

        def lookup(name):
            fn = getattr(os, name, _nop)
            if fn in os.supports_follow_symlinks:
                return fn
            else:
                return _nop

    st = lookup('stat')(src, follow_symlinks=follow)
    mode = stat.S_IMODE(st.st_mode)
    lookup('utime')(dst, ns=(st.st_atime_ns, st.st_mtime_ns), follow_symlinks=follow)
    try:
        lookup('chmod')(dst, mode, follow_symlinks=follow)
    except NotImplementedError:
        pass

    if hasattr(st, 'st_flags'):
        try:
            lookup('chflags')(dst, (st.st_flags), follow_symlinks=follow)
        except OSError as why:
            try:
                for err in ('EOPNOTSUPP', 'ENOTSUP'):
                    if hasattr(errno, err):
                        if why.errno == getattr(errno, err):
                            break
                else:
                    raise

            finally:
                why = None
                del why

        _copyxattr(src, dst, follow_symlinks=follow)


def copy(src, dst, *, follow_symlinks=True):
    """Copy data and mode bits ("cp src dst"). Return the file's destination.

    The destination may be a directory.

    If follow_symlinks is false, symlinks won't be followed. This
    resembles GNU's "cp -P src dst".

    If source and destination are the same file, a SameFileError will be
    raised.

    """
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    copyfile(src, dst, follow_symlinks=follow_symlinks)
    copymode(src, dst, follow_symlinks=follow_symlinks)
    return dst


def copy2(src, dst, *, follow_symlinks=True):
    """Copy data and metadata. Return the file's destination.

    Metadata is copied with copystat(). Please see the copystat function
    for more information.

    The destination may be a directory.

    If follow_symlinks is false, symlinks won't be followed. This
    resembles GNU's "cp -P src dst".

    """
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    copyfile(src, dst, follow_symlinks=follow_symlinks)
    copystat(src, dst, follow_symlinks=follow_symlinks)
    return dst


def ignore_patterns(*patterns):
    """Function that can be used as copytree() ignore parameter.

    Patterns is a sequence of glob-style patterns
    that are used to exclude files"""

    def _ignore_patterns(path, names):
        ignored_names = []
        for pattern in patterns:
            ignored_names.extend(fnmatch.filter(names, pattern))

        return set(ignored_names)

    return _ignore_patterns


def copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False):
    """Recursively copy a directory tree.

    The destination directory must not already exist.
    If exception(s) occur, an Error is raised with a list of reasons.

    If the optional symlinks flag is true, symbolic links in the
    source tree result in symbolic links in the destination tree; if
    it is false, the contents of the files pointed to by symbolic
    links are copied. If the file pointed by the symlink doesn't
    exist, an exception will be added in the list of errors raised in
    an Error exception at the end of the copy process.

    You can set the optional ignore_dangling_symlinks flag to true if you
    want to silence this exception. Notice that this has no effect on
    platforms that don't support os.symlink.

    The optional ignore argument is a callable. If given, it
    is called with the `src` parameter, which is the directory
    being visited by copytree(), and `names` which is the list of
    `src` contents, as returned by os.listdir():

        callable(src, names) -> ignored_names

    Since copytree() is called recursively, the callable will be
    called once for each directory that is copied. It returns a
    list of names relative to the `src` directory that should
    not be copied.

    The optional copy_function argument is a callable that will be used
    to copy each file. It will be called with the source path and the
    destination path as arguments. By default, copy2() is used, but any
    function that supports the same signature (like copy()) can be used.

    """
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()
    os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.islink(srcname):
                linkto = os.readlink(srcname)
                if symlinks:
                    os.symlink(linkto, dstname)
                    copystat(srcname, dstname, follow_symlinks=(not symlinks))
                elif not os.path.exists(linkto):
                    if ignore_dangling_symlinks:
                        continue
                    if os.path.isdir(srcname):
                        copytree(srcname, dstname, symlinks, ignore, copy_function)
                    else:
                        copy_function(srcname, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks, ignore, copy_function)
            else:
                copy_function(srcname, dstname)
        except Error as err:
            try:
                errors.extend(err.args[0])
            finally:
                err = None
                del err

        except OSError as why:
            try:
                errors.append((srcname, dstname, str(why)))
            finally:
                why = None
                del why

    try:
        copystat(src, dst)
    except OSError as why:
        try:
            if getattr(why, 'winerror', None) is None:
                errors.append((src, dst, str(why)))
        finally:
            why = None
            del why

    if errors:
        raise Error(errors)
    return dst


def _rmtree_unsafe(path, onerror):
    try:
        with os.scandir(path) as (scandir_it):
            entries = list(scandir_it)
    except OSError:
        onerror(os.scandir, path, sys.exc_info())
        entries = []

    for entry in entries:
        fullname = entry.path
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except OSError:
            is_dir = False

        if is_dir:
            try:
                if entry.is_symlink():
                    raise OSError('Cannot call rmtree on a symbolic link')
            except OSError:
                onerror(os.path.islink, fullname, sys.exc_info())
                continue

            _rmtree_unsafe(fullname, onerror)
        else:
            try:
                os.unlink(fullname)
            except OSError:
                onerror(os.unlink, fullname, sys.exc_info())

    try:
        os.rmdir(path)
    except OSError:
        onerror(os.rmdir, path, sys.exc_info())


def _rmtree_safe_fd(topfd, path, onerror):
    try:
        with os.scandir(topfd) as (scandir_it):
            entries = list(scandir_it)
    except OSError as err:
        try:
            err.filename = path
            onerror(os.scandir, path, sys.exc_info())
            return
        finally:
            err = None
            del err

    for entry in entries:
        fullname = os.path.join(path, entry.name)
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
            if is_dir:
                orig_st = entry.stat(follow_symlinks=False)
                is_dir = stat.S_ISDIR(orig_st.st_mode)
        except OSError:
            is_dir = False

        if is_dir:
            try:
                dirfd = os.open((entry.name), (os.O_RDONLY), dir_fd=topfd)
            except OSError:
                onerror(os.open, fullname, sys.exc_info())
            else:
                try:
                    if os.path.samestat(orig_st, os.fstat(dirfd)):
                        _rmtree_safe_fd(dirfd, fullname, onerror)
                        try:
                            os.rmdir((entry.name), dir_fd=topfd)
                        except OSError:
                            onerror(os.rmdir, fullname, sys.exc_info())

                    try:
                        raise OSError('Cannot call rmtree on a symbolic link')
                    except OSError:
                        onerror(os.path.islink, fullname, sys.exc_info())

                finally:
                    os.close(dirfd)

        else:
            try:
                os.unlink((entry.name), dir_fd=topfd)
            except OSError:
                onerror(os.unlink, fullname, sys.exc_info())


_use_fd_functions = {
 os.open, os.stat, os.unlink, os.rmdir} <= os.supports_dir_fd and os.scandir in os.supports_fd and os.stat in os.supports_follow_symlinks

def rmtree(path, ignore_errors=False, onerror=None):
    """Recursively delete a directory tree.

    If ignore_errors is set, errors are ignored; otherwise, if onerror
    is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is platform and implementation dependent;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info().  If ignore_errors
    is false and onerror is None, an exception is raised.

    """
    if ignore_errors:

        def onerror(*args):
            pass

    elif onerror is None:

        def onerror(*args):
            raise

    else:
        if _use_fd_functions:
            if isinstance(path, bytes):
                path = os.fsdecode(path)
            try:
                orig_st = os.lstat(path)
            except Exception:
                onerror(os.lstat, path, sys.exc_info())
                return
            else:
                try:
                    fd = os.open(path, os.O_RDONLY)
                except Exception:
                    onerror(os.lstat, path, sys.exc_info())
                    return
                else:
                    try:
                        if os.path.samestat(orig_st, os.fstat(fd)):
                            _rmtree_safe_fd(fd, path, onerror)
                            try:
                                os.rmdir(path)
                            except OSError:
                                onerror(os.rmdir, path, sys.exc_info())

                        try:
                            raise OSError('Cannot call rmtree on a symbolic link')
                        except OSError:
                            onerror(os.path.islink, path, sys.exc_info())

                    finally:
                        os.close(fd)

        try:
            if os.path.islink(path):
                raise OSError('Cannot call rmtree on a symbolic link')
        except OSError:
            onerror(os.path.islink, path, sys.exc_info())
            return
        else:
            return _rmtree_unsafe(path, onerror)


rmtree.avoids_symlink_attacks = _use_fd_functions

def _basename(path):
    sep = os.path.sep + (os.path.altsep or '')
    return os.path.basename(path.rstrip(sep))


def move(src, dst, copy_function=copy2):
    """Recursively move a file or directory to another location. This is
    similar to the Unix "mv" command. Return the file or directory's
    destination.

    If the destination is a directory or a symlink to a directory, the source
    is moved inside the directory. The destination path must not already
    exist.

    If the destination already exists but is not a directory, it may be
    overwritten depending on os.rename() semantics.

    If the destination is on our current filesystem, then rename() is used.
    Otherwise, src is copied to the destination and then removed. Symlinks are
    recreated under the new name if os.rename() fails because of cross
    filesystem renames.

    The optional `copy_function` argument is a callable that will be used
    to copy the source or it will be delegated to `copytree`.
    By default, copy2() is used, but any function that supports the same
    signature (like copy()) can be used.

    A lot more could be done here...  A look at a mv.c shows a lot of
    the issues this implementation glosses over.

    """
    real_dst = dst
    if os.path.isdir(dst):
        if _samefile(src, dst):
            os.rename(src, dst)
        return
    else:
        real_dst = os.path.join(dst, _basename(src))
        if os.path.exists(real_dst):
            raise Error("Destination path '%s' already exists" % real_dst)
        try:
            os.rename(src, real_dst)
        except OSError:
            if os.path.islink(src):
                linkto = os.readlink(src)
                os.symlink(linkto, real_dst)
                os.unlink(src)
            elif os.path.isdir(src):
                if _destinsrc(src, dst):
                    raise Error("Cannot move a directory '%s' into itself '%s'." % (
                     src, dst))
                copytree(src, real_dst, copy_function=copy_function, symlinks=True)
                rmtree(src)
            else:
                copy_function(src, real_dst)
                os.unlink(src)

        return real_dst


def _destinsrc(src, dst):
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    if not src.endswith(os.path.sep):
        src += os.path.sep
    if not dst.endswith(os.path.sep):
        dst += os.path.sep
    return dst.startswith(src)


def _get_gid(name):
    """Returns a gid, given a group name."""
    if getgrnam is None or name is None:
        return
    try:
        result = getgrnam(name)
    except KeyError:
        result = None

    if result is not None:
        return result[2]


def _get_uid(name):
    """Returns an uid, given a user name."""
    if getpwnam is None or name is None:
        return
    try:
        result = getpwnam(name)
    except KeyError:
        result = None

    if result is not None:
        return result[2]


def _make_tarball(base_name, base_dir, compress='gzip', verbose=0, dry_run=0, owner=None, group=None, logger=None):
    """Create a (possibly compressed) tar file from all the files under
    'base_dir'.

    'compress' must be "gzip" (the default), "bzip2", "xz", or None.

    'owner' and 'group' can be used to define an owner and a group for the
    archive that is being built. If not provided, the current owner and group
    will be used.

    The output tar file will be named 'base_name' +  ".tar", possibly plus
    the appropriate compression extension (".gz", ".bz2", or ".xz").

    Returns the output filename.
    """
    if compress is None:
        tar_compression = ''
    elif _ZLIB_SUPPORTED:
        if compress == 'gzip':
            tar_compression = 'gz'
        elif _BZ2_SUPPORTED:
            if compress == 'bzip2':
                tar_compression = 'bz2'
            elif _LZMA_SUPPORTED:
                if compress == 'xz':
                    tar_compression = 'xz'
                else:
                    raise ValueError("bad value for 'compress', or compression format not supported : {0}".format(compress))
                import tarfile
                compress_ext = '.' + tar_compression if compress else ''
                archive_name = base_name + '.tar' + compress_ext
                archive_dir = os.path.dirname(archive_name)
                if archive_dir:
                    pass
                if not os.path.exists(archive_dir):
                    if logger is not None:
                        logger.info('creating %s', archive_dir)
                    if not dry_run:
                        os.makedirs(archive_dir)
                    if logger is not None:
                        logger.info('Creating tar archive')
                    uid = _get_uid(owner)
                    gid = _get_gid(group)

                    def _set_uid_gid(tarinfo):
                        if gid is not None:
                            tarinfo.gid = gid
                            tarinfo.gname = group
                        if uid is not None:
                            tarinfo.uid = uid
                            tarinfo.uname = owner
                        return tarinfo

                    if not dry_run:
                        tar = tarfile.open(archive_name, 'w|%s' % tar_compression)
                        try:
                            tar.add(base_dir, filter=_set_uid_gid)
                        finally:
                            tar.close()

                    return archive_name


def _make_zipfile(base_name, base_dir, verbose=0, dry_run=0, logger=None):
    """Create a zip file from all the files under 'base_dir'.

    The output zip file will be named 'base_name' + ".zip".  Returns the
    name of the output zip file.
    """
    import zipfile
    zip_filename = base_name + '.zip'
    archive_dir = os.path.dirname(base_name)
    if archive_dir:
        pass
    if not os.path.exists(archive_dir):
        if logger is not None:
            logger.info('creating %s', archive_dir)
        if not dry_run:
            os.makedirs(archive_dir)
        if logger is not None:
            logger.info("creating '%s' and adding '%s' to it", zip_filename, base_dir)
        if not dry_run:
            with zipfile.ZipFile(zip_filename, 'w', compression=(zipfile.ZIP_DEFLATED)) as (zf):
                path = os.path.normpath(base_dir)
                if path != os.curdir:
                    zf.write(path, path)
                    if logger is not None:
                        logger.info("adding '%s'", path)
                    for dirpath, dirnames, filenames in os.walk(base_dir):
                        for name in sorted(dirnames):
                            path = os.path.normpath(os.path.join(dirpath, name))
                            zf.write(path, path)
                            if logger is not None:
                                logger.info("adding '%s'", path)

                        for name in filenames:
                            path = os.path.normpath(os.path.join(dirpath, name))
                            if os.path.isfile(path):
                                zf.write(path, path)
                                if logger is not None:
                                    logger.info("adding '%s'", path)

        return zip_filename


_ARCHIVE_FORMATS = {'tar': (_make_tarball, [('compress', None)], 'uncompressed tar file')}
if _ZLIB_SUPPORTED:
    _ARCHIVE_FORMATS['gztar'] = (
     _make_tarball, [('compress', 'gzip')],
     "gzip'ed tar-file")
    _ARCHIVE_FORMATS['zip'] = (_make_zipfile, [], 'ZIP file')
if _BZ2_SUPPORTED:
    _ARCHIVE_FORMATS['bztar'] = (
     _make_tarball, [('compress', 'bzip2')],
     "bzip2'ed tar-file")
if _LZMA_SUPPORTED:
    _ARCHIVE_FORMATS['xztar'] = (
     _make_tarball, [('compress', 'xz')],
     "xz'ed tar-file")

def get_archive_formats():
    """Returns a list of supported formats for archiving and unarchiving.

    Each element of the returned sequence is a tuple (name, description)
    """
    formats = [(name, registry[2]) for name, registry in _ARCHIVE_FORMATS.items()]
    formats.sort()
    return formats


def register_archive_format(name, function, extra_args=None, description=''):
    """Registers an archive format.

    name is the name of the format. function is the callable that will be
    used to create archives. If provided, extra_args is a sequence of
    (name, value) tuples that will be passed as arguments to the callable.
    description can be provided to describe the format, and will be returned
    by the get_archive_formats() function.
    """
    if extra_args is None:
        extra_args = []
    if not callable(function):
        raise TypeError('The %s object is not callable' % function)
    if not isinstance(extra_args, (tuple, list)):
        raise TypeError('extra_args needs to be a sequence')
    for element in extra_args:
        if isinstance(element, (tuple, list)) and len(element) != 2:
            raise TypeError('extra_args elements are : (arg_name, value)')

    _ARCHIVE_FORMATS[name] = (
     function, extra_args, description)


def unregister_archive_format(name):
    del _ARCHIVE_FORMATS[name]


def make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None, logger=None):
    """Create an archive file (eg. zip or tar).

    'base_name' is the name of the file to create, minus any format-specific
    extension; 'format' is the archive format: one of "zip", "tar", "gztar",
    "bztar", or "xztar".  Or any other registered format.

    'root_dir' is a directory that will be the root directory of the
    archive; ie. we typically chdir into 'root_dir' before creating the
    archive.  'base_dir' is the directory where we start archiving from;
    ie. 'base_dir' will be the common prefix of all files and
    directories in the archive.  'root_dir' and 'base_dir' both default
    to the current directory.  Returns the name of the archive file.

    'owner' and 'group' are used when creating a tar archive. By default,
    uses the current owner and group.
    """
    save_cwd = os.getcwd()
    if root_dir is not None:
        if logger is not None:
            logger.debug("changing into '%s'", root_dir)
        base_name = os.path.abspath(base_name)
        if not dry_run:
            os.chdir(root_dir)
        if base_dir is None:
            base_dir = os.curdir
        kwargs = {'dry_run':dry_run,  'logger':logger}
        try:
            format_info = _ARCHIVE_FORMATS[format]
        except KeyError:
            raise ValueError("unknown archive format '%s'" % format) from None

        func = format_info[0]
        for arg, val in format_info[1]:
            kwargs[arg] = val

        if format != 'zip':
            kwargs['owner'] = owner
            kwargs['group'] = group
        try:
            filename = func(base_name, base_dir, **kwargs)
        finally:
            if root_dir is not None:
                if logger is not None:
                    logger.debug("changing back to '%s'", save_cwd)
                os.chdir(save_cwd)

        return filename


def get_unpack_formats():
    """Returns a list of supported formats for unpacking.

    Each element of the returned sequence is a tuple
    (name, extensions, description)
    """
    formats = [(name, info[0], info[3]) for name, info in _UNPACK_FORMATS.items()]
    formats.sort()
    return formats


def _check_unpack_options(extensions, function, extra_args):
    """Checks what gets registered as an unpacker."""
    existing_extensions = {}
    for name, info in _UNPACK_FORMATS.items():
        for ext in info[0]:
            existing_extensions[ext] = name

    for extension in extensions:
        if extension in existing_extensions:
            msg = '%s is already registered for "%s"'
            raise RegistryError(msg % (extension,
             existing_extensions[extension]))

    if not callable(function):
        raise TypeError('The registered function must be a callable')


def register_unpack_format(name, extensions, function, extra_args=None, description=''):
    """Registers an unpack format.

    `name` is the name of the format. `extensions` is a list of extensions
    corresponding to the format.

    `function` is the callable that will be
    used to unpack archives. The callable will receive archives to unpack.
    If it's unable to handle an archive, it needs to raise a ReadError
    exception.

    If provided, `extra_args` is a sequence of
    (name, value) tuples that will be passed as arguments to the callable.
    description can be provided to describe the format, and will be returned
    by the get_unpack_formats() function.
    """
    if extra_args is None:
        extra_args = []
    _check_unpack_options(extensions, function, extra_args)
    _UNPACK_FORMATS[name] = (extensions, function, extra_args, description)


def unregister_unpack_format(name):
    """Removes the pack format from the registry."""
    del _UNPACK_FORMATS[name]


def _ensure_directory(path):
    """Ensure that the parent directory of `path` exists"""
    dirname = os.path.dirname(path)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)


def _unpack_zipfile(filename, extract_dir):
    """Unpack zip `filename` to `extract_dir`
    """
    import zipfile
    if not zipfile.is_zipfile(filename):
        raise ReadError('%s is not a zip file' % filename)
    zip = zipfile.ZipFile(filename)
    try:
        for info in zip.infolist():
            name = info.filename
            if not name.startswith('/'):
                if '..' in name:
                    pass
                else:
                    target = (os.path.join)(extract_dir, *name.split('/'))
                    if not target:
                        pass
                    else:
                        _ensure_directory(target)
                        if not name.endswith('/'):
                            data = zip.read(info.filename)
                            f = open(target, 'wb')
                            try:
                                f.write(data)
                            finally:
                                f.close()
                                del data

    finally:
        zip.close()


def _unpack_tarfile(filename, extract_dir):
    """Unpack tar/tar.gz/tar.bz2/tar.xz `filename` to `extract_dir`
    """
    import tarfile
    try:
        tarobj = tarfile.open(filename)
    except tarfile.TarError:
        raise ReadError('%s is not a compressed or uncompressed tar file' % filename)

    try:
        tarobj.extractall(extract_dir)
    finally:
        tarobj.close()


_UNPACK_FORMATS = {'tar':(
  [
   '.tar'], _unpack_tarfile, [], 'uncompressed tar file'), 
 'zip':(
  [
   '.zip'], _unpack_zipfile, [], 'ZIP file')}
if _ZLIB_SUPPORTED:
    _UNPACK_FORMATS['gztar'] = (
     [
      '.tar.gz', '.tgz'], _unpack_tarfile, [],
     "gzip'ed tar-file")
if _BZ2_SUPPORTED:
    _UNPACK_FORMATS['bztar'] = (
     [
      '.tar.bz2', '.tbz2'], _unpack_tarfile, [],
     "bzip2'ed tar-file")
if _LZMA_SUPPORTED:
    _UNPACK_FORMATS['xztar'] = (
     [
      '.tar.xz', '.txz'], _unpack_tarfile, [],
     "xz'ed tar-file")

def _find_unpack_format(filename):
    for name, info in _UNPACK_FORMATS.items():
        for extension in info[0]:
            if filename.endswith(extension):
                return name


def unpack_archive(filename, extract_dir=None, format=None):
    """Unpack an archive.

    `filename` is the name of the archive.

    `extract_dir` is the name of the target directory, where the archive
    is unpacked. If not provided, the current working directory is used.

    `format` is the archive format: one of "zip", "tar", "gztar", "bztar",
    or "xztar".  Or any other registered format.  If not provided,
    unpack_archive will use the filename extension and see if an unpacker
    was registered for that extension.

    In case none is found, a ValueError is raised.
    """
    if extract_dir is None:
        extract_dir = os.getcwd()
    extract_dir = os.fspath(extract_dir)
    filename = os.fspath(filename)
    if format is not None:
        try:
            format_info = _UNPACK_FORMATS[format]
        except KeyError:
            raise ValueError("Unknown unpack format '{0}'".format(format)) from None

        func = format_info[1]
        func(filename, extract_dir, **dict(format_info[2]))
    else:
        format = _find_unpack_format(filename)
        if format is None:
            raise ReadError("Unknown archive format '{0}'".format(filename))
        func = _UNPACK_FORMATS[format][1]
        kwargs = dict(_UNPACK_FORMATS[format][2])
        func(filename, extract_dir, **kwargs)


if hasattr(os, 'statvfs'):
    __all__.append('disk_usage')
    _ntuple_diskusage = collections.namedtuple('usage', 'total used free')
    _ntuple_diskusage.total.__doc__ = 'Total space in bytes'
    _ntuple_diskusage.used.__doc__ = 'Used space in bytes'
    _ntuple_diskusage.free.__doc__ = 'Free space in bytes'

    def disk_usage(path):
        """Return disk usage statistics about the given path.

        Returned value is a named tuple with attributes 'total', 'used' and
        'free', which are the amount of total, used and free space, in bytes.
        """
        st = os.statvfs(path)
        free = st.f_bavail * st.f_frsize
        total = st.f_blocks * st.f_frsize
        used = (st.f_blocks - st.f_bfree) * st.f_frsize
        return _ntuple_diskusage(total, used, free)


elif os.name == 'nt':
    import nt
    __all__.append('disk_usage')
    _ntuple_diskusage = collections.namedtuple('usage', 'total used free')

    def disk_usage(path):
        """Return disk usage statistics about the given path.

        Returned values is a named tuple with attributes 'total', 'used' and
        'free', which are the amount of total, used and free space, in bytes.
        """
        total, free = nt._getdiskusage(path)
        used = total - free
        return _ntuple_diskusage(total, used, free)


else:

    def chown(path, user=None, group=None):
        """Change owner user and group of the given path.

    user and group can be the uid/gid or the user/group names, and in that case,
    they are converted to their respective uid/gid.
    """
        if user is None:
            if group is None:
                raise ValueError('user and/or group must be set')
            _user = user
            _group = group
            if user is None:
                _user = -1
            elif isinstance(user, str):
                _user = _get_uid(user)
                if _user is None:
                    raise LookupError('no such user: {!r}'.format(user))
                if group is None:
                    _group = -1
            if not isinstance(group, int):
                _group = _get_gid(group)
                if _group is None:
                    raise LookupError('no such group: {!r}'.format(group))
                os.chown(path, _user, _group)


    def get_terminal_size(fallback=(80, 24)):
        """Get the size of the terminal window.

    For each of the two dimensions, the environment variable, COLUMNS
    and LINES respectively, is checked. If the variable is defined and
    the value is a positive integer, it is used.

    When COLUMNS or LINES is not defined, which is the common case,
    the terminal connected to sys.__stdout__ is queried
    by invoking os.get_terminal_size.

    If the terminal size cannot be successfully queried, either because
    the system doesn't support querying, or because we are not
    connected to a terminal, the value given in fallback parameter
    is used. Fallback defaults to (80, 24) which is the default
    size used by many terminal emulators.

    The value returned is a named tuple of type os.terminal_size.
    """
        try:
            columns = int(os.environ['COLUMNS'])
        except (KeyError, ValueError):
            columns = 0

        try:
            lines = int(os.environ['LINES'])
        except (KeyError, ValueError):
            lines = 0

        if columns <= 0 or lines <= 0:
            try:
                size = os.get_terminal_size(sys.__stdout__.fileno())
            except (AttributeError, ValueError, OSError):
                size = os.terminal_size(fallback)

            if columns <= 0:
                columns = size.columns
            if lines <= 0:
                lines = size.lines
            return os.terminal_size((columns, lines))


    def which(cmd, mode=os.F_OK | os.X_OK, path=None):
        """Given a command, mode, and a PATH string, return the path which
    conforms to the given mode on the PATH, or None if there is no such
    file.

    `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
    of os.environ.get("PATH"), or can be overridden with a custom search
    path.

    """

        def _access_check(fn, mode):
            return os.path.exists(fn) and os.access(fn, mode) and not os.path.isdir(fn)

        if os.path.dirname(cmd):
            if _access_check(cmd, mode):
                return cmd
            return
        if path is None:
            path = os.environ.get('PATH', os.defpath)
        if not path:
            return
        path = path.split(os.pathsep)
        if sys.platform == 'win32':
            if os.curdir not in path:
                path.insert(0, os.curdir)
            pathext = os.environ.get('PATHEXT', '').split(os.pathsep)
            if any(cmd.lower().endswith(ext.lower()) for ext in pathext):
                files = [
                 cmd]
            else:
                files = [cmd + ext for ext in pathext]
        else:
            files = [
             cmd]
        seen = set()
        for dir in path:
            normdir = os.path.normcase(dir)
            if normdir not in seen:
                seen.add(normdir)
                for thefile in files:
                    name = os.path.join(dir, thefile)
                    if _access_check(name, mode):
                        return name