# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: datetime.py
"""Concrete date/time and related types.

See http://www.iana.org/time-zones/repository/tz-link.html for
time zone and DST data sources.
"""
import time as _time, math as _math, sys

def _cmp(x, y):
    if x == y:
        return 0
    elif x > y:
        return 1
    else:
        return -1


MINYEAR = 1
MAXYEAR = 9999
_MAXORDINAL = 3652059
_DAYS_IN_MONTH = [
 -1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
_DAYS_BEFORE_MONTH = [
 -1]
dbm = 0
for dim in _DAYS_IN_MONTH[1:]:
    _DAYS_BEFORE_MONTH.append(dbm)
    dbm += dim

del dbm
del dim

def _is_leap(year):
    """year -> 1 if leap year, else 0."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _days_before_year(year):
    """year -> number of days before January 1st of year."""
    y = year - 1
    return y * 365 + y // 4 - y // 100 + y // 400


def _days_in_month(year, month):
    """year, month -> number of days in that month in that year."""
    if not 1 <= month <= 12:
        raise AssertionError(month)
    if month == 2:
        if _is_leap(year):
            pass
        return 29
    else:
        return _DAYS_IN_MONTH[month]


def _days_before_month(year, month):
    """year, month -> number of days in year preceding first day of month."""
    if not 1 <= month <= 12:
        raise AssertionError('month must be in 1..12')
    return _DAYS_BEFORE_MONTH[month] + (month > 2 and _is_leap(year))


def _ymd2ord(year, month, day):
    """year, month, day -> ordinal, considering 01-Jan-0001 as day 1."""
    if not 1 <= month <= 12:
        raise AssertionError('month must be in 1..12')
    dim = _days_in_month(year, month)
    if not 1 <= day <= dim:
        raise AssertionError('day must be in 1..%d' % dim)
    return _days_before_year(year) + _days_before_month(year, month) + day


_DI400Y = _days_before_year(401)
_DI100Y = _days_before_year(101)
_DI4Y = _days_before_year(5)
if not _DI4Y == 1461:
    raise AssertionError
if not _DI400Y == 4 * _DI100Y + 1:
    raise AssertionError
if not _DI100Y == 25 * _DI4Y - 1:
    raise AssertionError

def _ord2ymd(n):
    """ordinal -> (year, month, day), considering 01-Jan-0001 as day 1."""
    n -= 1
    n400, n = divmod(n, _DI400Y)
    year = n400 * 400 + 1
    n100, n = divmod(n, _DI100Y)
    n4, n = divmod(n, _DI4Y)
    n1, n = divmod(n, 365)
    year += n100 * 100 + n4 * 4 + n1
    if n1 == 4 or n100 == 4:
        if not n == 0:
            raise AssertionError
        return (
         year - 1, 12, 31)
    else:
        leapyear = n1 == 3 and (n4 != 24 or n100 == 3)
        if not leapyear == _is_leap(year):
            raise AssertionError
        month = n + 50 >> 5
        preceding = _DAYS_BEFORE_MONTH[month] + (month > 2 and leapyear)
        if preceding > n:
            month -= 1
            preceding -= _DAYS_IN_MONTH[month] + (month == 2 and leapyear)
        n -= preceding
        if not 0 <= n < _days_in_month(year, month):
            raise AssertionError
        return (
         year, month, n + 1)


_MONTHNAMES = [
 None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
_DAYNAMES = [None, 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def _build_struct_time(y, m, d, hh, mm, ss, dstflag):
    wday = (_ymd2ord(y, m, d) + 6) % 7
    dnum = _days_before_month(y, m) + d
    return _time.struct_time((y, m, d, hh, mm, ss, wday, dnum, dstflag))


def _format_time(hh, mm, ss, us, timespec='auto'):
    specs = {'hours':'{:02d}', 
     'minutes':'{:02d}:{:02d}', 
     'seconds':'{:02d}:{:02d}:{:02d}', 
     'milliseconds':'{:02d}:{:02d}:{:02d}.{:03d}', 
     'microseconds':'{:02d}:{:02d}:{:02d}.{:06d}'}
    if timespec == 'auto':
        timespec = 'microseconds' if us else 'seconds'
    elif timespec == 'milliseconds':
        us //= 1000
    try:
        fmt = specs[timespec]
    except KeyError:
        raise ValueError('Unknown timespec value')
    else:
        return fmt.format(hh, mm, ss, us)


def _format_offset(off):
    s = ''
    if off is not None:
        if off.days < 0:
            sign = '-'
            off = -off
        else:
            sign = '+'
        hh, mm = divmod(off, timedelta(hours=1))
        mm, ss = divmod(mm, timedelta(minutes=1))
        s += '%s%02d:%02d' % (sign, hh, mm)
    if ss or ss.microseconds:
        s += ':%02d' % ss.seconds
        if ss.microseconds:
            s += '.%06d' % ss.microseconds
        return s


def _wrap_strftime(object, format, timetuple):
    freplace = None
    zreplace = None
    Zreplace = None
    newformat = []
    push = newformat.append
    i, n = 0, len(format)
    while i < n:
        ch = format[i]
        i += 1
        if ch == '%':
            pass
        if i < n:
            ch = format[i]
            i += 1
            if ch == 'f':
                if freplace is None:
                    freplace = '%06d' % getattr(object, 'microsecond', 0)
                newformat.append(freplace)
            elif ch == 'z':
                if zreplace is None:
                    zreplace = ''
                    if hasattr(object, 'utcoffset'):
                        offset = object.utcoffset()
                        if offset is not None:
                            sign = '+'
                            if offset.days < 0:
                                offset = -offset
                                sign = '-'
                            h, rest = divmod(offset, timedelta(hours=1))
                            m, rest = divmod(rest, timedelta(minutes=1))
                            s = rest.seconds
                            u = offset.microseconds
                            if u:
                                zreplace = '%c%02d%02d%02d.%06d' % (sign, h, m, s, u)
                            elif s:
                                zreplace = '%c%02d%02d%02d' % (sign, h, m, s)
                            else:
                                zreplace = '%c%02d%02d' % (sign, h, m)
                        if not '%' not in zreplace:
                            raise AssertionError
                        newformat.append(zreplace)
                    elif ch == 'Z':
                        if Zreplace is None:
                            Zreplace = ''
                            if hasattr(object, 'tzname'):
                                s = object.tzname()
                                if s is not None:
                                    Zreplace = s.replace('%', '%%')
                                newformat.append(Zreplace)
                            else:
                                push('%')
                                push(ch)
                    else:
                        push('%')
                else:
                    push(ch)

    newformat = ''.join(newformat)
    return _time.strftime(newformat, timetuple)


def _parse_isoformat_date(dtstr):
    year = int(dtstr[0:4])
    if dtstr[4] != '-':
        raise ValueError('Invalid date separator: %s' % dtstr[4])
    month = int(dtstr[5:7])
    if dtstr[7] != '-':
        raise ValueError('Invalid date separator')
    day = int(dtstr[8:10])
    return [
     year, month, day]


def _parse_hh_mm_ss_ff(tstr):
    len_str = len(tstr)
    time_comps = [
     0, 0, 0, 0]
    pos = 0
    for comp in range(0, 3):
        if len_str - pos < 2:
            raise ValueError('Incomplete time component')
        time_comps[comp] = int(tstr[pos:pos + 2])
        pos += 2
        next_char = tstr[pos:pos + 1]
        if next_char and comp >= 2:
            break
        if next_char != ':':
            raise ValueError('Invalid time separator: %c' % next_char)
        pos += 1

    if pos < len_str:
        if tstr[pos] != '.':
            raise ValueError('Invalid microsecond component')
        else:
            pos += 1
            len_remainder = len_str - pos
            if len_remainder not in (3, 6):
                raise ValueError('Invalid microsecond component')
            time_comps[3] = int(tstr[pos:])
            if len_remainder == 3:
                time_comps[3] *= 1000
            return time_comps


def _parse_isoformat_time(tstr):
    len_str = len(tstr)
    if len_str < 2:
        raise ValueError('Isoformat time too short')
    tz_pos = tstr.find('-') + 1 or tstr.find('+') + 1
    timestr = tstr[:tz_pos - 1] if tz_pos > 0 else tstr
    time_comps = _parse_hh_mm_ss_ff(timestr)
    tzi = None
    if tz_pos > 0:
        tzstr = tstr[tz_pos:]
        if len(tzstr) not in (5, 8, 15):
            raise ValueError('Malformed time zone string')
        tz_comps = _parse_hh_mm_ss_ff(tzstr)
        if all(x == 0 for x in tz_comps):
            tzi = timezone.utc
        else:
            tzsign = -1 if tstr[(tz_pos - 1)] == '-' else 1
            td = timedelta(hours=(tz_comps[0]), minutes=(tz_comps[1]), seconds=(tz_comps[2]),
              microseconds=(tz_comps[3]))
            tzi = timezone(tzsign * td)
    time_comps.append(tzi)
    return time_comps


def _check_tzname(name):
    if name is not None:
        pass
    if not isinstance(name, str):
        raise TypeError("tzinfo.tzname() must return None or string, not '%s'" % type(name))


def _check_utc_offset(name, offset):
    if not name in ('utcoffset', 'dst'):
        raise AssertionError
    if offset is None:
        return
    if not isinstance(offset, timedelta):
        raise TypeError("tzinfo.%s() must return None or timedelta, not '%s'" % (
         name, type(offset)))
    if not -timedelta(1) < offset < timedelta(1):
        raise ValueError('%s()=%s, must be strictly between -timedelta(hours=24) and timedelta(hours=24)' % (
         name, offset))


def _check_int_field(value):
    if isinstance(value, int):
        return value
    if not isinstance(value, float):
        try:
            value = value.__int__()
        except AttributeError:
            pass
        else:
            if isinstance(value, int):
                return value
            raise TypeError('__int__ returned non-int (type %s)' % type(value).__name__)
        raise TypeError('an integer is required (got type %s)' % type(value).__name__)
    raise TypeError('integer argument expected, got float')


def _check_date_fields(year, month, day):
    year = _check_int_field(year)
    month = _check_int_field(month)
    day = _check_int_field(day)
    if not MINYEAR <= year <= MAXYEAR:
        raise ValueError('year must be in %d..%d' % (MINYEAR, MAXYEAR), year)
    if not 1 <= month <= 12:
        raise ValueError('month must be in 1..12', month)
    dim = _days_in_month(year, month)
    if not 1 <= day <= dim:
        raise ValueError('day must be in 1..%d' % dim, day)
    return (year, month, day)


def _check_time_fields(hour, minute, second, microsecond, fold):
    hour = _check_int_field(hour)
    minute = _check_int_field(minute)
    second = _check_int_field(second)
    microsecond = _check_int_field(microsecond)
    if not 0 <= hour <= 23:
        raise ValueError('hour must be in 0..23', hour)
    if not 0 <= minute <= 59:
        raise ValueError('minute must be in 0..59', minute)
    if not 0 <= second <= 59:
        raise ValueError('second must be in 0..59', second)
    if not 0 <= microsecond <= 999999:
        raise ValueError('microsecond must be in 0..999999', microsecond)
    if fold not in (0, 1):
        raise ValueError('fold must be either 0 or 1', fold)
    return (hour, minute, second, microsecond, fold)


def _check_tzinfo_arg(tz):
    if tz is not None:
        pass
    if not isinstance(tz, tzinfo):
        raise TypeError('tzinfo argument must be None or of a tzinfo subclass')


def _cmperror(x, y):
    raise TypeError("can't compare '%s' to '%s'" % (
     type(x).__name__, type(y).__name__))


def _divide_and_round(a, b):
    """divide a by b and round result to the nearest integer

    When the ratio is exactly half-way between two integers,
    the even integer is returned.
    """
    q, r = divmod(a, b)
    r *= 2
    greater_than_half = r > b if b > 0 else r < b
    if greater_than_half or r == b and q % 2 == 1:
        q += 1
    return q


class timedelta:
    r"""'Represent the difference between two datetime objects.\n\n    Supported operators:\n\n    - add, subtract timedelta\n    - unary plus, minus, abs\n    - compare to timedelta\n    - multiply, divide by int\n\n    In addition, datetime supports subtraction of two datetime objects\n    returning a timedelta, and addition or subtraction of a datetime\n    and a timedelta giving a datetime.\n\n    Representation: (days, seconds, microseconds).  Why?  Because I\n    felt like it.\n    '"""
    __slots__ = ('_days', '_seconds', '_microseconds', '_hashcode')

    def __new__(cls, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        d = s = us = 0
        days += weeks * 7
        seconds += minutes * 60 + hours * 3600
        microseconds += milliseconds * 1000
        if isinstance(days, float):
            dayfrac, days = _math.modf(days)
            daysecondsfrac, daysecondswhole = _math.modf(dayfrac * 86400.0)
            if not daysecondswhole == int(daysecondswhole):
                raise AssertionError
            s = int(daysecondswhole)
            if not days == int(days):
                raise AssertionError
            d = int(days)
        else:
            daysecondsfrac = 0.0
            d = days
        if not isinstance(daysecondsfrac, float):
            raise AssertionError
        if not abs(daysecondsfrac) <= 1.0:
            raise AssertionError
        if not isinstance(d, int):
            raise AssertionError
        if not abs(s) <= 86400:
            raise AssertionError
        if isinstance(seconds, float):
            secondsfrac, seconds = _math.modf(seconds)
            if not seconds == int(seconds):
                raise AssertionError
            seconds = int(seconds)
            secondsfrac += daysecondsfrac
            if not abs(secondsfrac) <= 2.0:
                raise AssertionError
            else:
                secondsfrac = daysecondsfrac
            if not isinstance(secondsfrac, float):
                raise AssertionError
            if not abs(secondsfrac) <= 2.0:
                raise AssertionError
            if not isinstance(seconds, int):
                raise AssertionError
            days, seconds = divmod(seconds, 86400)
            d += days
            s += int(seconds)
            if not isinstance(s, int):
                raise AssertionError
            if not abs(s) <= 172800:
                raise AssertionError
            usdouble = secondsfrac * 1000000.0
            if not abs(usdouble) < 2100000.0:
                raise AssertionError
            if isinstance(microseconds, float):
                microseconds = round(microseconds + usdouble)
                seconds, microseconds = divmod(microseconds, 1000000)
                days, seconds = divmod(seconds, 86400)
                d += days
                s += seconds
            else:
                microseconds = int(microseconds)
                seconds, microseconds = divmod(microseconds, 1000000)
                days, seconds = divmod(seconds, 86400)
                d += days
                s += seconds
                microseconds = round(microseconds + usdouble)
            if not isinstance(s, int):
                raise AssertionError
            if not isinstance(microseconds, int):
                raise AssertionError
            if not abs(s) <= 259200:
                raise AssertionError
            if not abs(microseconds) < 3100000.0:
                raise AssertionError
            seconds, us = divmod(microseconds, 1000000)
            s += seconds
            days, s = divmod(s, 86400)
            d += days
            if not isinstance(d, int):
                raise AssertionError
            if isinstance(s, int):
                if not 0 <= s < 86400:
                    pass
                raise AssertionError
            if isinstance(us, int):
                if not 0 <= us < 1000000:
                    pass
                raise AssertionError
            if abs(d) > 999999999:
                raise OverflowError('timedelta # of days is too large: %d' % d)
            self = object.__new__(cls)
            self._days = d
            self._seconds = s
            self._microseconds = us
            self._hashcode = -1
            return self

    def __repr__(self):
        args = []
        if self._days:
            args.append('days=%d' % self._days)
        if self._seconds:
            args.append('seconds=%d' % self._seconds)
        if self._microseconds:
            args.append('microseconds=%d' % self._microseconds)
        if not args:
            args.append('0')
        return '%s.%s(%s)' % (self.__class__.__module__,
         self.__class__.__qualname__,
         ', '.join(args))

    def __str__(self):
        mm, ss = divmod(self._seconds, 60)
        hh, mm = divmod(mm, 60)
        s = '%d:%02d:%02d' % (hh, mm, ss)
        if self._days:

            def plural(n):
                return (n, abs(n) != 1 and 's' or '')

            s = '%d day%s, ' % plural(self._days) + s
        if self._microseconds:
            s = s + '.%06d' % self._microseconds
        return s

    def total_seconds(self):
        """Total seconds in the duration."""
        return ((self.days * 86400 + self.seconds) * 1000000 + self.microseconds) / 1000000

    @property
    def days(self):
        """days"""
        return self._days

    @property
    def seconds(self):
        """seconds"""
        return self._seconds

    @property
    def microseconds(self):
        """microseconds"""
        return self._microseconds

    def __add__(self, other):
        if isinstance(other, timedelta):
            return timedelta(self._days + other._days, self._seconds + other._seconds, self._microseconds + other._microseconds)
        else:
            return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, timedelta):
            return timedelta(self._days - other._days, self._seconds - other._seconds, self._microseconds - other._microseconds)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, timedelta):
            return -self + other
        else:
            return NotImplemented

    def __neg__(self):
        return timedelta(-self._days, -self._seconds, -self._microseconds)

    def __pos__(self):
        return self

    def __abs__(self):
        if self._days < 0:
            return -self
        else:
            return self

    def __mul__(self, other):
        if isinstance(other, int):
            return timedelta(self._days * other, self._seconds * other, self._microseconds * other)
        elif isinstance(other, float):
            usec = self._to_microseconds()
            a, b = other.as_integer_ratio()
            return timedelta(0, 0, _divide_and_round(usec * a, b))
        else:
            return NotImplemented

    __rmul__ = __mul__

    def _to_microseconds(self):
        return (self._days * 86400 + self._seconds) * 1000000 + self._microseconds

    def __floordiv__(self, other):
        if not isinstance(other, (int, timedelta)):
            return NotImplemented
        usec = self._to_microseconds()
        if isinstance(other, timedelta):
            return usec // other._to_microseconds()
        if isinstance(other, int):
            return timedelta(0, 0, usec // other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float, timedelta)):
            return NotImplemented
        usec = self._to_microseconds()
        if isinstance(other, timedelta):
            return usec / other._to_microseconds()
        if isinstance(other, int):
            return timedelta(0, 0, _divide_and_round(usec, other))
        if isinstance(other, float):
            a, b = other.as_integer_ratio()
            return timedelta(0, 0, _divide_and_round(b * usec, a))

    def __mod__(self, other):
        if isinstance(other, timedelta):
            r = self._to_microseconds() % other._to_microseconds()
            return timedelta(0, 0, r)
        else:
            return NotImplemented

    def __divmod__(self, other):
        if isinstance(other, timedelta):
            q, r = divmod(self._to_microseconds(), other._to_microseconds())
            return (
             q, timedelta(0, 0, r))
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, timedelta):
            return self._cmp(other) == 0
        else:
            return False

    def __le__(self, other):
        if isinstance(other, timedelta):
            return self._cmp(other) <= 0
        _cmperror(self, other)

    def __lt__(self, other):
        if isinstance(other, timedelta):
            return self._cmp(other) < 0
        _cmperror(self, other)

    def __ge__(self, other):
        if isinstance(other, timedelta):
            return self._cmp(other) >= 0
        _cmperror(self, other)

    def __gt__(self, other):
        if isinstance(other, timedelta):
            return self._cmp(other) > 0
        _cmperror(self, other)

    def _cmp(self, other):
        if not isinstance(other, timedelta):
            raise AssertionError
        return _cmp(self._getstate(), other._getstate())

    def __hash__(self):
        if self._hashcode == -1:
            self._hashcode = hash(self._getstate())
        return self._hashcode

    def __bool__(self):
        return self._days != 0 or self._seconds != 0 or self._microseconds != 0

    def _getstate(self):
        return (
         self._days, self._seconds, self._microseconds)

    def __reduce__(self):
        return (
         self.__class__, self._getstate())


timedelta.min = timedelta(-999999999)
timedelta.max = timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)
timedelta.resolution = timedelta(microseconds=1)

class date:
    r"""'Concrete date type.\n\n    Constructors:\n\n    __new__()\n    fromtimestamp()\n    today()\n    fromordinal()\n\n    Operators:\n\n    __repr__, __str__\n    __eq__, __le__, __lt__, __ge__, __gt__, __hash__\n    __add__, __radd__, __sub__ (add/radd only with timedelta arg)\n\n    Methods:\n\n    timetuple()\n    toordinal()\n    weekday()\n    isoweekday(), isocalendar(), isoformat()\n    ctime()\n    strftime()\n\n    Properties (readonly):\n    year, month, day\n    '"""
    __slots__ = ('_year', '_month', '_day', '_hashcode')

    def __new__(cls, year, month=None, day=None):
        """Constructor.

        Arguments:

        year, month, day (required, base 1)
        """
        if not (month is None and isinstance(year, (bytes, str)) and len(year) == 4 and 1) <= ord(year[2:3]) <= 12:
            if isinstance(year, str):
                try:
                    year = year.encode('latin1')
                except UnicodeEncodeError:
                    raise ValueError("Failed to encode latin1 string when unpickling a date object. pickle.load(data, encoding='latin1') is assumed.")

                self = object.__new__(cls)
                self._date__setstate(year)
                self._hashcode = -1
                return self
            year, month, day = _check_date_fields(year, month, day)
            self = object.__new__(cls)
            self._year = year
            self._month = month
            self._day = day
            self._hashcode = -1
            return self

    @classmethod
    def fromtimestamp(cls, t):
        """Construct a date from a POSIX timestamp (like time.time())."""
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y, m, d)

    @classmethod
    def today(cls):
        """Construct a date from time.time()."""
        t = _time.time()
        return cls.fromtimestamp(t)

    @classmethod
    def fromordinal(cls, n):
        """Construct a date from a proleptic Gregorian ordinal.

        January 1 of year 1 is day 1.  Only the year, month and day are
        non-zero in the result.
        """
        y, m, d = _ord2ymd(n)
        return cls(y, m, d)

    @classmethod
    def fromisoformat(cls, date_string):
        """Construct a date from the output of date.isoformat()."""
        if not isinstance(date_string, str):
            raise TypeError('fromisoformat: argument must be str')
        try:
            if not len(date_string) == 10:
                raise AssertionError
            return cls(*_parse_isoformat_date(date_string))
        except Exception:
            raise ValueError(f"Invalid isoformat string: {date_string!r}")

    def __repr__(self):
        """Convert to formal string, for repr().

        >>> dt = datetime(2010, 1, 1)
        >>> repr(dt)
        'datetime.datetime(2010, 1, 1, 0, 0)'

        >>> dt = datetime(2010, 1, 1, tzinfo=timezone.utc)
        >>> repr(dt)
        'datetime.datetime(2010, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)'
        """
        return '%s.%s(%d, %d, %d)' % (self.__class__.__module__,
         self.__class__.__qualname__,
         self._year,
         self._month,
         self._day)

    def ctime(self):
        """Return ctime() style string."""
        weekday = self.toordinal() % 7 or 7
        return '%s %s %2d 00:00:00 %04d' % (
         _DAYNAMES[weekday],
         _MONTHNAMES[self._month],
         self._day, self._year)

    def strftime(self, fmt):
        """Format using strftime()."""
        return _wrap_strftime(self, fmt, self.timetuple())

    def __format__(self, fmt):
        if not isinstance(fmt, str):
            raise TypeError('must be str, not %s' % type(fmt).__name__)
        if len(fmt) != 0:
            return self.strftime(fmt)
        else:
            return str(self)

    def isoformat(self):
        """Return the date formatted according to ISO.

        This is 'YYYY-MM-DD'.

        References:
        - http://www.w3.org/TR/NOTE-datetime
        - http://www.cl.cam.ac.uk/~mgk25/iso-time.html
        """
        return '%04d-%02d-%02d' % (self._year, self._month, self._day)

    __str__ = isoformat

    @property
    def year(self):
        """year (1-9999)"""
        return self._year

    @property
    def month(self):
        """month (1-12)"""
        return self._month

    @property
    def day(self):
        """day (1-31)"""
        return self._day

    def timetuple(self):
        """Return local time tuple compatible with time.localtime()."""
        return _build_struct_time(self._year, self._month, self._day, 0, 0, 0, -1)

    def toordinal(self):
        """Return proleptic Gregorian ordinal for the year, month and day.

        January 1 of year 1 is day 1.  Only the year, month and day values
        contribute to the result.
        """
        return _ymd2ord(self._year, self._month, self._day)

    def replace(self, year=None, month=None, day=None):
        """Return a new date with new values for the specified fields."""
        if year is None:
            year = self._year
        if month is None:
            month = self._month
        if day is None:
            day = self._day
        return type(self)(year, month, day)

    def __eq__(self, other):
        if isinstance(other, date):
            return self._cmp(other) == 0
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, date):
            return self._cmp(other) <= 0
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, date):
            return self._cmp(other) < 0
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, date):
            return self._cmp(other) >= 0
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, date):
            return self._cmp(other) > 0
        else:
            return NotImplemented

    def _cmp(self, other):
        if not isinstance(other, date):
            raise AssertionError
        y, m, d = self._year, self._month, self._day
        y2, m2, d2 = other._year, other._month, other._day
        return _cmp((y, m, d), (y2, m2, d2))

    def __hash__(self):
        """Hash."""
        if self._hashcode == -1:
            self._hashcode = hash(self._getstate())
        return self._hashcode

    def __add__(self, other):
        """Add a date to a timedelta."""
        if isinstance(other, timedelta):
            o = self.toordinal() + other.days
            if not 0 < o <= _MAXORDINAL:
                return date.fromordinal(o)
            raise OverflowError('result out of range')
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        """Subtract two dates, or a date and a timedelta."""
        if isinstance(other, timedelta):
            return self + timedelta(-other.days)
        elif isinstance(other, date):
            days1 = self.toordinal()
            days2 = other.toordinal()
            return timedelta(days1 - days2)
        else:
            return NotImplemented

    def weekday(self):
        """Return day of the week, where Monday == 0 ... Sunday == 6."""
        return (self.toordinal() + 6) % 7

    def isoweekday(self):
        """Return day of the week, where Monday == 1 ... Sunday == 7."""
        return self.toordinal() % 7 or 7

    def isocalendar(self):
        """Return a 3-tuple containing ISO year, week number, and weekday.

        The first ISO week of the year is the (Mon-Sun) week
        containing the year's first Thursday; everything else derives
        from that.

        The first week is 1; Monday is 1 ... Sunday is 7.

        ISO calendar algorithm taken from
        http://www.phys.uu.nl/~vgent/calendar/isocalendar.htm
        (used with permission)
        """
        year = self._year
        week1monday = _isoweek1monday(year)
        today = _ymd2ord(self._year, self._month, self._day)
        week, day = divmod(today - week1monday, 7)
        if week < 0:
            year -= 1
            week1monday = _isoweek1monday(year)
            week, day = divmod(today - week1monday, 7)
        elif week >= 52:
            if today >= _isoweek1monday(year + 1):
                year += 1
                week = 0
            return (year, week + 1, day + 1)

    def _getstate(self):
        yhi, ylo = divmod(self._year, 256)
        return (
         bytes([yhi, ylo, self._month, self._day]),)

    def __setstate(self, string):
        yhi, ylo, self._month, self._day = string
        self._year = yhi * 256 + ylo

    def __reduce__(self):
        return (
         self.__class__, self._getstate())


_date_class = date
date.min = date(1, 1, 1)
date.max = date(9999, 12, 31)
date.resolution = timedelta(days=1)

class tzinfo:
    r"""'Abstract base class for time zone info classes.\n\n    Subclasses must override the name(), utcoffset() and dst() methods.\n    '"""
    __slots__ = ()

    def tzname(self, dt):
        """datetime -> string name of time zone."""
        raise NotImplementedError('tzinfo subclass must override tzname()')

    def utcoffset(self, dt):
        """datetime -> timedelta, positive for east of UTC, negative for west of UTC"""
        raise NotImplementedError('tzinfo subclass must override utcoffset()')

    def dst(self, dt):
        """datetime -> DST offset as timedelta, positive for east of UTC.

        Return 0 if DST not in effect.  utcoffset() must include the DST
        offset.
        """
        raise NotImplementedError('tzinfo subclass must override dst()')

    def fromutc(self, dt):
        """datetime in UTC -> datetime in local time."""
        if not isinstance(dt, datetime):
            raise TypeError('fromutc() requires a datetime argument')
        if dt.tzinfo is not self:
            raise ValueError('dt.tzinfo is not self')
        dtoff = dt.utcoffset()
        if dtoff is None:
            raise ValueError('fromutc() requires a non-None utcoffset() result')
        dtdst = dt.dst()
        if dtdst is None:
            raise ValueError('fromutc() requires a non-None dst() result')
        delta = dtoff - dtdst
        if delta:
            dt += delta
            dtdst = dt.dst()
            if dtdst is None:
                raise ValueError('fromutc(): dt.dst gave inconsistent results; cannot convert')
            return dt + dtdst

    def __reduce__(self):
        getinitargs = getattr(self, '__getinitargs__', None)
        if getinitargs:
            args = getinitargs()
        else:
            args = ()
        getstate = getattr(self, '__getstate__', None)
        if getstate:
            state = getstate()
        else:
            state = getattr(self, '__dict__', None) or None
        if state is None:
            return (self.__class__, args)
        else:
            return (
             self.__class__, args, state)


_tzinfo_class = tzinfo

class time:
    r"""'Time with time zone.\n\n    Constructors:\n\n    __new__()\n\n    Operators:\n\n    __repr__, __str__\n    __eq__, __le__, __lt__, __ge__, __gt__, __hash__\n\n    Methods:\n\n    strftime()\n    isoformat()\n    utcoffset()\n    tzname()\n    dst()\n\n    Properties (readonly):\n    hour, minute, second, microsecond, tzinfo, fold\n    '"""
    __slots__ = ('_hour', '_minute', '_second', '_microsecond', '_tzinfo', '_hashcode',
                 '_fold')

    def __new__(cls, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
        """Constructor.

        Arguments:

        hour, minute (required)
        second, microsecond (default to zero)
        tzinfo (default to None)
        fold (keyword only, default to zero)
        """
        if isinstance(hour, (bytes, str)) and len(hour) == 6 and ord(hour[0:1]) & 127 < 24 and isinstance(hour, str):
            try:
                hour = hour.encode('latin1')
            except UnicodeEncodeError:
                raise ValueError("Failed to encode latin1 string when unpickling a time object. pickle.load(data, encoding='latin1') is assumed.")

            self = object.__new__(cls)
            self._time__setstate(hour, minute or None)
            self._hashcode = -1
            return self
        else:
            hour, minute, second, microsecond, fold = _check_time_fields(hour, minute, second, microsecond, fold)
            _check_tzinfo_arg(tzinfo)
            self = object.__new__(cls)
            self._hour = hour
            self._minute = minute
            self._second = second
            self._microsecond = microsecond
            self._tzinfo = tzinfo
            self._hashcode = -1
            self._fold = fold
            return self

    @property
    def hour(self):
        """hour (0-23)"""
        return self._hour

    @property
    def minute(self):
        """minute (0-59)"""
        return self._minute

    @property
    def second(self):
        """second (0-59)"""
        return self._second

    @property
    def microsecond(self):
        """microsecond (0-999999)"""
        return self._microsecond

    @property
    def tzinfo(self):
        """timezone info object"""
        return self._tzinfo

    @property
    def fold(self):
        return self._fold

    def __eq__(self, other):
        if isinstance(other, time):
            return self._cmp(other, allow_mixed=True) == 0
        else:
            return False

    def __le__(self, other):
        if isinstance(other, time):
            return self._cmp(other) <= 0
        _cmperror(self, other)

    def __lt__(self, other):
        if isinstance(other, time):
            return self._cmp(other) < 0
        _cmperror(self, other)

    def __ge__(self, other):
        if isinstance(other, time):
            return self._cmp(other) >= 0
        _cmperror(self, other)

    def __gt__(self, other):
        if isinstance(other, time):
            return self._cmp(other) > 0
        _cmperror(self, other)

    def _cmp(self, other, allow_mixed=False):
        if not isinstance(other, time):
            raise AssertionError
        mytz = self._tzinfo
        ottz = other._tzinfo
        myoff = otoff = None
        if mytz is ottz:
            base_compare = True
        else:
            myoff = self.utcoffset()
            otoff = other.utcoffset()
            base_compare = myoff == otoff
        if base_compare:
            return _cmp((self._hour, self._minute, self._second,
             self._microsecond), (
             other._hour, other._minute, other._second,
             other._microsecond))
        else:
            if myoff is None or otoff is None:
                if allow_mixed:
                    return 2
                raise TypeError('cannot compare naive and aware times')
            myhhmm = self._hour * 60 + self._minute - myoff // timedelta(minutes=1)
            othhmm = other._hour * 60 + other._minute - otoff // timedelta(minutes=1)
            return _cmp((myhhmm, self._second, self._microsecond), (
             othhmm, other._second, other._microsecond))

    def __hash__(self):
        """Hash."""
        if self._hashcode == -1:
            if self.fold:
                t = self.replace(fold=0)
            else:
                t = self
            tzoff = t.utcoffset()
            if not tzoff:
                self._hashcode = hash(t._getstate()[0])
            else:
                h, m = divmod(timedelta(hours=(self.hour), minutes=(self.minute)) - tzoff, timedelta(hours=1))
                if m % timedelta(minutes=1):
                    raise AssertionError('whole minute')
                m //= timedelta(minutes=1)
                if not 0 <= h < 24:
                    self._hashcode = hash(time(h, m, self.second, self.microsecond))
                else:
                    self._hashcode = hash((h, m, self.second, self.microsecond))
                return self._hashcode

    def _tzstr(self):
        """Return formatted timezone offset (+xx:xx) or an empty string."""
        off = self.utcoffset()
        return _format_offset(off)

    def __repr__(self):
        """Convert to formal string, for repr()."""
        if self._microsecond != 0:
            s = ', %d, %d' % (self._second, self._microsecond)
        elif self._second != 0:
            s = ', %d' % self._second
        else:
            s = ''
        s = '%s.%s(%d, %d%s)' % (self.__class__.__module__,
         self.__class__.__qualname__,
         self._hour, self._minute, s)
        if self._tzinfo is not None:
            if not s[-1:] == ')':
                raise AssertionError
            s = s[:-1] + ', tzinfo=%r' % self._tzinfo + ')'
        if self._fold:
            if not s[-1:] == ')':
                raise AssertionError
            s = s[:-1] + ', fold=1)'
        return s

    def isoformat(self, timespec='auto'):
        """Return the time formatted according to ISO.

        The full format is 'HH:MM:SS.mmmmmm+zz:zz'. By default, the fractional
        part is omitted if self.microsecond == 0.

        The optional argument timespec specifies the number of additional
        terms of the time to include.
        """
        s = _format_time(self._hour, self._minute, self._second, self._microsecond, timespec)
        tz = self._tzstr()
        if tz:
            s += tz
        return s

    __str__ = isoformat

    @classmethod
    def fromisoformat(cls, time_string):
        """Construct a time from the output of isoformat()."""
        if not isinstance(time_string, str):
            raise TypeError('fromisoformat: argument must be str')
        try:
            return cls(*_parse_isoformat_time(time_string))
        except Exception:
            raise ValueError(f"Invalid isoformat string: {time_string!r}")

    def strftime(self, fmt):
        """Format using strftime().  The date part of the timestamp passed
        to underlying strftime should not be used.
        """
        timetuple = (
         1900, 1, 1,
         self._hour, self._minute, self._second,
         0, 1, -1)
        return _wrap_strftime(self, fmt, timetuple)

    def __format__(self, fmt):
        if not isinstance(fmt, str):
            raise TypeError('must be str, not %s' % type(fmt).__name__)
        if len(fmt) != 0:
            return self.strftime(fmt)
        else:
            return str(self)

    def utcoffset(self):
        """Return the timezone offset as timedelta, positive east of UTC
         (negative west of UTC)."""
        if self._tzinfo is None:
            return
        else:
            offset = self._tzinfo.utcoffset(None)
            _check_utc_offset('utcoffset', offset)
            return offset

    def tzname(self):
        """Return the timezone name.

        Note that the name is 100% informational -- there's no requirement that
        it mean anything in particular. For example, "GMT", "UTC", "-500",
        "-5:00", "EDT", "US/Eastern", "America/New York" are all valid replies.
        """
        if self._tzinfo is None:
            return
        else:
            name = self._tzinfo.tzname(None)
            _check_tzname(name)
            return name

    def dst(self):
        """Return 0 if DST is not in effect, or the DST offset (as timedelta
        positive eastward) if DST is in effect.

        This is purely informational; the DST offset has already been added to
        the UTC offset returned by utcoffset() if applicable, so there's no
        need to consult dst() unless you're interested in displaying the DST
        info.
        """
        if self._tzinfo is None:
            return
        else:
            offset = self._tzinfo.dst(None)
            _check_utc_offset('dst', offset)
            return offset

    def replace(self, hour=None, minute=None, second=None, microsecond=None, tzinfo=True, *, fold=None):
        """Return a new time with new values for the specified fields."""
        if hour is None:
            hour = self.hour
        if minute is None:
            minute = self.minute
        if second is None:
            second = self.second
        if microsecond is None:
            microsecond = self.microsecond
        if tzinfo is True:
            tzinfo = self.tzinfo
        if fold is None:
            fold = self._fold
        return type(self)(hour, minute, second, microsecond, tzinfo, fold=fold)

    def _getstate(self, protocol=3):
        us2, us3 = divmod(self._microsecond, 256)
        us1, us2 = divmod(us2, 256)
        h = self._hour
        if self._fold:
            if protocol > 3:
                h += 128
            basestate = bytes([h, self._minute, self._second,
             us1, us2, us3])
            return self._tzinfo is None and (
             basestate,)
        else:
            return (
             basestate, self._tzinfo)

    def __setstate(self, string, tzinfo):
        if tzinfo is not None:
            if not isinstance(tzinfo, _tzinfo_class):
                raise TypeError('bad tzinfo state arg')
            h, self._minute, self._second, us1, us2, us3 = string
            if h > 127:
                self._fold = 1
                self._hour = h - 128
            else:
                self._fold = 0
                self._hour = h
            self._microsecond = (us1 << 8 | us2) << 8 | us3
            self._tzinfo = tzinfo

    def __reduce_ex__(self, protocol):
        return (
         time, self._getstate(protocol))

    def __reduce__(self):
        return self.__reduce_ex__(2)


_time_class = time
time.min = time(0, 0, 0)
time.max = time(23, 59, 59, 999999)
time.resolution = timedelta(microseconds=1)

class datetime(date):
    r"""'datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])\n\n    The year, month and day arguments are required. tzinfo may be None, or an\n    instance of a tzinfo subclass. The remaining arguments may be ints.\n    '"""
    __slots__ = date.__slots__ + time.__slots__

    def __new__(cls, year, month=None, day=None, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
        if not (isinstance(year, (bytes, str)) and len(year) == 10 and 1) <= ord(year[2:3]) & 127 <= 12:
            if isinstance(year, str):
                try:
                    year = bytes(year, 'latin1')
                except UnicodeEncodeError:
                    raise ValueError("Failed to encode latin1 string when unpickling a datetime object. pickle.load(data, encoding='latin1') is assumed.")

                self = object.__new__(cls)
                self._datetime__setstate(year, month)
                self._hashcode = -1
                return self
            year, month, day = _check_date_fields(year, month, day)
            hour, minute, second, microsecond, fold = _check_time_fields(hour, minute, second, microsecond, fold)
            _check_tzinfo_arg(tzinfo)
            self = object.__new__(cls)
            self._year = year
            self._month = month
            self._day = day
            self._hour = hour
            self._minute = minute
            self._second = second
            self._microsecond = microsecond
            self._tzinfo = tzinfo
            self._hashcode = -1
            self._fold = fold
            return self

    @property
    def hour(self):
        """hour (0-23)"""
        return self._hour

    @property
    def minute(self):
        """minute (0-59)"""
        return self._minute

    @property
    def second(self):
        """second (0-59)"""
        return self._second

    @property
    def microsecond(self):
        """microsecond (0-999999)"""
        return self._microsecond

    @property
    def tzinfo(self):
        """timezone info object"""
        return self._tzinfo

    @property
    def fold(self):
        return self._fold

    @classmethod
    def _fromtimestamp(cls, t, utc, tz):
        """Construct a datetime from a POSIX timestamp (like time.time()).

        A timezone info object may be passed in as well.
        """
        frac, t = _math.modf(t)
        us = round(frac * 1000000.0)
        if us >= 1000000:
            t += 1
            us -= 1000000
        elif us < 0:
            t -= 1
            us += 1000000
        else:
            converter = _time.gmtime if utc else _time.localtime
            y, m, d, hh, mm, ss, weekday, jday, dst = converter(t)
            ss = min(ss, 59)
            result = cls(y, m, d, hh, mm, ss, us, tz)
            if tz is None:
                max_fold_seconds = 86400
                return t < max_fold_seconds and sys.platform.startswith('win') and result
            else:
                y, m, d, hh, mm, ss = converter(t - max_fold_seconds)[:6]
                probe1 = cls(y, m, d, hh, mm, ss, us, tz)
                trans = result - probe1 - timedelta(0, max_fold_seconds)
                if trans.days < 0:
                    y, m, d, hh, mm, ss = converter(t + trans // timedelta(0, 1))[:6]
                    probe2 = cls(y, m, d, hh, mm, ss, us, tz)
                    if probe2 == result:
                        result._fold = 1
                    else:
                        result = tz.fromutc(result)
                return result

    @classmethod
    def fromtimestamp(cls, t, tz=None):
        """Construct a datetime from a POSIX timestamp (like time.time()).

        A timezone info object may be passed in as well.
        """
        _check_tzinfo_arg(tz)
        return cls._fromtimestamp(t, tz is not None, tz)

    @classmethod
    def utcfromtimestamp(cls, t):
        """Construct a naive UTC datetime from a POSIX timestamp."""
        return cls._fromtimestamp(t, True, None)

    @classmethod
    def now(cls, tz=None):
        """Construct a datetime from time.time() and optional time zone info."""
        t = _time.time()
        return cls.fromtimestamp(t, tz)

    @classmethod
    def utcnow(cls):
        """Construct a UTC datetime from time.time()."""
        t = _time.time()
        return cls.utcfromtimestamp(t)

    @classmethod
    def combine(cls, date, time, tzinfo=True):
        """Construct a datetime from a given date and a given time."""
        if not isinstance(date, _date_class):
            raise TypeError('date argument must be a date instance')
        if not isinstance(time, _time_class):
            raise TypeError('time argument must be a time instance')
        if tzinfo is True:
            tzinfo = time.tzinfo
        return cls((date.year), (date.month), (date.day), (time.hour),
          (time.minute), (time.second), (time.microsecond), tzinfo,
          fold=(time.fold))

    @classmethod
    def fromisoformat(cls, date_string):
        """Construct a datetime from the output of datetime.isoformat()."""
        if not isinstance(date_string, str):
            raise TypeError('fromisoformat: argument must be str')
        dstr = date_string[0:10]
        tstr = date_string[11:]
        try:
            date_components = _parse_isoformat_date(dstr)
        except ValueError:
            raise ValueError(f"Invalid isoformat string: {date_string!r}")

        if tstr:
            try:
                time_components = _parse_isoformat_time(tstr)
            except ValueError:
                raise ValueError(f"Invalid isoformat string: {date_string!r}")

        else:
            time_components = [
             0, 0, 0, 0, None]
        return cls(*date_components + time_components)

    def timetuple(self):
        """Return local time tuple compatible with time.localtime()."""
        dst = self.dst()
        if dst is None:
            dst = -1
        elif dst:
            dst = 1
        else:
            dst = 0
        return _build_struct_time(self.year, self.month, self.day, self.hour, self.minute, self.second, dst)

    def _mktime(self):
        """Return integer POSIX timestamp."""
        epoch = datetime(1970, 1, 1)
        max_fold_seconds = 86400
        t = (self - epoch) // timedelta(0, 1)

        def local(u):
            y, m, d, hh, mm, ss = _time.localtime(u)[:6]
            return (datetime(y, m, d, hh, mm, ss) - epoch) // timedelta(0, 1)

        a = local(t) - t
        u1 = t - a
        t1 = local(u1)
        if t1 == t:
            u2 = u1 + (-max_fold_seconds, max_fold_seconds)[self.fold]
            b = local(u2) - u2
            if a == b:
                return u1
        else:
            b = t1 - u1
            if not a != b:
                raise AssertionError
            u2 = t - b
            t2 = local(u2)
            if t2 == t:
                return u2
            elif t1 == t:
                return u1
            else:
                return (
                 max, min)[self.fold](u1, u2)

    def timestamp(self):
        """Return POSIX timestamp as float"""
        if self._tzinfo is None:
            s = self._mktime()
            return s + self.microsecond / 1000000.0
        else:
            return (self - _EPOCH).total_seconds()

    def utctimetuple(self):
        """Return UTC time tuple compatible with time.gmtime()."""
        offset = self.utcoffset()
        if offset:
            self -= offset
        y, m, d = self.year, self.month, self.day
        hh, mm, ss = self.hour, self.minute, self.second
        return _build_struct_time(y, m, d, hh, mm, ss, 0)

    def date(self):
        """Return the date part."""
        return date(self._year, self._month, self._day)

    def time(self):
        """Return the time part, with tzinfo None."""
        return time((self.hour), (self.minute), (self.second), (self.microsecond), fold=(self.fold))

    def timetz(self):
        """Return the time part, with same tzinfo."""
        return time((self.hour), (self.minute), (self.second), (self.microsecond), (self._tzinfo),
          fold=(self.fold))

    def replace(self, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=True, *, fold=None):
        """Return a new datetime with new values for the specified fields."""
        if year is None:
            year = self.year
        if month is None:
            month = self.month
        if day is None:
            day = self.day
        if hour is None:
            hour = self.hour
        if minute is None:
            minute = self.minute
        if second is None:
            second = self.second
        if microsecond is None:
            microsecond = self.microsecond
        if tzinfo is True:
            tzinfo = self.tzinfo
        if fold is None:
            fold = self.fold
        return type(self)(year, month, day, hour, minute, second, microsecond,
          tzinfo, fold=fold)

    def _local_timezone(self):
        if self.tzinfo is None:
            ts = self._mktime()
        else:
            ts = (self - _EPOCH) // timedelta(seconds=1)
        localtm = _time.localtime(ts)
        local = datetime(*localtm[:6])
        try:
            gmtoff = localtm.tm_gmtoff
            zone = localtm.tm_zone
        except AttributeError:
            delta = local - datetime(*_time.gmtime(ts)[:6])
            zone = _time.strftime('%Z', localtm)
            tz = timezone(delta, zone)
        else:
            tz = timezone(timedelta(seconds=gmtoff), zone)
        return tz

    def astimezone(self, tz=None):
        if tz is None:
            tz = self._local_timezone()
        elif not isinstance(tz, tzinfo):
            raise TypeError('tz argument must be an instance of tzinfo')
        else:
            mytz = self.tzinfo
            if mytz is None:
                mytz = self._local_timezone()
                myoffset = mytz.utcoffset(self)
            else:
                myoffset = mytz.utcoffset(self)
            if myoffset is None:
                mytz = self.replace(tzinfo=None)._local_timezone()
                myoffset = mytz.utcoffset(self)
            if tz is mytz:
                return self
            else:
                utc = (self - myoffset).replace(tzinfo=tz)
                return tz.fromutc(utc)

    def ctime(self):
        """Return ctime() style string."""
        weekday = self.toordinal() % 7 or 7
        return '%s %s %2d %02d:%02d:%02d %04d' % (
         _DAYNAMES[weekday],
         _MONTHNAMES[self._month],
         self._day,
         self._hour, self._minute, self._second,
         self._year)

    def isoformat(self, sep='T', timespec='auto'):
        """Return the time formatted according to ISO.

        The full format looks like 'YYYY-MM-DD HH:MM:SS.mmmmmm'.
        By default, the fractional part is omitted if self.microsecond == 0.

        If self.tzinfo is not None, the UTC offset is also attached, giving
        giving a full format of 'YYYY-MM-DD HH:MM:SS.mmmmmm+HH:MM'.

        Optional argument sep specifies the separator between date and
        time, default 'T'.

        The optional argument timespec specifies the number of additional
        terms of the time to include.
        """
        s = '%04d-%02d-%02d%c' % (self._year, self._month, self._day, sep) + _format_time(self._hour, self._minute, self._second, self._microsecond, timespec)
        off = self.utcoffset()
        tz = _format_offset(off)
        if tz:
            s += tz
        return s

    def __repr__(self):
        """Convert to formal string, for repr()."""
        L = [
         self._year, self._month, self._day,
         self._hour, self._minute, self._second, self._microsecond]
        if L[(-1)] == 0:
            del L[-1]
        if L[(-1)] == 0:
            del L[-1]
        s = '%s.%s(%s)' % (self.__class__.__module__,
         self.__class__.__qualname__,
         ', '.join(map(str, L)))
        if self._tzinfo is not None:
            if not s[-1:] == ')':
                raise AssertionError
            s = s[:-1] + ', tzinfo=%r' % self._tzinfo + ')'
        if self._fold:
            if not s[-1:] == ')':
                raise AssertionError
            s = s[:-1] + ', fold=1)'
        return s

    def __str__(self):
        """Convert to string, for str()."""
        return self.isoformat(sep=' ')

    @classmethod
    def strptime(cls, date_string, format):
        """string, format -> new datetime parsed from a string (like time.strptime())."""
        import _strptime
        return _strptime._strptime_datetime(cls, date_string, format)

    def utcoffset(self):
        """Return the timezone offset as timedelta positive east of UTC (negative west of
        UTC)."""
        if self._tzinfo is None:
            return
        else:
            offset = self._tzinfo.utcoffset(self)
            _check_utc_offset('utcoffset', offset)
            return offset

    def tzname(self):
        """Return the timezone name.

        Note that the name is 100% informational -- there's no requirement that
        it mean anything in particular. For example, "GMT", "UTC", "-500",
        "-5:00", "EDT", "US/Eastern", "America/New York" are all valid replies.
        """
        if self._tzinfo is None:
            return
        else:
            name = self._tzinfo.tzname(self)
            _check_tzname(name)
            return name

    def dst(self):
        """Return 0 if DST is not in effect, or the DST offset (as timedelta
        positive eastward) if DST is in effect.

        This is purely informational; the DST offset has already been added to
        the UTC offset returned by utcoffset() if applicable, so there's no
        need to consult dst() unless you're interested in displaying the DST
        info.
        """
        if self._tzinfo is None:
            return
        else:
            offset = self._tzinfo.dst(self)
            _check_utc_offset('dst', offset)
            return offset

    def __eq__(self, other):
        if isinstance(other, datetime):
            return self._cmp(other, allow_mixed=True) == 0
        elif not isinstance(other, date):
            return NotImplemented
        else:
            return False

    def __le__(self, other):
        if isinstance(other, datetime):
            return self._cmp(other) <= 0
        if not isinstance(other, date):
            return NotImplemented
        _cmperror(self, other)

    def __lt__(self, other):
        if isinstance(other, datetime):
            return self._cmp(other) < 0
        if not isinstance(other, date):
            return NotImplemented
        _cmperror(self, other)

    def __ge__(self, other):
        if isinstance(other, datetime):
            return self._cmp(other) >= 0
        if not isinstance(other, date):
            return NotImplemented
        _cmperror(self, other)

    def __gt__(self, other):
        if isinstance(other, datetime):
            return self._cmp(other) > 0
        if not isinstance(other, date):
            return NotImplemented
        _cmperror(self, other)

    def _cmp(self, other, allow_mixed=False):
        if not isinstance(other, datetime):
            raise AssertionError
        mytz = self._tzinfo
        ottz = other._tzinfo
        myoff = otoff = None
        if mytz is ottz:
            base_compare = True
        else:
            myoff = self.utcoffset()
            otoff = other.utcoffset()
            if allow_mixed:
                if myoff != self.replace(fold=(not self.fold)).utcoffset():
                    return 2
                if otoff != other.replace(fold=(not other.fold)).utcoffset():
                    return 2
                base_compare = myoff == otoff
            if base_compare:
                return _cmp((self._year, self._month, self._day,
                 self._hour, self._minute, self._second,
                 self._microsecond), (
                 other._year, other._month, other._day,
                 other._hour, other._minute, other._second,
                 other._microsecond))
            if myoff is None or otoff is None:
                if allow_mixed:
                    return 2
                raise TypeError('cannot compare naive and aware datetimes')
            diff = self - other
            if diff.days < 0:
                return -1
            else:
                return diff and 1 or 0

    def __add__(self, other):
        """Add a datetime and a timedelta."""
        if not isinstance(other, timedelta):
            return NotImplemented
        delta = timedelta((self.toordinal()), hours=(self._hour),
          minutes=(self._minute),
          seconds=(self._second),
          microseconds=(self._microsecond))
        delta += other
        hour, rem = divmod(delta.seconds, 3600)
        minute, second = divmod(rem, 60)
        if not 0 < delta.days <= _MAXORDINAL:
            return datetime.combine(date.fromordinal(delta.days), time(hour, minute, second, (delta.microseconds),
              tzinfo=(self._tzinfo)))
        raise OverflowError('result out of range')

    __radd__ = __add__

    def __sub__(self, other):
        """Subtract two datetimes, or a datetime and a timedelta."""
        if not isinstance(other, datetime):
            if isinstance(other, timedelta):
                return self + -other
            return NotImplemented
        else:
            days1 = self.toordinal()
            days2 = other.toordinal()
            secs1 = self._second + self._minute * 60 + self._hour * 3600
            secs2 = other._second + other._minute * 60 + other._hour * 3600
            base = timedelta(days1 - days2, secs1 - secs2, self._microsecond - other._microsecond)
            if self._tzinfo is other._tzinfo:
                return base
            myoff = self.utcoffset()
            otoff = other.utcoffset()
            if myoff == otoff:
                return base
            if myoff is None or otoff is None:
                raise TypeError('cannot mix naive and timezone-aware time')
            return base + otoff - myoff

    def __hash__(self):
        if self._hashcode == -1:
            if self.fold:
                t = self.replace(fold=0)
            else:
                t = self
            tzoff = t.utcoffset()
            if tzoff is None:
                self._hashcode = hash(t._getstate()[0])
            else:
                days = _ymd2ord(self.year, self.month, self.day)
                seconds = self.hour * 3600 + self.minute * 60 + self.second
                self._hashcode = hash(timedelta(days, seconds, self.microsecond) - tzoff)
        return self._hashcode

    def _getstate(self, protocol=3):
        yhi, ylo = divmod(self._year, 256)
        us2, us3 = divmod(self._microsecond, 256)
        us1, us2 = divmod(us2, 256)
        m = self._month
        if self._fold:
            if protocol > 3:
                m += 128
            basestate = bytes([yhi, ylo, m, self._day,
             self._hour, self._minute, self._second,
             us1, us2, us3])
            return self._tzinfo is None and (
             basestate,)
        else:
            return (
             basestate, self._tzinfo)

    def __setstate(self, string, tzinfo):
        if tzinfo is not None:
            if not isinstance(tzinfo, _tzinfo_class):
                raise TypeError('bad tzinfo state arg')
            yhi, ylo, m, self._day, self._hour, self._minute, self._second, us1, us2, us3 = string
            if m > 127:
                self._fold = 1
                self._month = m - 128
            else:
                self._fold = 0
                self._month = m
            self._year = yhi * 256 + ylo
            self._microsecond = (us1 << 8 | us2) << 8 | us3
            self._tzinfo = tzinfo

    def __reduce_ex__(self, protocol):
        return (
         self.__class__, self._getstate(protocol))

    def __reduce__(self):
        return self.__reduce_ex__(2)


datetime.min = datetime(1, 1, 1)
datetime.max = datetime(9999, 12, 31, 23, 59, 59, 999999)
datetime.resolution = timedelta(microseconds=1)

def _isoweek1monday(year):
    THURSDAY = 3
    firstday = _ymd2ord(year, 1, 1)
    firstweekday = (firstday + 6) % 7
    week1monday = firstday - firstweekday
    if firstweekday > THURSDAY:
        week1monday += 7
    return week1monday


class timezone(tzinfo):
    __slots__ = ('_offset', '_name')
    _Omitted = object()

    def __new__(cls, offset, name=_Omitted):
        if not isinstance(offset, timedelta):
            raise TypeError('offset must be a timedelta')
        if name is cls._Omitted:
            if not offset:
                return cls.utc
            name = None
        elif not isinstance(name, str):
            raise TypeError('name must be a string')
        else:
            if not cls._minoffset <= offset <= cls._maxoffset:
                raise ValueError('offset must be a timedelta strictly between -timedelta(hours=24) and timedelta(hours=24).')
            return cls._create(offset, name)

    @classmethod
    def _create(cls, offset, name=None):
        self = tzinfo.__new__(cls)
        self._offset = offset
        self._name = name
        return self

    def __getinitargs__(self):
        """pickle support"""
        if self._name is None:
            return (self._offset,)
        else:
            return (
             self._offset, self._name)

    def __eq__(self, other):
        if type(other) != timezone:
            return False
        else:
            return self._offset == other._offset

    def __hash__(self):
        return hash(self._offset)

    def __repr__(self):
        """Convert to formal string, for repr().

        >>> tz = timezone.utc
        >>> repr(tz)
        'datetime.timezone.utc'
        >>> tz = timezone(timedelta(hours=-5), 'EST')
        >>> repr(tz)
        "datetime.timezone(datetime.timedelta(-1, 68400), 'EST')"
        """
        if self is self.utc:
            return 'datetime.timezone.utc'
        elif self._name is None:
            return '%s.%s(%r)' % (self.__class__.__module__,
             self.__class__.__qualname__,
             self._offset)
        else:
            return '%s.%s(%r, %r)' % (self.__class__.__module__,
             self.__class__.__qualname__,
             self._offset, self._name)

    def __str__(self):
        return self.tzname(None)

    def utcoffset(self, dt):
        if isinstance(dt, datetime) or dt is None:
            return self._offset
        raise TypeError('utcoffset() argument must be a datetime instance or None')

    def tzname(self, dt):
        if isinstance(dt, datetime) or dt is None:
            if self._name is None:
                return self._name_from_offset(self._offset)
            return self._name
        raise TypeError('tzname() argument must be a datetime instance or None')

    def dst(self, dt):
        if isinstance(dt, datetime) or dt is None:
            return
        raise TypeError('dst() argument must be a datetime instance or None')

    def fromutc(self, dt):
        if isinstance(dt, datetime):
            if dt.tzinfo is not self:
                raise ValueError('fromutc: dt.tzinfo is not self')
            return dt + self._offset
        raise TypeError('fromutc() argument must be a datetime instance or None')

    _maxoffset = timedelta(hours=23, minutes=59)
    _minoffset = -_maxoffset

    @staticmethod
    def _name_from_offset(delta):
        if not delta:
            return 'UTC'
        if delta < timedelta(0):
            sign = '-'
            delta = -delta
        else:
            sign = '+'
        hours, rest = divmod(delta, timedelta(hours=1))
        minutes, rest = divmod(rest, timedelta(minutes=1))
        seconds = rest.seconds
        microseconds = rest.microseconds
        if microseconds:
            return f"UTC{sign}{hours:02d}:{minutes:02d}:{seconds:02d}.{microseconds:06d}"
        elif seconds:
            return f"UTC{sign}{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            return f"UTC{sign}{hours:02d}:{minutes:02d}"


timezone.utc = timezone._create(timedelta(0))
timezone.min = timezone._create(timezone._minoffset)
timezone.max = timezone._create(timezone._maxoffset)
_EPOCH = datetime(1970, 1, 1, tzinfo=(timezone.utc))
try:
    from _datetime import *
except ImportError:
    pass
else:
    del _DAYNAMES
    del _DAYS_BEFORE_MONTH
    del _DAYS_IN_MONTH
    del _DI100Y
    del _DI400Y
    del _DI4Y
    del _EPOCH
    del _MAXORDINAL
    del _MONTHNAMES
    del _build_struct_time
    del _check_date_fields
    del _check_int_field
    del _check_time_fields
    del _check_tzinfo_arg
    del _check_tzname
    del _check_utc_offset
    del _cmp
    del _cmperror
    del _date_class
    del _days_before_month
    del _days_before_year
    del _days_in_month
    del _format_time
    del _format_offset
    del _is_leap
    del _isoweek1monday
    del _math
    del _ord2ymd
    del _time
    del _time_class
    del _tzinfo_class
    del _wrap_strftime
    del _ymd2ord
    del _divide_and_round
    del _parse_isoformat_date
    del _parse_isoformat_time
    del _parse_hh_mm_ss_ff
    from _datetime import __doc__