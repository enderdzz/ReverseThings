# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: urllib\request.py
"""An extensible library for opening URLs using a variety of protocols

The simplest way to use this module is to call the urlopen function,
which accepts a string containing a URL or a Request object (described
below).  It opens the URL and returns the results as file-like
object; the returned object has some extra methods described below.

The OpenerDirector manages a collection of Handler objects that do
all the actual work.  Each Handler implements a particular protocol or
option.  The OpenerDirector is a composite object that invokes the
Handlers needed to open the requested URL.  For example, the
HTTPHandler performs HTTP GET and POST requests and deals with
non-error returns.  The HTTPRedirectHandler automatically deals with
HTTP 301, 302, 303 and 307 redirect errors, and the HTTPDigestAuthHandler
deals with digest authentication.

urlopen(url, data=None) -- Basic usage is the same as original
urllib.  pass the url and optionally data to post to an HTTP URL, and
get a file-like object back.  One difference is that you can also pass
a Request instance instead of URL.  Raises a URLError (subclass of
OSError); for HTTP errors, raises an HTTPError, which can also be
treated as a valid response.

build_opener -- Function that creates a new OpenerDirector instance.
Will install the default handlers.  Accepts one or more Handlers as
arguments, either instances or Handler classes that it will
instantiate.  If one of the argument is a subclass of the default
handler, the argument will be installed instead of the default.

install_opener -- Installs a new opener as the default opener.

objects of interest:

OpenerDirector -- Sets up the User Agent as the Python-urllib client and manages
the Handler classes, while dealing with requests and responses.

Request -- An object that encapsulates the state of a request.  The
state can be as simple as the URL.  It can also include extra HTTP
headers, e.g. a User-Agent.

BaseHandler --

internals:
BaseHandler and parent
_call_chain conventions

Example usage:

import urllib.request

# set up authentication info
authinfo = urllib.request.HTTPBasicAuthHandler()
authinfo.add_password(realm='PDQ Application',
                      uri='https://mahler:8092/site-updates.py',
                      user='klem',
                      passwd='geheim$parole')

proxy_support = urllib.request.ProxyHandler({"http" : "http://ahad-haam:3128"})

# build a new opener that adds authentication and caching FTP handlers
opener = urllib.request.build_opener(proxy_support, authinfo,
                                     urllib.request.CacheFTPHandler)

# install it
urllib.request.install_opener(opener)

f = urllib.request.urlopen('http://www.python.org/')
"""
import base64, bisect, email, hashlib, http.client, io, os, posixpath, re, socket, string, sys, time, tempfile, contextlib, warnings
from urllib.error import URLError, HTTPError, ContentTooShortError
from urllib.parse import urlparse, urlsplit, urljoin, unwrap, quote, unquote, splittype, splithost, splitport, splituser, splitpasswd, splitattr, splitquery, splitvalue, splittag, to_bytes, unquote_to_bytes, urlunparse
from urllib.response import addinfourl, addclosehook
try:
    import ssl
except ImportError:
    _have_ssl = False
else:
    _have_ssl = True
__all__ = [
 'Request', 'OpenerDirector', 'BaseHandler', 'HTTPDefaultErrorHandler',
 'HTTPRedirectHandler', 'HTTPCookieProcessor', 'ProxyHandler',
 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm',
 'HTTPPasswordMgrWithPriorAuth', 'AbstractBasicAuthHandler',
 'HTTPBasicAuthHandler', 'ProxyBasicAuthHandler', 'AbstractDigestAuthHandler',
 'HTTPDigestAuthHandler', 'ProxyDigestAuthHandler', 'HTTPHandler',
 'FileHandler', 'FTPHandler', 'CacheFTPHandler', 'DataHandler',
 'UnknownHandler', 'HTTPErrorProcessor',
 'urlopen', 'install_opener', 'build_opener',
 'pathname2url', 'url2pathname', 'getproxies',
 'urlretrieve', 'urlcleanup', 'URLopener', 'FancyURLopener']
__version__ = '%d.%d' % sys.version_info[:2]
_opener = None

def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, *, cafile=None, capath=None, cadefault=False, context=None):
    """Open the URL url, which can be either a string or a Request object.

    *data* must be an object specifying additional data to be sent to
    the server, or None if no such data is needed.  See Request for
    details.

    urllib.request module uses HTTP/1.1 and includes a "Connection:close"
    header in its HTTP requests.

    The optional *timeout* parameter specifies a timeout in seconds for
    blocking operations like the connection attempt (if not specified, the
    global default timeout setting will be used). This only works for HTTP,
    HTTPS and FTP connections.

    If *context* is specified, it must be a ssl.SSLContext instance describing
    the various SSL options. See HTTPSConnection for more details.

    The optional *cafile* and *capath* parameters specify a set of trusted CA
    certificates for HTTPS requests. cafile should point to a single file
    containing a bundle of CA certificates, whereas capath should point to a
    directory of hashed certificate files. More information can be found in
    ssl.SSLContext.load_verify_locations().

    The *cadefault* parameter is ignored.

    This function always returns an object which can work as a context
    manager and has methods such as

    * geturl() - return the URL of the resource retrieved, commonly used to
      determine if a redirect was followed

    * info() - return the meta-information of the page, such as headers, in the
      form of an email.message_from_string() instance (see Quick Reference to
      HTTP Headers)

    * getcode() - return the HTTP status code of the response.  Raises URLError
      on errors.

    For HTTP and HTTPS URLs, this function returns a http.client.HTTPResponse
    object slightly modified. In addition to the three new methods above, the
    msg attribute contains the same information as the reason attribute ---
    the reason phrase returned by the server --- instead of the response
    headers as it is specified in the documentation for HTTPResponse.

    For FTP, file, and data URLs and requests explicitly handled by legacy
    URLopener and FancyURLopener classes, this function returns a
    urllib.response.addinfourl object.

    Note that None may be returned if no handler handles the request (though
    the default installed global OpenerDirector uses UnknownHandler to ensure
    this never happens).

    In addition, if proxy settings are detected (for example, when a *_proxy
    environment variable like http_proxy is set), ProxyHandler is default
    installed and makes sure the requests are handled through the proxy.

    """
    global _opener
    if cafile or capath or cadefault:
        import warnings
        warnings.warn('cafile, capath and cadefault are deprecated, use a custom context instead.', DeprecationWarning, 2)
        if context is not None:
            raise ValueError("You can't pass both context and any of cafile, capath, and cadefault")
        if not _have_ssl:
            raise ValueError('SSL support not available')
        context = ssl.create_default_context((ssl.Purpose.SERVER_AUTH), cafile=cafile,
          capath=capath)
        https_handler = HTTPSHandler(context=context)
        opener = build_opener(https_handler)
    elif context:
        https_handler = HTTPSHandler(context=context)
        opener = build_opener(https_handler)
    elif _opener is None:
        _opener = opener = build_opener()
    else:
        opener = _opener
    return opener.open(url, data, timeout)


def install_opener(opener):
    global _opener
    _opener = opener


_url_tempfiles = []

def urlretrieve(url, filename=None, reporthook=None, data=None):
    """
    Retrieve a URL into a temporary location on disk.

    Requires a URL argument. If a filename is passed, it is used as
    the temporary file location. The reporthook argument should be
    a callable that accepts a block number, a read size, and the
    total file size of the URL target. The data argument should be
    valid URL encoded data.

    If a filename is passed and the URL points to a local resource,
    the result is a copy from local file to new file.

    Returns a tuple containing the path to the newly created
    data file as well as the resulting HTTPMessage object.
    """
    url_type, path = splittype(url)
    with contextlib.closing(urlopen(url, data)) as (fp):
        headers = fp.info()
        if url_type == 'file':
            if not filename:
                return (
                 os.path.normpath(path), headers)
            if filename:
                tfp = open(filename, 'wb')
            else:
                tfp = tempfile.NamedTemporaryFile(delete=False)
                filename = tfp.name
                _url_tempfiles.append(filename)
            with tfp:
                result = (
                 filename, headers)
                bs = 8192
                size = -1
                read = 0
                blocknum = 0
                if 'content-length' in headers:
                    size = int(headers['Content-Length'])
                if reporthook:
                    reporthook(blocknum, bs, size)
                while 1:
                    block = fp.read(bs)
                    if not block:
                        break
                    read += len(block)
                    tfp.write(block)
                    blocknum += 1
                    if reporthook:
                        reporthook(blocknum, bs, size)

    if size >= 0:
        if read < size:
            raise ContentTooShortError('retrieval incomplete: got only %i out of %i bytes' % (
             read, size), result)
        return result


def urlcleanup():
    """Clean up temporary files from urlretrieve calls."""
    global _opener
    for temp_file in _url_tempfiles:
        try:
            os.unlink(temp_file)
        except OSError:
            pass

    del _url_tempfiles[:]
    if _opener:
        _opener = None


_cut_port_re = re.compile(':\\d+$', re.ASCII)

def request_host(request):
    """Return request-host, as defined by RFC 2965.

    Variation from RFC: returned value is lowercased, for convenient
    comparison.

    """
    url = request.full_url
    host = urlparse(url)[1]
    if host == '':
        host = request.get_header('Host', '')
    host = _cut_port_re.sub('', host, 1)
    return host.lower()


class Request:

    def __init__(self, url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None):
        self.full_url = url
        self.headers = {}
        self.unredirected_hdrs = {}
        self._data = None
        self.data = data
        self._tunnel_host = None
        for key, value in headers.items():
            self.add_header(key, value)

        if origin_req_host is None:
            origin_req_host = request_host(self)
        self.origin_req_host = origin_req_host
        self.unverifiable = unverifiable
        if method:
            self.method = method

    @property
    def full_url(self):
        if self.fragment:
            return '{}#{}'.format(self._full_url, self.fragment)
        else:
            return self._full_url

    @full_url.setter
    def full_url(self, url):
        self._full_url = unwrap(url)
        self._full_url, self.fragment = splittag(self._full_url)
        self._parse()

    @full_url.deleter
    def full_url(self):
        self._full_url = None
        self.fragment = None
        self.selector = ''

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data != self._data and data
        if self.has_header('Content-length'):
            self.remove_header('Content-length')

    @data.deleter
    def data(self):
        self.data = None

    def _parse(self):
        self.type, rest = splittype(self._full_url)
        if self.type is None:
            raise ValueError('unknown url type: %r' % self.full_url)
        self.host, self.selector = splithost(rest)
        if self.host:
            self.host = unquote(self.host)

    def get_method(self):
        """Return a string indicating the HTTP request method."""
        default_method = 'POST' if self.data is not None else 'GET'
        return getattr(self, 'method', default_method)

    def get_full_url(self):
        return self.full_url

    def set_proxy(self, host, type):
        if self.type == 'https':
            if not self._tunnel_host:
                self._tunnel_host = self.host
            else:
                self.type = type
                self.selector = self.full_url
            self.host = host

    def has_proxy(self):
        return self.selector == self.full_url

    def add_header(self, key, val):
        self.headers[key.capitalize()] = val

    def add_unredirected_header(self, key, val):
        self.unredirected_hdrs[key.capitalize()] = val

    def has_header(self, header_name):
        return header_name in self.headers or header_name in self.unredirected_hdrs

    def get_header(self, header_name, default=None):
        return self.headers.get(header_name, self.unredirected_hdrs.get(header_name, default))

    def remove_header(self, header_name):
        self.headers.pop(header_name, None)
        self.unredirected_hdrs.pop(header_name, None)

    def header_items(self):
        hdrs = self.unredirected_hdrs.copy()
        hdrs.update(self.headers)
        return list(hdrs.items())


class OpenerDirector:

    def __init__(self):
        client_version = 'Python-urllib/%s' % __version__
        self.addheaders = [('User-agent', client_version)]
        self.handlers = []
        self.handle_open = {}
        self.handle_error = {}
        self.process_response = {}
        self.process_request = {}

    def add_handler(self, handler):
        if not hasattr(handler, 'add_parent'):
            raise TypeError('expected BaseHandler instance, got %r' % type(handler))
        added = False
        for meth in dir(handler):
            if meth in ('redirect_request', 'do_open', 'proxy_open'):
                continue
            i = meth.find('_')
            protocol = meth[:i]
            condition = meth[i + 1:]
            if condition.startswith('error'):
                j = condition.find('_') + i + 1
                kind = meth[j + 1:]
                try:
                    kind = int(kind)
                except ValueError:
                    pass

                lookup = self.handle_error.get(protocol, {})
                self.handle_error[protocol] = lookup
            elif condition == 'open':
                kind = protocol
                lookup = self.handle_open
            elif condition == 'response':
                kind = protocol
                lookup = self.process_response
            else:
                if condition == 'request':
                    kind = protocol
                    lookup = self.process_request
                else:
                    continue
                handlers = lookup.setdefault(kind, [])
                if handlers:
                    bisect.insort(handlers, handler)
                else:
                    handlers.append(handler)
            added = True

        if added:
            bisect.insort(self.handlers, handler)
            handler.add_parent(self)

    def close(self):
        pass

    def _call_chain(self, chain, kind, meth_name, *args):
        handlers = chain.get(kind, ())
        for handler in handlers:
            func = getattr(handler, meth_name)
            result = func(*args)
            if result is not None:
                return result

    def open(self, fullurl, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        if isinstance(fullurl, str):
            req = Request(fullurl, data)
        else:
            req = fullurl
            if data is not None:
                req.data = data
            req.timeout = timeout
            protocol = req.type
            meth_name = protocol + '_request'
            for processor in self.process_request.get(protocol, []):
                meth = getattr(processor, meth_name)
                req = meth(req)

            response = self._open(req, data)
            meth_name = protocol + '_response'
            for processor in self.process_response.get(protocol, []):
                meth = getattr(processor, meth_name)
                response = meth(req, response)

            return response

    def _open(self, req, data=None):
        result = self._call_chain(self.handle_open, 'default', 'default_open', req)
        if result:
            return result
        protocol = req.type
        result = self._call_chain(self.handle_open, protocol, protocol + '_open', req)
        if result:
            return result
        else:
            return self._call_chain(self.handle_open, 'unknown', 'unknown_open', req)

    def error(self, proto, *args):
        if proto in ('http', 'https'):
            dict = self.handle_error['http']
            proto = args[2]
            meth_name = 'http_error_%s' % proto
            http_err = 1
            orig_args = args
        else:
            dict = self.handle_error
            meth_name = proto + '_error'
            http_err = 0
        args = (
         dict, proto, meth_name) + args
        result = (self._call_chain)(*args)
        if result:
            return result
        if http_err:
            args = (
             dict, 'default', 'http_error_default') + orig_args
            return (self._call_chain)(*args)


def build_opener(*handlers):
    """Create an opener object from a list of handlers.

    The opener will use several default handlers, including support
    for HTTP, FTP and when applicable HTTPS.

    If any of the handlers passed as arguments are subclasses of the
    default handlers, the default handlers will not be used.
    """
    opener = OpenerDirector()
    default_classes = [ProxyHandler, UnknownHandler, HTTPHandler,
     HTTPDefaultErrorHandler, HTTPRedirectHandler,
     FTPHandler, FileHandler, HTTPErrorProcessor,
     DataHandler]
    if hasattr(http.client, 'HTTPSConnection'):
        default_classes.append(HTTPSHandler)
    skip = set()
    for klass in default_classes:
        for check in handlers:
            if isinstance(check, type):
                if issubclass(check, klass):
                    skip.add(klass)
                elif isinstance(check, klass):
                    skip.add(klass)

    for klass in skip:
        default_classes.remove(klass)

    for klass in default_classes:
        opener.add_handler(klass())

    for h in handlers:
        if isinstance(h, type):
            h = h()
        opener.add_handler(h)

    return opener


class BaseHandler:
    handler_order = 500

    def add_parent(self, parent):
        self.parent = parent

    def close(self):
        pass

    def __lt__(self, other):
        if not hasattr(other, 'handler_order'):
            return True
        else:
            return self.handler_order < other.handler_order


class HTTPErrorProcessor(BaseHandler):
    """'Process HTTP error responses.'"""
    handler_order = 1000

    def http_response(self, request, response):
        code, msg, hdrs = response.code, response.msg, response.info()
        if not 200 <= code < 300:
            response = self.parent.error('http', request, response, code, msg, hdrs)
        return response

    https_response = http_response


class HTTPDefaultErrorHandler(BaseHandler):

    def http_error_default(self, req, fp, code, msg, hdrs):
        raise HTTPError(req.full_url, code, msg, hdrs, fp)


class HTTPRedirectHandler(BaseHandler):
    max_repeats = 4
    max_redirections = 10

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        """Return a Request or None in response to a redirect.

        This is called by the http_error_30x methods when a
        redirection response is received.  If a redirection should
        take place, return a new Request to allow http_error_30x to
        perform the redirect.  Otherwise, raise HTTPError if no-one
        else should try to handle this url.  Return None if you can't
        but another Handler might.
        """
        m = req.get_method()
        if not (code in (301, 302, 303, 307) and m in ('GET', 'HEAD')):
            if not (code in (301, 302, 303) and m == 'POST'):
                raise HTTPError(req.full_url, code, msg, headers, fp)
            newurl = newurl.replace(' ', '%20')
            CONTENT_HEADERS = ('content-length', 'content-type')
            newheaders = {k:v for k, v in req.headers.items() if k.lower() not in CONTENT_HEADERS}
            return Request(newurl, headers=newheaders,
              origin_req_host=(req.origin_req_host),
              unverifiable=True)

    def http_error_302(self, req, fp, code, msg, headers):
        if 'location' in headers:
            newurl = headers['location']
        else:
            if 'uri' in headers:
                newurl = headers['uri']
            else:
                return
            urlparts = urlparse(newurl)
            if urlparts.scheme not in ('http', 'https', 'ftp', ''):
                raise HTTPError(newurl, code, "%s - Redirection to url '%s' is not allowed" % (msg, newurl), headers, fp)
            if not urlparts.path:
                if urlparts.netloc:
                    urlparts = list(urlparts)
                    urlparts[2] = '/'
                newurl = urlunparse(urlparts)
                newurl = quote(newurl,
                  encoding='iso-8859-1', safe=(string.punctuation))
                newurl = urljoin(req.full_url, newurl)
                new = self.redirect_request(req, fp, code, msg, headers, newurl)
                return new is None and None
            else:
                if hasattr(req, 'redirect_dict'):
                    visited = new.redirect_dict = req.redirect_dict
                    if visited.get(newurl, 0) >= self.max_repeats or len(visited) >= self.max_redirections:
                        raise HTTPError(req.full_url, code, self.inf_msg + msg, headers, fp)
                    else:
                        visited = new.redirect_dict = req.redirect_dict = {}
                    visited[newurl] = visited.get(newurl, 0) + 1
                    fp.read()
                    fp.close()
                return self.parent.open(new, timeout=(req.timeout))

    http_error_301 = http_error_303 = http_error_307 = http_error_302
    inf_msg = 'The HTTP server returned a redirect error that would lead to an infinite loop.\nThe last 30x error message was:\n'


def _parse_proxy(proxy):
    """Return (scheme, user, password, host/port) given a URL or an authority.

    If a URL is supplied, it must have an authority (host:port) component.
    According to RFC 3986, having an authority component means the URL must
    have two slashes after the scheme.
    """
    scheme, r_scheme = splittype(proxy)
    if not r_scheme.startswith('/'):
        scheme = None
        authority = proxy
    elif not r_scheme.startswith('//'):
        raise ValueError('proxy URL with no authority: %r' % proxy)
    else:
        end = r_scheme.find('/', 2)
        if end == -1:
            end = None
        authority = r_scheme[2:end]

    userinfo, hostport = splituser(authority)
    if userinfo is not None:
        user, password = splitpasswd(userinfo)
    else:
        user = password = None
    return (scheme, user, password, hostport)


class ProxyHandler(BaseHandler):
    handler_order = 100

    def __init__(self, proxies=None):
        if proxies is None:
            proxies = getproxies()
        assert hasattr(proxies, 'keys'), 'proxies must be a mapping'
        self.proxies = proxies
        for type, url in proxies.items():
            setattr(self, '%s_open' % type, lambda r, proxy=url, type=type, meth=self.proxy_open: meth(r, proxy, type))

    def proxy_open(self, req, proxy, type):
        orig_type = req.type
        proxy_type, user, password, hostport = _parse_proxy(proxy)
        if proxy_type is None:
            proxy_type = orig_type
        if req.host:
            pass
        if proxy_bypass(req.host):
            return
        if user:
            if password:
                user_pass = '%s:%s' % (unquote(user),
                 unquote(password))
                creds = base64.b64encode(user_pass.encode()).decode('ascii')
                req.add_header('Proxy-authorization', 'Basic ' + creds)
            hostport = unquote(hostport)
            req.set_proxy(hostport, proxy_type)
            return (orig_type == proxy_type or orig_type == 'https') and None
        else:
            return self.parent.open(req, timeout=(req.timeout))


class HTTPPasswordMgr:

    def __init__(self):
        self.passwd = {}

    def add_password(self, realm, uri, user, passwd):
        if isinstance(uri, str):
            uri = [
             uri]
        if realm not in self.passwd:
            self.passwd[realm] = {}
        for default_port in (True, False):
            reduced_uri = tuple(self.reduce_uri(u, default_port) for u in uri)
            self.passwd[realm][reduced_uri] = (user, passwd)

    def find_user_password(self, realm, authuri):
        domains = self.passwd.get(realm, {})
        for default_port in (True, False):
            reduced_authuri = self.reduce_uri(authuri, default_port)
            for uris, authinfo in domains.items():
                for uri in uris:
                    if self.is_suburi(uri, reduced_authuri):
                        return authinfo

        return (None, None)

    def reduce_uri(self, uri, default_port=True):
        """Accept authority or URI and extract only the authority and path."""
        parts = urlsplit(uri)
        if parts[1]:
            scheme = parts[0]
            authority = parts[1]
            path = parts[2] or '/'
        else:
            scheme = None
            authority = uri
            path = '/'
        host, port = splitport(authority)
        if default_port:
            if port is None:
                pass
        if scheme is not None:
            dport = {'http':80, 
             'https':443}.get(scheme)
            if dport is not None:
                authority = '%s:%d' % (host, dport)
            return (authority, path)

    def is_suburi(self, base, test):
        """Check if test is below base in a URI tree

        Both args must be URIs in reduced form.
        """
        if base == test:
            return True
        elif base[0] != test[0]:
            return False
        common = posixpath.commonprefix((base[1], test[1]))
        if len(common) == len(base[1]):
            return True
        else:
            return False


class HTTPPasswordMgrWithDefaultRealm(HTTPPasswordMgr):

    def find_user_password(self, realm, authuri):
        user, password = HTTPPasswordMgr.find_user_password(self, realm, authuri)
        if user is not None:
            return (user, password)
        else:
            return HTTPPasswordMgr.find_user_password(self, None, authuri)


class HTTPPasswordMgrWithPriorAuth(HTTPPasswordMgrWithDefaultRealm):

    def __init__(self, *args, **kwargs):
        self.authenticated = {}
        (super().__init__)(*args, **kwargs)

    def add_password(self, realm, uri, user, passwd, is_authenticated=False):
        self.update_authenticated(uri, is_authenticated)
        if realm is not None:
            super().add_password(None, uri, user, passwd)
        super().add_password(realm, uri, user, passwd)

    def update_authenticated(self, uri, is_authenticated=False):
        if isinstance(uri, str):
            uri = [
             uri]
        for default_port in (True, False):
            for u in uri:
                reduced_uri = self.reduce_uri(u, default_port)
                self.authenticated[reduced_uri] = is_authenticated

    def is_authenticated(self, authuri):
        for default_port in (True, False):
            reduced_authuri = self.reduce_uri(authuri, default_port)
            for uri in self.authenticated:
                if self.is_suburi(uri, reduced_authuri):
                    return self.authenticated[uri]


class AbstractBasicAuthHandler:
    rx = re.compile('(?:.*,)*[ \t]*([^ \t]+)[ \t]+realm=(["\']?)([^"\']*)\\2', re.I)

    def __init__(self, password_mgr=None):
        if password_mgr is None:
            password_mgr = HTTPPasswordMgr()
        self.passwd = password_mgr
        self.add_password = self.passwd.add_password

    def http_error_auth_reqed(self, authreq, host, req, headers):
        authreq = headers.get(authreq, None)
        if authreq:
            scheme = authreq.split()[0]
            if scheme.lower() != 'basic':
                raise ValueError("AbstractBasicAuthHandler does not support the following scheme: '%s'" % scheme)
            else:
                mo = AbstractBasicAuthHandler.rx.search(authreq)
                if mo:
                    scheme, quote, realm = mo.groups()
                    if quote not in ('"', "'"):
                        warnings.warn('Basic Auth Realm was unquoted', UserWarning, 2)
        if scheme.lower() == 'basic':
            return self.retry_http_basic_auth(host, req, realm)

    def retry_http_basic_auth(self, host, req, realm):
        user, pw = self.passwd.find_user_password(realm, host)
        if pw is not None:
            raw = '%s:%s' % (user, pw)
            auth = 'Basic ' + base64.b64encode(raw.encode()).decode('ascii')
            if req.get_header(self.auth_header, None) == auth:
                return
            req.add_unredirected_header(self.auth_header, auth)
            return self.parent.open(req, timeout=(req.timeout))
        else:
            return

    def http_request(self, req):
        if not (hasattr(self.passwd, 'is_authenticated') and self.passwd.is_authenticated(req.full_url)):
            return req
        else:
            if not req.has_header('Authorization'):
                user, passwd = self.passwd.find_user_password(None, req.full_url)
                credentials = '{0}:{1}'.format(user, passwd).encode()
                auth_str = base64.standard_b64encode(credentials).decode()
                req.add_unredirected_header('Authorization', 'Basic {}'.format(auth_str.strip()))
            return req

    def http_response(self, req, response):
        if hasattr(self.passwd, 'is_authenticated'):
            if not 200 <= response.code < 300:
                self.passwd.update_authenticated(req.full_url, True)
            else:
                self.passwd.update_authenticated(req.full_url, False)
            return response

    https_request = http_request
    https_response = http_response


class HTTPBasicAuthHandler(AbstractBasicAuthHandler, BaseHandler):
    auth_header = 'Authorization'

    def http_error_401(self, req, fp, code, msg, headers):
        url = req.full_url
        response = self.http_error_auth_reqed('www-authenticate', url, req, headers)
        return response


class ProxyBasicAuthHandler(AbstractBasicAuthHandler, BaseHandler):
    auth_header = 'Proxy-authorization'

    def http_error_407(self, req, fp, code, msg, headers):
        authority = req.host
        response = self.http_error_auth_reqed('proxy-authenticate', authority, req, headers)
        return response


_randombytes = os.urandom

class AbstractDigestAuthHandler:

    def __init__(self, passwd=None):
        if passwd is None:
            passwd = HTTPPasswordMgr()
        self.passwd = passwd
        self.add_password = self.passwd.add_password
        self.retried = 0
        self.nonce_count = 0
        self.last_nonce = None

    def reset_retry_count(self):
        self.retried = 0

    def http_error_auth_reqed(self, auth_header, host, req, headers):
        authreq = headers.get(auth_header, None)
        if self.retried > 5:
            raise HTTPError(req.full_url, 401, 'digest auth failed', headers, None)
        else:
            self.retried += 1
        if authreq:
            scheme = authreq.split()[0]
            if scheme.lower() == 'digest':
                return self.retry_http_digest_auth(req, authreq)
        if scheme.lower() != 'basic':
            raise ValueError("AbstractDigestAuthHandler does not support the following scheme: '%s'" % scheme)

    def retry_http_digest_auth(self, req, auth):
        token, challenge = auth.split(' ', 1)
        chal = parse_keqv_list(filter(None, parse_http_list(challenge)))
        auth = self.get_authorization(req, chal)
        if auth:
            auth_val = 'Digest %s' % auth
            if req.headers.get(self.auth_header, None) == auth_val:
                return
            req.add_unredirected_header(self.auth_header, auth_val)
            resp = self.parent.open(req, timeout=(req.timeout))
            return resp

    def get_cnonce(self, nonce):
        s = '%s:%s:%s:' % (self.nonce_count, nonce, time.ctime())
        b = s.encode('ascii') + _randombytes(8)
        dig = hashlib.sha1(b).hexdigest()
        return dig[:16]

    def get_authorization(self, req, chal):
        try:
            realm = chal['realm']
            nonce = chal['nonce']
            qop = chal.get('qop')
            algorithm = chal.get('algorithm', 'MD5')
            opaque = chal.get('opaque', None)
        except KeyError:
            return
        else:
            H, KD = self.get_algorithm_impls(algorithm)
            if H is None:
                return
            else:
                user, pw = self.passwd.find_user_password(realm, req.full_url)
                if user is None:
                    return
                if req.data is not None:
                    entdig = self.get_entity_digest(req.data, chal)
                else:
                    entdig = None
                A1 = '%s:%s:%s' % (user, realm, pw)
                A2 = '%s:%s' % (req.get_method(),
                 req.selector)
                if qop == 'auth':
                    if nonce == self.last_nonce:
                        self.nonce_count += 1
                    else:
                        self.nonce_count = 1
                        self.last_nonce = nonce
                    ncvalue = '%08x' % self.nonce_count
                    cnonce = self.get_cnonce(nonce)
                    noncebit = '%s:%s:%s:%s:%s' % (nonce, ncvalue, cnonce, qop, H(A2))
                    respdig = KD(H(A1), noncebit)
                elif qop is None:
                    respdig = KD(H(A1), '%s:%s' % (nonce, H(A2)))
                else:
                    raise URLError("qop '%s' is not supported." % qop)
                base = 'username="%s", realm="%s", nonce="%s", uri="%s", response="%s"' % (
                 user, realm, nonce, req.selector,
                 respdig)
                if opaque:
                    base += ', opaque="%s"' % opaque
                if entdig:
                    base += ', digest="%s"' % entdig
                base += ', algorithm="%s"' % algorithm
                if qop:
                    base += ', qop=auth, nc=%s, cnonce="%s"' % (ncvalue, cnonce)
                return base

    def get_algorithm_impls(self, algorithm):
        if algorithm == 'MD5':
            H = lambda x: hashlib.md5(x.encode('ascii')).hexdigest()
        elif algorithm == 'SHA':
            H = lambda x: hashlib.sha1(x.encode('ascii')).hexdigest()
        else:
            raise ValueError('Unsupported digest authentication algorithm %r' % algorithm)
        KD = lambda s, d: H('%s:%s' % (s, d))
        return (
         H, KD)

    def get_entity_digest(self, data, chal):
        pass


class HTTPDigestAuthHandler(BaseHandler, AbstractDigestAuthHandler):
    r"""'An authentication protocol defined by RFC 2069\n\n    Digest authentication improves on basic authentication because it\n    does not transmit passwords in the clear.\n    '"""
    auth_header = 'Authorization'
    handler_order = 490

    def http_error_401(self, req, fp, code, msg, headers):
        host = urlparse(req.full_url)[1]
        retry = self.http_error_auth_reqed('www-authenticate', host, req, headers)
        self.reset_retry_count()
        return retry


class ProxyDigestAuthHandler(BaseHandler, AbstractDigestAuthHandler):
    auth_header = 'Proxy-Authorization'
    handler_order = 490

    def http_error_407(self, req, fp, code, msg, headers):
        host = req.host
        retry = self.http_error_auth_reqed('proxy-authenticate', host, req, headers)
        self.reset_retry_count()
        return retry


class AbstractHTTPHandler(BaseHandler):

    def __init__(self, debuglevel=0):
        self._debuglevel = debuglevel

    def set_http_debuglevel(self, level):
        self._debuglevel = level

    def _get_content_length(self, request):
        return http.client.HTTPConnection._get_content_length(request.data, request.get_method())

    def do_request_(self, request):
        host = request.host
        if not host:
            raise URLError('no host given')
        if request.data is not None:
            data = request.data
            if isinstance(data, str):
                msg = 'POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.'
                raise TypeError(msg)
            if not request.has_header('Content-type'):
                request.add_unredirected_header('Content-type', 'application/x-www-form-urlencoded')
        if not request.has_header('Content-length'):
            if not request.has_header('Transfer-encoding'):
                content_length = self._get_content_length(request)
                if content_length is not None:
                    request.add_unredirected_header('Content-length', str(content_length))
                else:
                    request.add_unredirected_header('Transfer-encoding', 'chunked')
            sel_host = host
            if request.has_proxy():
                scheme, sel = splittype(request.selector)
                sel_host, sel_path = splithost(sel)
            if not request.has_header('Host'):
                request.add_unredirected_header('Host', sel_host)
            for name, value in self.parent.addheaders:
                name = name.capitalize()
                if not request.has_header(name):
                    request.add_unredirected_header(name, value)

            return request

    def do_open(self, http_class, req, **http_conn_args):
        """Return an HTTPResponse object for the request, using http_class.

        http_class must implement the HTTPConnection API from http.client.
        """
        host = req.host
        if not host:
            raise URLError('no host given')
        h = http_class(host, timeout=req.timeout, **http_conn_args)
        h.set_debuglevel(self._debuglevel)
        headers = dict(req.unredirected_hdrs)
        headers.update({k:v for k, v in req.headers.items() if k not in headers})
        headers['Connection'] = 'close'
        headers = {name.title():val for name, val in headers.items()}
        if req._tunnel_host:
            tunnel_headers = {}
            proxy_auth_hdr = 'Proxy-Authorization'
            if proxy_auth_hdr in headers:
                tunnel_headers[proxy_auth_hdr] = headers[proxy_auth_hdr]
                del headers[proxy_auth_hdr]
            h.set_tunnel((req._tunnel_host), headers=tunnel_headers)
        try:
            try:
                h.request((req.get_method()), (req.selector), (req.data), headers, encode_chunked=(req.has_header('Transfer-encoding')))
            except OSError as err:
                try:
                    raise URLError(err)
                finally:
                    err = None
                    del err

            r = h.getresponse()
        except:
            h.close()
            raise

        if h.sock:
            h.sock.close()
            h.sock = None
        r.url = req.get_full_url()
        r.msg = r.reason
        return r


class HTTPHandler(AbstractHTTPHandler):

    def http_open(self, req):
        return self.do_open(http.client.HTTPConnection, req)

    http_request = AbstractHTTPHandler.do_request_


if hasattr(http.client, 'HTTPSConnection'):

    class HTTPSHandler(AbstractHTTPHandler):

        def __init__(self, debuglevel=0, context=None, check_hostname=None):
            AbstractHTTPHandler.__init__(self, debuglevel)
            self._context = context
            self._check_hostname = check_hostname

        def https_open(self, req):
            return self.do_open((http.client.HTTPSConnection), req, context=(self._context),
              check_hostname=(self._check_hostname))

        https_request = AbstractHTTPHandler.do_request_


    __all__.append('HTTPSHandler')

class HTTPCookieProcessor(BaseHandler):

    def __init__(self, cookiejar=None):
        import http.cookiejar
        if cookiejar is None:
            cookiejar = http.cookiejar.CookieJar()
        self.cookiejar = cookiejar

    def http_request(self, request):
        self.cookiejar.add_cookie_header(request)
        return request

    def http_response(self, request, response):
        self.cookiejar.extract_cookies(response, request)
        return response

    https_request = http_request
    https_response = http_response


class UnknownHandler(BaseHandler):

    def unknown_open(self, req):
        type = req.type
        raise URLError('unknown url type: %s' % type)


def parse_keqv_list(l):
    """Parse list of key=value strings where keys are not duplicated."""
    parsed = {}
    for elt in l:
        k, v = elt.split('=', 1)
        if v[0] == '"':
            if v[(-1)] == '"':
                v = v[1:-1]
            parsed[k] = v

    return parsed


def parse_http_list(s):
    """Parse lists as described by RFC 2068 Section 2.

    In particular, parse comma-separated lists where the elements of
    the list may include quoted-strings.  A quoted-string could
    contain a comma.  A non-quoted string could have quotes in the
    middle.  Neither commas nor quotes count if they are escaped.
    Only double-quotes count, not single-quotes.
    """
    res = []
    part = ''
    escape = quote = False
    for cur in s:
        if escape:
            part += cur
            escape = False
        elif quote:
            if cur == '\\':
                escape = True
                continue
            elif cur == '"':
                quote = False
            else:
                part += cur

        elif cur == ',':
            res.append(part)
            part = ''
            continue
            if cur == '"':
                quote = True
            part += cur

    if part:
        res.append(part)
    return [part.strip() for part in res]


class FileHandler(BaseHandler):

    def file_open(self, req):
        url = req.selector
        if url[:2] == '//':
            if url[2:3] != '/':
                if req.host:
                    if req.host != 'localhost':
                        pass
        if req.host not in self.get_names():
            raise URLError('file:// scheme is supported only on localhost')
        else:
            return self.open_local_file(req)

    names = None

    def get_names(self):
        if FileHandler.names is None:
            try:
                FileHandler.names = tuple(socket.gethostbyname_ex('localhost')[2] + socket.gethostbyname_ex(socket.gethostname())[2])
            except socket.gaierror:
                FileHandler.names = (
                 socket.gethostbyname('localhost'),)

            return FileHandler.names

    def open_local_file(self, req):
        import email.utils, mimetypes
        host = req.host
        filename = req.selector
        localfile = url2pathname(filename)
        try:
            stats = os.stat(localfile)
            size = stats.st_size
            modified = email.utils.formatdate((stats.st_mtime), usegmt=True)
            mtype = mimetypes.guess_type(filename)[0]
            headers = email.message_from_string('Content-type: %s\nContent-length: %d\nLast-modified: %s\n' % (
             mtype or 'text/plain', size, modified))
            if host:
                host, port = splitport(host)
            if host and (port or _safe_gethostbyname(host) in self.get_names()):
                if host:
                    origurl = 'file://' + host + filename
                else:
                    origurl = 'file://' + filename
                return addinfourl(open(localfile, 'rb'), headers, origurl)
        except OSError as exp:
            try:
                raise URLError(exp)
            finally:
                exp = None
                del exp

        raise URLError('file not on local host')


def _safe_gethostbyname(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return


class FTPHandler(BaseHandler):

    def ftp_open(self, req):
        import ftplib, mimetypes
        host = req.host
        if not host:
            raise URLError('ftp error: no host given')
        host, port = splitport(host)
        if port is None:
            port = ftplib.FTP_PORT
        else:
            port = int(port)
        user, host = splituser(host)
        if user:
            user, passwd = splitpasswd(user)
        else:
            passwd = None
        host = unquote(host)
        user = user or ''
        passwd = passwd or ''
        try:
            host = socket.gethostbyname(host)
        except OSError as msg:
            try:
                raise URLError(msg)
            finally:
                msg = None
                del msg

        path, attrs = splitattr(req.selector)
        dirs = path.split('/')
        dirs = list(map(unquote, dirs))
        dirs, file = dirs[:-1], dirs[(-1)]
        if dirs:
            pass
        if not dirs[0]:
            dirs = dirs[1:]
        try:
            fw = self.connect_ftp(user, passwd, host, port, dirs, req.timeout)
            type = file and 'I' or 'D'
            for attr in attrs:
                attr, value = splitvalue(attr)
                if attr.lower() == 'type':
                    type = value in ('a', 'A', 'i', 'I', 'd', 'D') and value.upper()

            fp, retrlen = fw.retrfile(file, type)
            headers = ''
            mtype = mimetypes.guess_type(req.full_url)[0]
            if mtype:
                headers += 'Content-type: %s\n' % mtype
            if retrlen is not None:
                pass
            if retrlen >= 0:
                headers += 'Content-length: %d\n' % retrlen
            headers = email.message_from_string(headers)
            return addinfourl(fp, headers, req.full_url)
        except ftplib.all_errors as exp:
            try:
                exc = URLError('ftp error: %r' % exp)
                raise exc.with_traceback(sys.exc_info()[2])
            finally:
                exp = None
                del exp

    def connect_ftp(self, user, passwd, host, port, dirs, timeout):
        return ftpwrapper(user, passwd, host, port, dirs, timeout, persistent=False)


class CacheFTPHandler(FTPHandler):

    def __init__(self):
        self.cache = {}
        self.timeout = {}
        self.soonest = 0
        self.delay = 60
        self.max_conns = 16

    def setTimeout(self, t):
        self.delay = t

    def setMaxConns(self, m):
        self.max_conns = m

    def connect_ftp(self, user, passwd, host, port, dirs, timeout):
        key = (
         user, host, port, '/'.join(dirs), timeout)
        if key in self.cache:
            self.timeout[key] = time.time() + self.delay
        else:
            self.cache[key] = ftpwrapper(user, passwd, host, port, dirs, timeout)
            self.timeout[key] = time.time() + self.delay
        self.check_cache()
        return self.cache[key]

    def check_cache(self):
        t = time.time()
        if self.soonest <= t:
            for k, v in list(self.timeout.items()):
                if v < t:
                    self.cache[k].close()
                    del self.cache[k]
                    del self.timeout[k]

        self.soonest = min(list(self.timeout.values()))
        if len(self.cache) == self.max_conns:
            for k, v in list(self.timeout.items()):
                if v == self.soonest:
                    del self.cache[k]
                    del self.timeout[k]
                    break

            self.soonest = min(list(self.timeout.values()))

    def clear_cache(self):
        for conn in self.cache.values():
            conn.close()

        self.cache.clear()
        self.timeout.clear()


class DataHandler(BaseHandler):

    def data_open(self, req):
        url = req.full_url
        scheme, data = url.split(':', 1)
        mediatype, data = data.split(',', 1)
        data = unquote_to_bytes(data)
        if mediatype.endswith(';base64'):
            data = base64.decodebytes(data)
            mediatype = mediatype[:-7]
        if not mediatype:
            mediatype = 'text/plain;charset=US-ASCII'
        headers = email.message_from_string('Content-type: %s\nContent-length: %d\n' % (
         mediatype, len(data)))
        return addinfourl(io.BytesIO(data), headers, url)


MAXFTPCACHE = 10
if os.name == 'nt':
    from nturl2path import url2pathname, pathname2url
else:

    def url2pathname(pathname):
        """OS-specific conversion from a relative URL of the 'file' scheme
        to a file system path; not recommended for general use."""
        return unquote(pathname)


    def pathname2url(pathname):
        """OS-specific conversion from a file system path to a relative URL
        of the 'file' scheme; not recommended for general use."""
        return quote(pathname)


ftpcache = {}

class URLopener:
    """"Class to open URLs.\\n    This is a class rather than just a subroutine because we may need\\n    more than one set of global protocol-specific options.\\n    Note -- this is a base class for those who don't want the\\n    automatic handling of errors type 302 (relocated) and 401\\n    (authorization needed).\""""
    _URLopener__tempfiles = None
    version = 'Python-urllib/%s' % __version__

    def __init__(self, proxies=None, **x509):
        msg = '%(class)s style of invoking requests is deprecated. Use newer urlopen functions/methods' % {'class': self.__class__.__name__}
        warnings.warn(msg, DeprecationWarning, stacklevel=3)
        if proxies is None:
            proxies = getproxies()
        assert hasattr(proxies, 'keys'), 'proxies must be a mapping'
        self.proxies = proxies
        self.key_file = x509.get('key_file')
        self.cert_file = x509.get('cert_file')
        self.addheaders = [('User-Agent', self.version), ('Accept', '*/*')]
        self._URLopener__tempfiles = []
        self._URLopener__unlink = os.unlink
        self.tempcache = None
        self.ftpcache = ftpcache

    def __del__(self):
        self.close()

    def close(self):
        self.cleanup()

    def cleanup(self):
        if self._URLopener__tempfiles:
            for file in self._URLopener__tempfiles:
                try:
                    self._URLopener__unlink(file)
                except OSError:
                    pass

            del self._URLopener__tempfiles[:]
        if self.tempcache:
            self.tempcache.clear()

    def addheader(self, *args):
        """Add a header to be used by the HTTP interface only
        e.g. u.addheader('Accept', 'sound/basic')"""
        self.addheaders.append(args)

    def open(self, fullurl, data=None):
        """Use URLopener().open(file) instead of open(file, 'r')."""
        fullurl = unwrap(to_bytes(fullurl))
        fullurl = quote(fullurl, safe="%/:=&?~#+!$,;'@()*[]|")
        if self.tempcache:
            if fullurl in self.tempcache:
                filename, headers = self.tempcache[fullurl]
                fp = open(filename, 'rb')
                return addinfourl(fp, headers, fullurl)
            urltype, url = splittype(fullurl)
            if not urltype:
                urltype = 'file'
            if urltype in self.proxies:
                proxy = self.proxies[urltype]
                urltype, proxyhost = splittype(proxy)
                host, selector = splithost(proxyhost)
                url = (host, fullurl)
            else:
                proxy = None
            name = 'open_' + urltype
            self.type = urltype
            name = name.replace('-', '_')
            if not hasattr(self, name):
                if proxy:
                    return self.open_unknown_proxy(proxy, fullurl, data)
                return self.open_unknown(fullurl, data)
        try:
            if data is None:
                return getattr(self, name)(url)
            else:
                return getattr(self, name)(url, data)
        except (HTTPError, URLError):
            raise
        except OSError as msg:
            try:
                raise OSError('socket error', msg).with_traceback(sys.exc_info()[2])
            finally:
                msg = None
                del msg

    def open_unknown(self, fullurl, data=None):
        """Overridable interface to open unknown URL type."""
        type, url = splittype(fullurl)
        raise OSError('url error', 'unknown url type', type)

    def open_unknown_proxy(self, proxy, fullurl, data=None):
        """Overridable interface to open unknown URL type."""
        type, url = splittype(fullurl)
        raise OSError('url error', 'invalid proxy for %s' % type, proxy)

    def retrieve(self, url, filename=None, reporthook=None, data=None):
        """retrieve(url) returns (filename, headers) for a local object
        or (tempfilename, headers) for a remote object."""
        url = unwrap(to_bytes(url))
        if self.tempcache:
            if url in self.tempcache:
                return self.tempcache[url]
            type, url1 = splittype(url)
            if filename is None:
                pass
        if type and type == 'file':
            try:
                fp = self.open_local_file(url1)
                hdrs = fp.info()
                fp.close()
                return (
                 url2pathname(splithost(url1)[1]), hdrs)
            except OSError as msg:
                try:
                    pass
                finally:
                    msg = None
                    del msg

            fp = self.open(url, data)
            try:
                headers = fp.info()
                if filename:
                    tfp = open(filename, 'wb')
                else:
                    garbage, path = splittype(url)
                    garbage, path = splithost(path or '')
                    path, garbage = splitquery(path or '')
                    path, garbage = splitattr(path or '')
                    suffix = os.path.splitext(path)[1]
                    fd, filename = tempfile.mkstemp(suffix)
                    self._URLopener__tempfiles.append(filename)
                    tfp = os.fdopen(fd, 'wb')
                try:
                    result = (
                     filename, headers)
                    if self.tempcache is not None:
                        self.tempcache[url] = result
                    bs = 8192
                    size = -1
                    read = 0
                    blocknum = 0
                    if 'content-length' in headers:
                        size = int(headers['Content-Length'])
                    if reporthook:
                        reporthook(blocknum, bs, size)
                    while 1:
                        block = fp.read(bs)
                        if not block:
                            break
                        read += len(block)
                        tfp.write(block)
                        blocknum += 1
                        if reporthook:
                            reporthook(blocknum, bs, size)

                finally:
                    tfp.close()

            finally:
                fp.close()

        if size >= 0:
            if read < size:
                raise ContentTooShortError('retrieval incomplete: got only %i out of %i bytes' % (
                 read, size), result)
            return result

    def _open_generic_http(self, connection_factory, url, data):
        """Make an HTTP connection using connection_class.

        This is an internal method that should be called from
        open_http() or open_https().

        Arguments:
        - connection_factory should take a host name and return an
          HTTPConnection instance.
        - url is the url to retrieval or a host, relative-path pair.
        - data is payload for a POST request or None.
        """
        user_passwd = None
        proxy_passwd = None
        if isinstance(url, str):
            host, selector = splithost(url)
            if host:
                user_passwd, host = splituser(host)
                host = unquote(host)
            realhost = host
        else:
            host, selector = url
            proxy_passwd, host = splituser(host)
            urltype, rest = splittype(selector)
            url = rest
            user_passwd = None
        if urltype.lower() != 'http':
            realhost = None
        else:
            realhost, rest = splithost(rest)
            if realhost:
                user_passwd, realhost = splituser(realhost)
            if user_passwd:
                selector = '%s://%s%s' % (urltype, realhost, rest)
            if proxy_bypass(realhost):
                host = realhost
            if not host:
                raise OSError('http error', 'no host given')
            if proxy_passwd:
                proxy_passwd = unquote(proxy_passwd)
                proxy_auth = base64.b64encode(proxy_passwd.encode()).decode('ascii')
            else:
                proxy_auth = None
            if user_passwd:
                user_passwd = unquote(user_passwd)
                auth = base64.b64encode(user_passwd.encode()).decode('ascii')
            else:
                auth = None
            http_conn = connection_factory(host)
            headers = {}
            if proxy_auth:
                headers['Proxy-Authorization'] = 'Basic %s' % proxy_auth
            if auth:
                headers['Authorization'] = 'Basic %s' % auth
            if realhost:
                headers['Host'] = realhost
            headers['Connection'] = 'close'
            for header, value in self.addheaders:
                headers[header] = value

            if data is not None:
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
                http_conn.request('POST', selector, data, headers)
            else:
                http_conn.request('GET', selector, headers=headers)
            try:
                response = http_conn.getresponse()
            except http.client.BadStatusLine:
                raise URLError('http protocol error: bad status line')

            if not 200 <= response.status < 300:
                return addinfourl(response, response.msg, 'http:' + url, response.status)
            return self.http_error(url, response.fp, response.status, response.reason, response.msg, data)

    def open_http(self, url, data=None):
        """Use HTTP protocol."""
        return self._open_generic_http(http.client.HTTPConnection, url, data)

    def http_error(self, url, fp, errcode, errmsg, headers, data=None):
        """Handle http errors.

        Derived class can override this, or provide specific handlers
        named http_error_DDD where DDD is the 3-digit error code."""
        name = 'http_error_%d' % errcode
        if hasattr(self, name):
            method = getattr(self, name)
            if data is None:
                result = method(url, fp, errcode, errmsg, headers)
            else:
                result = method(url, fp, errcode, errmsg, headers, data)
            return result and result
        else:
            return self.http_error_default(url, fp, errcode, errmsg, headers)

    def http_error_default(self, url, fp, errcode, errmsg, headers):
        """Default error handler: close the connection and raise OSError."""
        fp.close()
        raise HTTPError(url, errcode, errmsg, headers, None)

    if _have_ssl:

        def _https_connection(self, host):
            return http.client.HTTPSConnection(host, key_file=(self.key_file),
              cert_file=(self.cert_file))

        def open_https(self, url, data=None):
            """Use HTTPS protocol."""
            return self._open_generic_http(self._https_connection, url, data)

    def open_file(self, url):
        """Use local file or FTP depending on form of URL."""
        if not isinstance(url, str):
            raise URLError('file error: proxy support for file protocol currently not implemented')
        if url[:2] == '//':
            if url[2:3] != '/':
                pass
        if url[2:12].lower() != 'localhost/':
            raise ValueError('file:// scheme is supported only on localhost')
        else:
            return self.open_local_file(url)

    def open_local_file(self, url):
        """Use local file."""
        import email.utils, mimetypes
        host, file = splithost(url)
        localname = url2pathname(file)
        try:
            stats = os.stat(localname)
        except OSError as e:
            try:
                raise URLError(e.strerror, e.filename)
            finally:
                e = None
                del e

        size = stats.st_size
        modified = email.utils.formatdate((stats.st_mtime), usegmt=True)
        mtype = mimetypes.guess_type(url)[0]
        headers = email.message_from_string('Content-Type: %s\nContent-Length: %d\nLast-modified: %s\n' % (
         mtype or 'text/plain', size, modified))
        if not host:
            urlfile = file
            if file[:1] == '/':
                urlfile = 'file://' + file
            return addinfourl(open(localname, 'rb'), headers, urlfile)
        host, port = splitport(host)
        if not port:
            if socket.gethostbyname(host) in (localhost(),) + thishost():
                urlfile = file
                if file[:1] == '/':
                    urlfile = 'file://' + file
                elif file[:2] == './':
                    raise ValueError('local file url may start with / or file:. Unknown url of type: %s' % url)
                return addinfourl(open(localname, 'rb'), headers, urlfile)
            raise URLError('local file error: not on local host')

    def open_ftp(self, url):
        """Use FTP protocol."""
        if not isinstance(url, str):
            raise URLError('ftp error: proxy support for ftp protocol currently not implemented')
        import mimetypes
        host, path = splithost(url)
        if not host:
            raise URLError('ftp error: no host given')
        host, port = splitport(host)
        user, host = splituser(host)
        if user:
            user, passwd = splitpasswd(user)
        else:
            passwd = None
        host = unquote(host)
        user = unquote(user or '')
        passwd = unquote(passwd or '')
        host = socket.gethostbyname(host)
        if not port:
            import ftplib
            port = ftplib.FTP_PORT
        else:
            port = int(port)
        path, attrs = splitattr(path)
        path = unquote(path)
        dirs = path.split('/')
        dirs, file = dirs[:-1], dirs[(-1)]
        if dirs:
            pass
        if not dirs[0]:
            dirs = dirs[1:]
        if dirs:
            if not dirs[0]:
                dirs[0] = '/'
            key = (
             user, host, port, '/'.join(dirs))
            if len(self.ftpcache) > MAXFTPCACHE:
                for k in list(self.ftpcache):
                    if k != key:
                        v = self.ftpcache[k]
                        del self.ftpcache[k]
                        v.close()

        try:
            if key not in self.ftpcache:
                self.ftpcache[key] = ftpwrapper(user, passwd, host, port, dirs)
            if not file:
                type = 'D'
            else:
                type = 'I'
            for attr in attrs:
                attr, value = splitvalue(attr)
                if attr.lower() == 'type':
                    type = value in ('a', 'A', 'i', 'I', 'd', 'D') and value.upper()

            fp, retrlen = self.ftpcache[key].retrfile(file, type)
            mtype = mimetypes.guess_type('ftp:' + url)[0]
            headers = ''
            if mtype:
                headers += 'Content-Type: %s\n' % mtype
            if retrlen is not None:
                pass
            if retrlen >= 0:
                headers += 'Content-Length: %d\n' % retrlen
            headers = email.message_from_string(headers)
            return addinfourl(fp, headers, 'ftp:' + url)
        except ftperrors() as exp:
            try:
                raise URLError('ftp error %r' % exp).with_traceback(sys.exc_info()[2])
            finally:
                exp = None
                del exp

    def open_data(self, url, data=None):
        """Use "data" URL."""
        if not isinstance(url, str):
            raise URLError('data error: proxy support for data protocol currently not implemented')
        try:
            type, data = url.split(',', 1)
        except ValueError:
            raise OSError('data error', 'bad data URL')

        if not type:
            type = 'text/plain;charset=US-ASCII'
        semi = type.rfind(';')
        if semi >= 0:
            if '=' not in type[semi:]:
                encoding = type[semi + 1:]
                type = type[:semi]
            else:
                encoding = ''
            msg = []
            msg.append('Date: %s' % time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(time.time())))
            msg.append('Content-type: %s' % type)
            if encoding == 'base64':
                data = base64.decodebytes(data.encode('ascii')).decode('latin-1')
            else:
                data = unquote(data)
            msg.append('Content-Length: %d' % len(data))
            msg.append('')
            msg.append(data)
            msg = '\n'.join(msg)
            headers = email.message_from_string(msg)
            f = io.StringIO(msg)
            return addinfourl(f, headers, url)


class FancyURLopener(URLopener):
    """'Derived class with handlers for errors we can handle (perhaps).'"""

    def __init__(self, *args, **kwargs):
        (URLopener.__init__)(self, *args, **kwargs)
        self.auth_cache = {}
        self.tries = 0
        self.maxtries = 10

    def http_error_default(self, url, fp, errcode, errmsg, headers):
        """Default error handling -- don't raise an exception."""
        return addinfourl(fp, headers, 'http:' + url, errcode)

    def http_error_302(self, url, fp, errcode, errmsg, headers, data=None):
        """Error 302 -- relocated (temporarily)."""
        self.tries += 1
        try:
            if self.maxtries:
                if self.tries >= self.maxtries:
                    if hasattr(self, 'http_error_500'):
                        meth = self.http_error_500
                    else:
                        meth = self.http_error_default
                    return meth(url, fp, 500, 'Internal Server Error: Redirect Recursion', headers)
                result = self.redirect_internal(url, fp, errcode, errmsg, headers, data)
            return result
        finally:
            self.tries = 0

    def redirect_internal(self, url, fp, errcode, errmsg, headers, data):
        if 'location' in headers:
            newurl = headers['location']
        else:
            if 'uri' in headers:
                newurl = headers['uri']
            else:
                return
            fp.close()
            newurl = urljoin(self.type + ':' + url, newurl)
            urlparts = urlparse(newurl)
            if urlparts.scheme not in ('http', 'https', 'ftp', ''):
                raise HTTPError(newurl, errcode, errmsg + " Redirection to url '%s' is not allowed." % newurl, headers, fp)
            return self.open(newurl)

    def http_error_301(self, url, fp, errcode, errmsg, headers, data=None):
        """Error 301 -- also relocated (permanently)."""
        return self.http_error_302(url, fp, errcode, errmsg, headers, data)

    def http_error_303(self, url, fp, errcode, errmsg, headers, data=None):
        """Error 303 -- also relocated (essentially identical to 302)."""
        return self.http_error_302(url, fp, errcode, errmsg, headers, data)

    def http_error_307(self, url, fp, errcode, errmsg, headers, data=None):
        """Error 307 -- relocated, but turn POST into error."""
        if data is None:
            return self.http_error_302(url, fp, errcode, errmsg, headers, data)
        else:
            return self.http_error_default(url, fp, errcode, errmsg, headers)

    def http_error_401(self, url, fp, errcode, errmsg, headers, data=None, retry=False):
        """Error 401 -- authentication required.
        This function supports Basic authentication only."""
        if 'www-authenticate' not in headers:
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        stuff = headers['www-authenticate']
        match = re.match('[ \t]*([^ \t]+)[ \t]+realm="([^"]*)"', stuff)
        if not match:
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        scheme, realm = match.groups()
        if scheme.lower() != 'basic':
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        if not retry:
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        name = 'retry_' + self.type + '_basic_auth'
        if data is None:
            return getattr(self, name)(url, realm)
        else:
            return getattr(self, name)(url, realm, data)

    def http_error_407(self, url, fp, errcode, errmsg, headers, data=None, retry=False):
        """Error 407 -- proxy authentication required.
        This function supports Basic authentication only."""
        if 'proxy-authenticate' not in headers:
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        stuff = headers['proxy-authenticate']
        match = re.match('[ \t]*([^ \t]+)[ \t]+realm="([^"]*)"', stuff)
        if not match:
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        scheme, realm = match.groups()
        if scheme.lower() != 'basic':
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        if not retry:
            URLopener.http_error_default(self, url, fp, errcode, errmsg, headers)
        name = 'retry_proxy_' + self.type + '_basic_auth'
        if data is None:
            return getattr(self, name)(url, realm)
        else:
            return getattr(self, name)(url, realm, data)

    def retry_proxy_http_basic_auth(self, url, realm, data=None):
        host, selector = splithost(url)
        newurl = 'http://' + host + selector
        proxy = self.proxies['http']
        urltype, proxyhost = splittype(proxy)
        proxyhost, proxyselector = splithost(proxyhost)
        i = proxyhost.find('@') + 1
        proxyhost = proxyhost[i:]
        user, passwd = self.get_user_passwd(proxyhost, realm, i)
        if not user:
            if not passwd:
                pass
            return
        proxyhost = '%s:%s@%s' % (quote(user, safe=''),
         quote(passwd, safe=''), proxyhost)
        self.proxies['http'] = 'http://' + proxyhost + proxyselector
        if data is None:
            return self.open(newurl)
        else:
            return self.open(newurl, data)

    def retry_proxy_https_basic_auth(self, url, realm, data=None):
        host, selector = splithost(url)
        newurl = 'https://' + host + selector
        proxy = self.proxies['https']
        urltype, proxyhost = splittype(proxy)
        proxyhost, proxyselector = splithost(proxyhost)
        i = proxyhost.find('@') + 1
        proxyhost = proxyhost[i:]
        user, passwd = self.get_user_passwd(proxyhost, realm, i)
        if not user:
            if not passwd:
                pass
            return
        proxyhost = '%s:%s@%s' % (quote(user, safe=''),
         quote(passwd, safe=''), proxyhost)
        self.proxies['https'] = 'https://' + proxyhost + proxyselector
        if data is None:
            return self.open(newurl)
        else:
            return self.open(newurl, data)

    def retry_http_basic_auth(self, url, realm, data=None):
        host, selector = splithost(url)
        i = host.find('@') + 1
        host = host[i:]
        user, passwd = self.get_user_passwd(host, realm, i)
        if not user:
            if not passwd:
                pass
            return
        host = '%s:%s@%s' % (quote(user, safe=''),
         quote(passwd, safe=''), host)
        newurl = 'http://' + host + selector
        if data is None:
            return self.open(newurl)
        else:
            return self.open(newurl, data)

    def retry_https_basic_auth(self, url, realm, data=None):
        host, selector = splithost(url)
        i = host.find('@') + 1
        host = host[i:]
        user, passwd = self.get_user_passwd(host, realm, i)
        if not user:
            if not passwd:
                pass
            return
        host = '%s:%s@%s' % (quote(user, safe=''),
         quote(passwd, safe=''), host)
        newurl = 'https://' + host + selector
        if data is None:
            return self.open(newurl)
        else:
            return self.open(newurl, data)

    def get_user_passwd(self, host, realm, clear_cache=0):
        key = realm + '@' + host.lower()
        if key in self.auth_cache:
            if clear_cache:
                del self.auth_cache[key]
            else:
                return self.auth_cache[key]
            user, passwd = self.prompt_user_passwd(host, realm)
            if user or passwd:
                self.auth_cache[key] = (
                 user, passwd)
            return (user, passwd)

    def prompt_user_passwd(self, host, realm):
        """Override this in a GUI environment!"""
        import getpass
        try:
            user = input('Enter username for %s at %s: ' % (realm, host))
            passwd = getpass.getpass('Enter password for %s in %s at %s: ' % (
             user, realm, host))
            return (
             user, passwd)
        except KeyboardInterrupt:
            print()
            return (None, None)


_localhost = None

def localhost():
    """Return the IP address of the magic hostname 'localhost'."""
    global _localhost
    if _localhost is None:
        _localhost = socket.gethostbyname('localhost')
    return _localhost


_thishost = None

def thishost():
    """Return the IP addresses of the current host."""
    global _thishost
    if _thishost is None:
        try:
            _thishost = tuple(socket.gethostbyname_ex(socket.gethostname())[2])
        except socket.gaierror:
            _thishost = tuple(socket.gethostbyname_ex('localhost')[2])

        return _thishost


_ftperrors = None

def ftperrors():
    """Return the set of errors raised by the FTP class."""
    global _ftperrors
    if _ftperrors is None:
        import ftplib
        _ftperrors = ftplib.all_errors
    return _ftperrors


_noheaders = None

def noheaders():
    """Return an empty email Message object."""
    global _noheaders
    if _noheaders is None:
        _noheaders = email.message_from_string('')
    return _noheaders


class ftpwrapper:
    """'Class used by open_ftp() for cache of open FTP connections.'"""

    def __init__(self, user, passwd, host, port, dirs, timeout=None, persistent=True):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.dirs = dirs
        self.timeout = timeout
        self.refcount = 0
        self.keepalive = persistent
        try:
            self.init()
        except:
            self.close()
            raise

    def init(self):
        import ftplib
        self.busy = 0
        self.ftp = ftplib.FTP()
        self.ftp.connect(self.host, self.port, self.timeout)
        self.ftp.login(self.user, self.passwd)
        _target = '/'.join(self.dirs)
        self.ftp.cwd(_target)

    def retrfile(self, file, type):
        import ftplib
        self.endtransfer()
        if type in ('d', 'D'):
            cmd = 'TYPE A'
            isdir = 1
        else:
            cmd = 'TYPE ' + type
            isdir = 0
        try:
            self.ftp.voidcmd(cmd)
        except ftplib.all_errors:
            self.init()
            self.ftp.voidcmd(cmd)

        conn = None
        if file:
            pass
        if not isdir:
            try:
                cmd = 'RETR ' + file
                conn, retrlen = self.ftp.ntransfercmd(cmd)
            except ftplib.error_perm as reason:
                try:
                    if str(reason)[:3] != '550':
                        raise URLError('ftp error: %r' % reason).with_traceback(sys.exc_info()[2])
                finally:
                    reason = None
                    del reason

            if not conn:
                self.ftp.voidcmd('TYPE A')
                if file:
                    pwd = self.ftp.pwd()
                    try:
                        try:
                            self.ftp.cwd(file)
                        except ftplib.error_perm as reason:
                            try:
                                raise URLError('ftp error: %r' % reason) from reason
                            finally:
                                reason = None
                                del reason

                    finally:
                        self.ftp.cwd(pwd)

                    cmd = 'LIST ' + file
                else:
                    cmd = 'LIST'
                conn, retrlen = self.ftp.ntransfercmd(cmd)
            self.busy = 1
            ftpobj = addclosehook(conn.makefile('rb'), self.file_close)
            self.refcount += 1
            conn.close()
            return (
             ftpobj, retrlen)

    def endtransfer(self):
        self.busy = 0

    def close(self):
        self.keepalive = False
        if self.refcount <= 0:
            self.real_close()

    def file_close(self):
        self.endtransfer()
        self.refcount -= 1
        if self.refcount <= 0:
            pass
        if not self.keepalive:
            self.real_close()

    def real_close(self):
        self.endtransfer()
        try:
            self.ftp.close()
        except ftperrors():
            pass


def getproxies_environment():
    """Return a dictionary of scheme -> proxy server URL mappings.

    Scan the environment for variables named <scheme>_proxy;
    this seems to be the standard convention.  If you need a
    different way, you can pass a proxies dictionary to the
    [Fancy]URLopener constructor.

    """
    proxies = {}
    for name, value in os.environ.items():
        name = name.lower()
        if value:
            proxies[name[:-6]] = name[-6:] == '_proxy' and value

    if 'REQUEST_METHOD' in os.environ:
        proxies.pop('http', None)
    for name, value in os.environ.items():
        if name[-6:] == '_proxy':
            name = name.lower()
            if value:
                proxies[name[:-6]] = value
            else:
                proxies.pop(name[:-6], None)

    return proxies


def proxy_bypass_environment(host, proxies=None):
    """Test if proxies should not be used for a particular host.

    Checks the proxy dict for the value of no_proxy, which should
    be a list of comma separated DNS suffixes, or '*' for all hosts.

    """
    if proxies is None:
        proxies = getproxies_environment()
    try:
        no_proxy = proxies['no']
    except KeyError:
        return 0
    else:
        if no_proxy == '*':
            return 1
        else:
            hostonly, port = splitport(host)
            no_proxy_list = [proxy.strip() for proxy in no_proxy.split(',')]
            for name in no_proxy_list:
                if name:
                    name = name.lstrip('.')
                    name = re.escape(name)
                    pattern = '(.+\\.)?%s$' % name
                    if re.match(pattern, hostonly, re.I) or re.match(pattern, host, re.I):
                        return 1

            return 0


def _proxy_bypass_macosx_sysconf(host, proxy_settings):
    """
    Return True iff this host shouldn't be accessed using a proxy

    This function uses the MacOSX framework SystemConfiguration
    to fetch the proxy information.

    proxy_settings come from _scproxy._get_proxy_settings or get mocked ie:
    { 'exclude_simple': bool,
      'exceptions': ['foo.bar', '*.bar.com', '127.0.0.1', '10.1', '10.0/16']
    }
    """
    from fnmatch import fnmatch
    hostonly, port = splitport(host)

    def ip2num(ipAddr):
        parts = ipAddr.split('.')
        parts = list(map(int, parts))
        if len(parts) != 4:
            parts = (parts + [0, 0, 0, 0])[:4]
        return parts[0] << 24 | parts[1] << 16 | parts[2] << 8 | parts[3]

    if '.' not in host:
        if proxy_settings['exclude_simple']:
            pass
        return True
    else:
        hostIP = None
        for value in proxy_settings.get('exceptions', ()):
            if not value:
                continue
            m = re.match('(\\d+(?:\\.\\d+)*)(/\\d+)?', value)
            if m is not None:
                pass
            if hostIP is None:
                try:
                    hostIP = socket.gethostbyname(hostonly)
                    hostIP = ip2num(hostIP)
                except OSError:
                    continue

                base = ip2num(m.group(1))
                mask = m.group(2)
                if mask is None:
                    mask = 8 * (m.group(1).count('.') + 1)
                else:
                    mask = int(mask[1:])
                mask = 32 - mask
                if hostIP >> mask == base >> mask:
                    return True
            elif fnmatch(host, value):
                return True

        return False


if sys.platform == 'darwin':
    from _scproxy import _get_proxy_settings, _get_proxies

    def proxy_bypass_macosx_sysconf(host):
        proxy_settings = _get_proxy_settings()
        return _proxy_bypass_macosx_sysconf(host, proxy_settings)


    def getproxies_macosx_sysconf():
        """Return a dictionary of scheme -> proxy server URL mappings.

        This function uses the MacOSX framework SystemConfiguration
        to fetch the proxy information.
        """
        return _get_proxies()


    def proxy_bypass(host):
        """Return True, if host should be bypassed.

        Checks proxy settings gathered from the environment, if specified,
        or from the MacOSX framework SystemConfiguration.

        """
        proxies = getproxies_environment()
        if proxies:
            return proxy_bypass_environment(host, proxies)
        else:
            return proxy_bypass_macosx_sysconf(host)


    def getproxies():
        return getproxies_environment() or getproxies_macosx_sysconf()


elif os.name == 'nt':

    def getproxies_registry():
        """Return a dictionary of scheme -> proxy server URL mappings.

        Win32 uses the registry to store proxies.

        """
        proxies = {}
        try:
            import winreg
        except ImportError:
            return proxies
        else:
            try:
                internetSettings = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings')
                proxyEnable = winreg.QueryValueEx(internetSettings, 'ProxyEnable')[0]
                if proxyEnable:
                    proxyServer = str(winreg.QueryValueEx(internetSettings, 'ProxyServer')[0])
                    if '=' in proxyServer:
                        for p in proxyServer.split(';'):
                            protocol, address = p.split('=', 1)
                            if not re.match('^([^/:]+)://', address):
                                address = '%s://%s' % (protocol, address)
                            proxies[protocol] = address

                    elif proxyServer[:5] == 'http:':
                        proxies['http'] = proxyServer
                    else:
                        proxies['http'] = 'http://%s' % proxyServer
                        proxies['https'] = 'https://%s' % proxyServer
                        proxies['ftp'] = 'ftp://%s' % proxyServer
                internetSettings.Close()
            except (OSError, ValueError, TypeError):
                pass

            return proxies


    def getproxies():
        """Return a dictionary of scheme -> proxy server URL mappings.

        Returns settings gathered from the environment, if specified,
        or the registry.

        """
        return getproxies_environment() or getproxies_registry()


    def proxy_bypass_registry(host):
        try:
            import winreg
        except ImportError:
            return 0
        else:
            try:
                internetSettings = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings')
                proxyEnable = winreg.QueryValueEx(internetSettings, 'ProxyEnable')[0]
                proxyOverride = str(winreg.QueryValueEx(internetSettings, 'ProxyOverride')[0])
            except OSError:
                return 0
            else:
                if not (proxyEnable and proxyOverride):
                    return 0
                else:
                    rawHost, port = splitport(host)
                    host = [rawHost]
                    try:
                        addr = socket.gethostbyname(rawHost)
                        if addr != rawHost:
                            host.append(addr)
                    except OSError:
                        pass

                    try:
                        fqdn = socket.getfqdn(rawHost)
                        if fqdn != rawHost:
                            host.append(fqdn)
                    except OSError:
                        pass

                    proxyOverride = proxyOverride.split(';')
                    for test in proxyOverride:
                        if test == '<local>':
                            if '.' not in rawHost:
                                return 1
                            test = test.replace('.', '\\.')
                            test = test.replace('*', '.*')
                            test = test.replace('?', '.')
                            for val in host:
                                if re.match(test, val, re.I):
                                    return 1

                    return 0


    def proxy_bypass(host):
        """Return True, if host should be bypassed.

        Checks proxy settings gathered from the environment, if specified,
        or the registry.

        """
        proxies = getproxies_environment()
        if proxies:
            return proxy_bypass_environment(host, proxies)
        else:
            return proxy_bypass_registry(host)


else:
    getproxies = getproxies_environment
    proxy_bypass = proxy_bypass_environment