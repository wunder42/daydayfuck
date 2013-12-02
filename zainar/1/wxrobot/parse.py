
import lxml.objectify
import httplib
import urlparse

__all__ = ('ParseError', 'InvalidFeed', 'from_string', 'from_url', 'from_file', 'parse_date')

class Proxy(object):
    __slots__ = ('__dict__',)

    def __init__(self, instance):
        object.__setattr__(self, '__instance__', instance)

    def _get_current_object(self):
        """
        Return the current object.  This is useful if you want the real object
        behind the proxy at a time for performance reasons or because you want
        to pass the object into a different context.
        """
        return self.__instance__
    _current_object = property(_get_current_object)

    def __dict__(self):
        try:
            return self._current_object.__dict__
        except RuntimeError:
            return AttributeError('__dict__')
    __dict__ = property(__dict__)

    def __repr__(self):
        try:
            obj = self._current_object
        except RuntimeError:
            return '<%s unbound>' % self.__class__.__name__
        return repr(obj)

    def __nonzero__(self):
        try:
            return bool(self._current_object)
        except RuntimeError:
            return False

    def __unicode__(self):
        try:
            return unicode(self.__current_oject)
        except RuntimeError:
            return repr(self)

    def __dir__(self):
        try:
            return dir(self._current_object)
        except RuntimeError:
            return []

    __getattr__ = lambda x, i, j=None: getattr(x._current_object, i, j)
    __setattr__ = lambda x, i, j: setattr(x._current_object, i, j)

    def __setitem__(self, key, value):
        self._current_object[key] = value

    def __delitem__(self, key):
        del self._current_object[key]

    def __setslice__(self, i, j, seq):
        self._current_object[i:j] = seq

    def __delslice__(self, i, j):
        del self._current_object[i:j]

    __delattr__ = lambda x, n: delattr(x._current_object, n)
    __str__ = lambda x: unicode(x._current_object)
    __unicode__ = lambda x: unicode(x._current_object)
    __lt__ = lambda x, o: x._current_object < o
    __le__ = lambda x, o: x._current_object <= o
    __eq__ = lambda x, o: x._current_object == o
    __ne__ = lambda x, o: x._current_object != o
    __gt__ = lambda x, o: x._current_object > o
    __ge__ = lambda x, o: x._current_object >= o
    __cmp__ = lambda x, o: cmp(x._current_object, o)
    __hash__ = lambda x: hash(x._current_object)
    # attributes are currently not callable
    # __call__ = lambda x, *a, **kw: x._current_object(*a, **kw)
    __len__ = lambda x: len(x._current_object)
    __getitem__ = lambda x, i: x._current_object[i]
    __iter__ = lambda x: iter(x._current_object)
    __contains__ = lambda x, i: i in x._current_object
    __getslice__ = lambda x, i, j: x._current_object[i:j]
    __add__ = lambda x, o: x._current_object + o
    __sub__ = lambda x, o: x._current_object - o
    __mul__ = lambda x, o: x._current_object * o
    __floordiv__ = lambda x, o: x._current_object // o
    __mod__ = lambda x, o: x._current_object % o
    __divmod__ = lambda x, o: x._current_object.__divmod__(o)
    __pow__ = lambda x, o: x._current_object ** o
    __lshift__ = lambda x, o: x._current_object << o
    __rshift__ = lambda x, o: x._current_object >> o
    __and__ = lambda x, o: x._current_object & o
    __xor__ = lambda x, o: x._current_object ^ o
    __or__ = lambda x, o: x._current_object | o
    __div__ = lambda x, o: x._current_object.__div__(o)
    __truediv__ = lambda x, o: x._current_object.__truediv__(o)
    __neg__ = lambda x: -(x._current_object)
    __pos__ = lambda x: +(x._current_object)
    __abs__ = lambda x: abs(x._current_object)
    __invert__ = lambda x: ~(x._current_object)
    __complex__ = lambda x: complex(x._current_object)
    __int__ = lambda x: int(x._current_object)
    __long__ = lambda x: long(x._current_object)
    __float__ = lambda x: float(x._current_object)
    __oct__ = lambda x: oct(x._current_object)
    __hex__ = lambda x: hex(x._current_object)
    __index__ = lambda x: x._current_object.__index__()
    __coerce__ = lambda x, o: x.__coerce__(x, o)
    __enter__ = lambda x: x.__enter__()
    __exit__ = lambda x, *a, **kw: x.__exit__(*a, **kw)

class InvalidFeed(Exception): pass

class BetterObject(object):
    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self)

class Tag(BetterObject, Proxy):
    def __unicode__(self):
        return unicode(self.__instance__).strip()

class Author(BetterObject):
    def __init__(self, name=None, email=None, link=None):
        self.name, self.email, self.link = name, email, link

    def __str__(self):
        if self.email:
            return "%s <%s>" % (self.name, self.email)
        elif self.name:
            return str(self.name)
        return str(self.link)

class Enclosure(BetterObject):
    media = None
    
    def __init__(self, href, type=None):
        self.type, self.href = type and unicode(type) or None, unicode(href)
    
    def __str__(self):
        if self.type:
            return '%s:%s' % (self.type, self.href)
        return self.href

    @property
    def link(self):
        return self.href

class Image(Enclosure):
    media = 'image'

class Thumbnail(Image):
    media = 'thumbnail'

class Feed(BetterObject):
    __feed__ = ''
    
    author = Author()
    is_valid = False
    
    def __init__(self, node):
        self._xml = node
        if not self.is_valid:
            raise InvalidFeed
    
    def __str__(self):
        return self.feed

    def __getattr__(self, attr, default=None):
        result = getattr(self._xml, attr, default)
        if result is not None:
            result = Tag(result)
        return result
    
    @property
    def entries(self):
        raise NotImplementedError
    
    @property
    def feed(self):
        return self.__feed__

class Item(BetterObject):
    author = Author()
    enclosures = []

    def __init__(self, node):
        self._xml = node

    def __getattr__(self, attr, default=None):
        return getattr(self._xml, attr, default)

    def __str__(self):
        return str(self.id or self.title)

class Atom10Item(Item):
    _enclosures = None
    _published = None
    _updated = None
    _link = None
    _author = None
    
    def _process_links(self):
        self._enclosures = []
        for link in self._xml.iterchildren(tag='{http://www.w3.org/2005/Atom}link'):
            if link.attrib.get('rel', 'alternate') == 'alternate':
                self._link = link.attrib['href']
            elif link.attrib['rel'] == 'enclosure':
                if link.attrib['type'].startswith('image/'):
                    cls = Image
                else:
                    cls = Enclosure
                self._enclosures.append(cls(link.attrib['href'], link.attrib['type']))
    
    @property
    def author(self):
        if self._author is None:
            author = self._xml.author
            self._author = Author(
                name=getattr(author, 'name', None),
                email=getattr(author, 'email', None),
                link=getattr(author, 'uri', None),
            )
        return self._author
    
    @property
    def link(self):
        if self._link is None:
            self._process_links()
        return self._link
    
    @property
    def enclosures(self):
        if self._enclosures is None:
            self._process_links()
        return self._enclosures
    
    media = enclosures
    
    @property
    def description(self):
        return unicode(self._xml.content).strip()
    
    @property
    def published(self):
        if self._published is None:
            try:
                datestr = self._xml.published
            except AttributeError:
                self._published = self.updated
            else:
                self._published = parse_date(datestr)
        return self._published

    @property
    def updated(self):
        if self._updated is None:
            try:
                datestr = self._xml.updated
            except AttributeError:
                self._updated = None
            else:
                self._updated = parse_date(datestr)
        return self._updated

class Atom10Feed(Feed):
    _published = None
    _updated = None
    
    __feed__ = 'Atom 1.0'
    
    @property
    def published(self):
        if self._published is None:
            try:
                datestr = self._xml.published
            except AttributeError:
                self._published = self.updated
            else:
                self._published = parse_date(datestr)
        return self._published

    @property
    def updated(self):
        if self._updated is None:
            try:
                datestr = self._xml.updated
            except AttributeError:
                self._updated = None
            else:
                self._updated = parse_date(datestr)
        return self._updated
    
    @property
    def is_valid(self):
        # <feed xmlns="http://www.w3.org/2005/Atom">
        return self._xml.tag == '{http://www.w3.org/2005/Atom}feed'
    
    @property
    def entries(self):
        return [Atom10Item(item) for item in self._xml.iterchildren(tag='{http://www.w3.org/2005/Atom}entry')]


class RSS20Item(Item):
    _published = None
    _enclosures = None
    
    @property
    def author(self):
        # TODO: implement parsing on this to at least support
        # standard author formats such as "Name <email.com>".
        if self._author is None:
            author = self._xml.author
            self._author = Author(
                name=author,
            )
        return self._author
    
    @property
    def description(self):
        return unicode(self._xml.description).strip()
    
    def _process_links(self):
        # <media:thumbnail url="http://th04.deviantart.net/fs48/300W/f/2009/207/d/7/d7400f45d945d29fa1edba98531bc887.jpg" height="399" width="300"/>
        # <media:content url="http://fc04.deviantart.com/fs48/f/2009/207/d/7/d7400f45d945d29fa1edba98531bc887.jpg" height="936" width="704" medium="image"/>
        # TODO: These need changed to namespaces
        self._enclosures = []
        for enclosure in self._xml.iterchildren(tag='thumbnail'):
            self._enclosures.append(Thumbnail(enclosure.attrib['url']))
        for enclosure in self._xml.iterchildren(tag='content'):
            if enclosure.attrib.get('medium') == 'image':
                self._enclosures.append(Image(enclosure.attrib['url']))
            else:
                self._enclosures.append(Enclosure(enclosure.attrib['url']))

    @property
    def enclosures(self):
        if self._enclosures is None:
            self._process_links()
        return self._enclosures
    
    media = enclosures
    
    @property
    def published(self):
        if self._published is None:
            try:
                self._published = parse_date(self._xml.pubDate)
            except AttributeError:
                self._published = None
        return self._published

    updated = published

    @property
    def id(self):
        return self._xml.guid

class RSS20Feed(Feed):
    _published = None
    _updated = None
    
    __feed__ = 'RSS 2.0'
    
    def __getattr__(self, attr, default=None):
    	# print attr
        result = getattr(self._xml.channel, attr, default)
        if result is not None:
            result = Tag(result)
        return result
    
    @property
    def is_valid(self):
        return self._xml.tag == 'rss' and self._xml.attrib['version'] == '2.0'
    
    @property
    def published(self):
        if self._published is None:
            try:
                datestr = self._xml.channel.pubDate
            except AttributeError:
                self._published = None
            else:
                self._published = parse_date(datestr)
        return self._published

    @property
    def updated(self):
        if self._updated is None:
            try:
                datestr = self._xml.channel.lastBuildDate
            except AttributeError:
                self._updated = self.published
            else:
                self._updated = parse_date(datestr)
        return self._updated
    
    @property
    def entries(self):
        return [RSS20Item(item) for item in self._xml.channel.iterchildren(tag='item')]

feeds = (RSS20Feed, Atom10Feed)

ACCEPT_HEADER = "application/atom+xml,application/rdf+xml,application/rss+xml,application/x-netcdf,application/xml;q=0.9,text/xml;q=0.2,*/*;q=0.1"

USER_AGENT = 'py-feedreader'

class ParseError(Exception): pass

def _from_parsed(parsed):
    for feed in feeds:
        try:
            result = feed(parsed)
        except InvalidFeed:
            pass
        else:
            return result
    raise InvalidFeed(parsed.tag)

def from_string(data, *args, **kwargs):
    parsed = lxml.objectify.fromstring(data, *args, **kwargs)
    return _from_parsed(parsed)

def from_file(fp, *args, **kwargs):
    parsed = lxml.objectify.parse(fp, **kwargs).getroot()
    return _from_parsed(parsed)

def from_url(url, **kwargs):
    url = urlparse.urlparse(url)
    if url.scheme == 'https':
        conn = httplib.HTTPSConnection
    elif url.scheme == 'http':
        conn = httplib.HTTPConnection
    else:
        raise NotImplementedError
    
    base_url = '%s://%s' % (url.scheme, url.hostname)
    
    headers = {
        'User-Agent': USER_AGENT,
        'Accept': ACCEPT_HEADER,
    }
    connection = conn(url.hostname)
    method = kwargs.pop('method', 'GET').upper()
    if method == 'GET':
        path, query = url.path, ''
        if url.query:
            path += '?' + url.query
    else:
        path, query = url.path, url.query
    connection.request(method, path, query, headers)
    try:
        response = connection.getresponse()
    except httplib.BadStatusLine, exc:
        raise ParseError('Bad status line: %s' % (exc,))
    
    if response.status != 200:
        if response.status in (301, 302):
            return from_url(response.getheader('location'), **kwargs)
        raise ParseError('%s %s' % (response.status, response.reason))

    return from_file(response, base_url=base_url)

def parse_date(date_string):
    date_string = unicode(date_string)

    return dateutil.parser.parse(date_string)




