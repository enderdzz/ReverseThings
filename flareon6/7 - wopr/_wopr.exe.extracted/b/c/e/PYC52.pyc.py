# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: _strptime.py
"""Strptime-related classes and functions.

CLASSES:
    LocaleTime -- Discovers and stores locale-specific time information
    TimeRE -- Creates regexes for pattern matching a string of text containing
                time information

FUNCTIONS:
    _getlang -- Figure out what language is being used for the locale
    strptime -- Calculates the time struct represented by the passed-in string

"""
import time, locale, calendar
from re import compile as re_compile
from re import IGNORECASE
from re import escape as re_escape
from datetime import date as datetime_date, timedelta as datetime_timedelta, timezone as datetime_timezone
from _thread import allocate_lock as _thread_allocate_lock
__all__ = []

def _getlang():
    return locale.getlocale(locale.LC_TIME)


class LocaleTime(object):
    r"""'Stores and handles locale-specific information related to time.\n\n    ATTRIBUTES:\n        f_weekday -- full weekday names (7-item list)\n        a_weekday -- abbreviated weekday names (7-item list)\n        f_month -- full month names (13-item list; dummy value in [0], which\n                    is added by code)\n        a_month -- abbreviated month names (13-item list, dummy value in\n                    [0], which is added by code)\n        am_pm -- AM/PM representation (2-item list)\n        LC_date_time -- format string for date/time representation (string)\n        LC_date -- format string for date representation (string)\n        LC_time -- format string for time representation (string)\n        timezone -- daylight- and non-daylight-savings timezone representation\n                    (2-item list of sets)\n        lang -- Language used by instance (2-item tuple)\n    '"""

    def __init__(self):
        """Set all attributes.

        Order of methods called matters for dependency reasons.

        The locale language is set at the offset and then checked again before
        exiting.  This is to make sure that the attributes were not set with a
        mix of information from more than one locale.  This would most likely
        happen when using threads where one thread calls a locale-dependent
        function while another thread changes the locale while the function in
        the other thread is still running.  Proper coding would call for
        locks to prevent changing the locale while locale-dependent code is
        running.  The check here is done in case someone does not think about
        doing this.

        Only other possible issue is if someone changed the timezone and did
        not call tz.tzset .  That is an issue for the programmer, though,
        since changing the timezone is worthless without that call.

        """
        self.lang = _getlang()
        self._LocaleTime__calc_weekday()
        self._LocaleTime__calc_month()
        self._LocaleTime__calc_am_pm()
        self._LocaleTime__calc_timezone()
        self._LocaleTime__calc_date_time()
        if _getlang() != self.lang:
            raise ValueError('locale changed during initialization')
        if time.tzname != self.tzname or time.daylight != self.daylight:
            raise ValueError('timezone changed during initialization')

    def __pad(self, seq, front):
        seq = list(seq)
        if front:
            seq.insert(0, '')
        else:
            seq.append('')
        return seq

    def __calc_weekday(self):
        a_weekday = [calendar.day_abbr[i].lower() for i in range(7)]
        f_weekday = [calendar.day_name[i].lower() for i in range(7)]
        self.a_weekday = a_weekday
        self.f_weekday = f_weekday

    def __calc_month(self):
        a_month = [calendar.month_abbr[i].lower() for i in range(13)]
        f_month = [calendar.month_name[i].lower() for i in range(13)]
        self.a_month = a_month
        self.f_month = f_month

    def __calc_am_pm(self):
        am_pm = []
        for hour in (1, 22):
            time_tuple = time.struct_time((1999, 3, 17, hour, 44, 55, 2, 76, 0))
            am_pm.append(time.strftime('%p', time_tuple).lower())

        self.am_pm = am_pm

    def __calc_date_time(self):
        time_tuple = time.struct_time((1999, 3, 17, 22, 44, 55, 2, 76, 0))
        date_time = [None, None, None]
        date_time[0] = time.strftime('%c', time_tuple).lower()
        date_time[1] = time.strftime('%x', time_tuple).lower()
        date_time[2] = time.strftime('%X', time_tuple).lower()
        replacement_pairs = [('%', '%%'), (self.f_weekday[2], '%A'),
         (
          self.f_month[3], '%B'), (self.a_weekday[2], '%a'),
         (
          self.a_month[3], '%b'), (self.am_pm[1], '%p'),
         ('1999', '%Y'), ('99', '%y'), ('22', '%H'),
         ('44', '%M'), ('55', '%S'), ('76', '%j'),
         ('17', '%d'), ('03', '%m'), ('3', '%m'),
         ('2', '%w'), ('10', '%I')]
        replacement_pairs.extend([(tz, '%Z') for tz_values in self.timezone for tz in iter(tz_values)])
        for offset, directive in ((0, '%c'), (1, '%x'), (2, '%X')):
            current_format = date_time[offset]
            for old, new in replacement_pairs:
                if old:
                    current_format = current_format.replace(old, new)

            time_tuple = time.struct_time((1999, 1, 3, 1, 1, 1, 6, 3, 0))
            if '00' in time.strftime(directive, time_tuple):
                U_W = '%W'
            else:
                U_W = '%U'
            date_time[offset] = current_format.replace('11', U_W)

        self.LC_date_time = date_time[0]
        self.LC_date = date_time[1]
        self.LC_time = date_time[2]

    def __calc_timezone(self):
        try:
            time.tzset()
        except AttributeError:
            pass

        self.tzname = time.tzname
        self.daylight = time.daylight
        no_saving = frozenset({'utc', 'gmt', self.tzname[0].lower()})
        if self.daylight:
            has_saving = frozenset({self.tzname[1].lower()})
        else:
            has_saving = frozenset()
        self.timezone = (
         no_saving, has_saving)


class TimeRE(dict):
    """'Handle conversion from format directives to regexes.'"""

    def __init__(self, locale_time=None):
        """Create keys/values.

        Order of execution is important for dependency reasons.

        """
        if locale_time:
            self.locale_time = locale_time
        else:
            self.locale_time = LocaleTime()
        base = super()
        base.__init__({'d':'(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])', 
         'f':'(?P<f>[0-9]{1,6})', 
         'H':'(?P<H>2[0-3]|[0-1]\\d|\\d)', 
         'I':'(?P<I>1[0-2]|0[1-9]|[1-9])', 
         'G':'(?P<G>\\d\\d\\d\\d)', 
         'j':'(?P<j>36[0-6]|3[0-5]\\d|[1-2]\\d\\d|0[1-9]\\d|00[1-9]|[1-9]\\d|0[1-9]|[1-9])', 
         'm':'(?P<m>1[0-2]|0[1-9]|[1-9])', 
         'M':'(?P<M>[0-5]\\d|\\d)', 
         'S':'(?P<S>6[0-1]|[0-5]\\d|\\d)', 
         'U':'(?P<U>5[0-3]|[0-4]\\d|\\d)', 
         'w':'(?P<w>[0-6])', 
         'u':'(?P<u>[1-7])', 
         'V':'(?P<V>5[0-3]|0[1-9]|[1-4]\\d|\\d)', 
         'y':'(?P<y>\\d\\d)', 
         'Y':'(?P<Y>\\d\\d\\d\\d)', 
         'z':'(?P<z>[+-]\\d\\d:?[0-5]\\d(:?[0-5]\\d(\\.\\d{1,6})?)?|Z)', 
         'A':self._TimeRE__seqToRE(self.locale_time.f_weekday, 'A'), 
         'a':self._TimeRE__seqToRE(self.locale_time.a_weekday, 'a'), 
         'B':self._TimeRE__seqToRE(self.locale_time.f_month[1:], 'B'), 
         'b':self._TimeRE__seqToRE(self.locale_time.a_month[1:], 'b'), 
         'p':self._TimeRE__seqToRE(self.locale_time.am_pm, 'p'), 
         'Z':self._TimeRE__seqToRE((tz for tz_names in self.locale_time.timezone for tz in tz_names), 'Z'), 
         '%':'%'})
        base.__setitem__('W', base.__getitem__('U').replace('U', 'W'))
        base.__setitem__('c', self.pattern(self.locale_time.LC_date_time))
        base.__setitem__('x', self.pattern(self.locale_time.LC_date))
        base.__setitem__('X', self.pattern(self.locale_time.LC_time))

    def __seqToRE(self, to_convert, directive):
        """Convert a list to a regex string for matching a directive.

        Want possible matching values to be from longest to shortest.  This
        prevents the possibility of a match occurring for a value that also
        a substring of a larger value that should have matched (e.g., 'abc'
        matching when 'abcdef' should have been the match).

        """
        to_convert = sorted(to_convert, key=len, reverse=True)
        for value in to_convert:
            if value != '':
                break
        else:
            return ''

        regex = '|'.join((re_escape(stuff) for stuff in to_convert))
        regex = '(?P<%s>%s' % (directive, regex)
        return '%s)' % regex

    def pattern(self, format):
        """Return regex pattern for the format string.

        Need to make sure that any characters that might be interpreted as
        regex syntax are escaped.

        """
        processed_format = ''
        regex_chars = re_compile('([\\\\.^$*+?\\(\\){}\\[\\]|])')
        format = regex_chars.sub('\\\\\\1', format)
        whitespace_replacement = re_compile('\\s+')
        format = whitespace_replacement.sub('\\\\s+', format)
        while 1:
            if '%' in format:
                directive_index = format.index('%') + 1
                processed_format = '%s%s%s' % (processed_format,
                 format[:directive_index - 1],
                 self[format[directive_index]])
                format = format[directive_index + 1:]

        return '%s%s' % (processed_format, format)

    def compile(self, format):
        """Return a compiled re object for the format string."""
        return re_compile(self.pattern(format), IGNORECASE)


_cache_lock = _thread_allocate_lock()
_TimeRE_cache = TimeRE()
_CACHE_MAX_SIZE = 5
_regex_cache = {}

def _calc_julian_from_U_or_W(year, week_of_year, day_of_week, week_starts_Mon):
    """Calculate the Julian day based on the year, week of the year, and day of
    the week, with week_start_day representing whether the week of the year
    assumes the week starts on Sunday or Monday (6 or 0)."""
    first_weekday = datetime_date(year, 1, 1).weekday()
    if not week_starts_Mon:
        first_weekday = (first_weekday + 1) % 7
        day_of_week = (day_of_week + 1) % 7
    week_0_length = (7 - first_weekday) % 7
    if week_of_year == 0:
        return 1 + day_of_week - first_weekday
    else:
        days_to_week = week_0_length + 7 * (week_of_year - 1)
        return 1 + days_to_week + day_of_week


def _calc_julian_from_V(iso_year, iso_week, iso_weekday):
    """Calculate the Julian day based on the ISO 8601 year, week, and weekday.
    ISO weeks start on Mondays, with week 01 being the week containing 4 Jan.
    ISO week days range from 1 (Monday) to 7 (Sunday).
    """
    correction = datetime_date(iso_year, 1, 4).isoweekday() + 3
    ordinal = iso_week * 7 + iso_weekday - correction
    if ordinal < 1:
        ordinal += datetime_date(iso_year, 1, 1).toordinal()
        iso_year -= 1
        ordinal -= datetime_date(iso_year, 1, 1).toordinal()
    return (iso_year, ordinal)


def _strptime(data_string, format='%a %b %d %H:%M:%S %Y'):
    """Return a 2-tuple consisting of a time struct and an int containing
    the number of microseconds based on the input string and the
    format string."""
    global _TimeRE_cache
    global _regex_cache
    for index, arg in enumerate([data_string, format]):
        if not isinstance(arg, str):
            msg = 'strptime() argument {} must be str, not {}'
            raise TypeError(msg.format(index, type(arg)))

    with _cache_lock:
        locale_time = _TimeRE_cache.locale_time
        if _getlang() != locale_time.lang or time.tzname != locale_time.tzname or time.daylight != locale_time.daylight:
            _TimeRE_cache = TimeRE()
            _regex_cache.clear()
            locale_time = _TimeRE_cache.locale_time
        if len(_regex_cache) > _CACHE_MAX_SIZE:
            _regex_cache.clear()
        format_regex = _regex_cache.get(format)
        if not format_regex:
            try:
                format_regex = _TimeRE_cache.compile(format)
            except KeyError as err:
                try:
                    bad_directive = err.args[0]
                    if bad_directive == '\\':
                        bad_directive = '%'
                    del err
                    raise ValueError("'%s' is a bad directive in format '%s'" % (
                     bad_directive, format)) from None
                finally:
                    err = None
                    del err

            except IndexError:
                raise ValueError("stray %% in format '%s'" % format) from None

            _regex_cache[format] = format_regex
    found = format_regex.match(data_string)
    if not found:
        raise ValueError('time data %r does not match format %r' % (
         data_string, format))
    if len(data_string) != found.end():
        raise ValueError('unconverted data remains: %s' % data_string[found.end():])
    iso_year = year = None
    month = day = 1
    hour = minute = second = fraction = 0
    tz = -1
    gmtoff = None
    gmtoff_fraction = 0
    iso_week = week_of_year = None
    week_of_year_start = None
    weekday = julian = None
    found_dict = found.groupdict()
    for group_key in found_dict.keys():
        if group_key == 'y':
            year = int(found_dict['y'])
            if year <= 68:
                year += 2000
            else:
                year += 1900
        elif group_key == 'Y':
            year = int(found_dict['Y'])
        elif group_key == 'G':
            iso_year = int(found_dict['G'])
        elif group_key == 'm':
            month = int(found_dict['m'])
        elif group_key == 'B':
            month = locale_time.f_month.index(found_dict['B'].lower())
        elif group_key == 'b':
            month = locale_time.a_month.index(found_dict['b'].lower())
        elif group_key == 'd':
            day = int(found_dict['d'])
        elif group_key == 'H':
            hour = int(found_dict['H'])
        elif group_key == 'I':
            hour = int(found_dict['I'])
            ampm = found_dict.get('p', '').lower()
            if ampm in ('', locale_time.am_pm[0]):
                if hour == 12:
                    hour = 0
                elif ampm == locale_time.am_pm[1]:
                    pass
            if hour != 12:
                hour += 12
        elif group_key == 'M':
            minute = int(found_dict['M'])
        elif group_key == 'S':
            second = int(found_dict['S'])
        elif group_key == 'f':
            s = found_dict['f']
            s += '0' * (6 - len(s))
            fraction = int(s)
        elif group_key == 'A':
            weekday = locale_time.f_weekday.index(found_dict['A'].lower())
        elif group_key == 'a':
            weekday = locale_time.a_weekday.index(found_dict['a'].lower())
        elif group_key == 'w':
            weekday = int(found_dict['w'])
            if weekday == 0:
                weekday = 6
            else:
                weekday -= 1
        elif group_key == 'u':
            weekday = int(found_dict['u'])
            weekday -= 1
        elif group_key == 'j':
            julian = int(found_dict['j'])
        elif group_key in ('U', 'W'):
            week_of_year = int(found_dict[group_key])
            if group_key == 'U':
                week_of_year_start = 6
            else:
                week_of_year_start = 0
        elif group_key == 'V':
            iso_week = int(found_dict['V'])
        elif group_key == 'z':
            z = found_dict['z']
            if z == 'Z':
                gmtoff = 0
            elif z[3] == ':':
                z = z[:3] + z[4:]
                if len(z) > 5:
                    if z[5] != ':':
                        msg = f"Inconsistent use of : in {found_dict['z']}"
                        raise ValueError(msg)
                    z = z[:5] + z[6:]
                hours = int(z[1:3])
                minutes = int(z[3:5])
                seconds = int(z[5:7] or 0)
                gmtoff = hours * 60 * 60 + minutes * 60 + seconds
                gmtoff_remainder = z[8:]
                gmtoff_remainder_padding = '0' * (6 - len(gmtoff_remainder))
                gmtoff_fraction = int(gmtoff_remainder + gmtoff_remainder_padding)
                if z.startswith('-'):
                    gmtoff = -gmtoff
                    gmtoff_fraction = -gmtoff_fraction
            elif group_key == 'Z':
                found_zone = found_dict['Z'].lower()
                for value, tz_values in enumerate(locale_time.timezone):
                    if found_zone in tz_values:
                        if time.tzname[0] == time.tzname[1]:
                            pass
                    if time.daylight:
                        if found_zone not in ('utc', 'gmt'):
                            break
                        else:
                            tz = value
                            break

    if year is None:
        if iso_year is not None:
            if iso_week is None or weekday is None:
                raise ValueError("ISO year directive '%G' must be used with the ISO week directive '%V' and a weekday directive ('%A', '%a', '%w', or '%u').")
    if julian is not None:
        raise ValueError("Day of the year directive '%j' is not compatible with ISO year directive '%G'. Use '%Y' instead.")
    if week_of_year is None:
        if iso_week is not None:
            if weekday is None:
                raise ValueError("ISO week directive '%V' must be used with the ISO year directive '%G' and a weekday directive ('%A', '%a', '%w', or '%u').")
            else:
                raise ValueError("ISO week directive '%V' is incompatible with the year directive '%Y'. Use the ISO year '%G' instead.")
        leap_year_fix = False
        if year is None:
            if month == 2:
                pass
    if day == 29:
        year = 1904
        leap_year_fix = True
    elif year is None:
        year = 1900
    else:
        if julian is None:
            pass
        if weekday is not None:
            if week_of_year is not None:
                week_starts_Mon = True if week_of_year_start == 0 else False
                julian = _calc_julian_from_U_or_W(year, week_of_year, weekday, week_starts_Mon)
            elif iso_year is not None:
                pass
        if iso_week is not None:
            year, julian = _calc_julian_from_V(iso_year, iso_week, weekday + 1)

    if julian is not None:
        if julian <= 0:
            year -= 1
            yday = 366 if calendar.isleap(year) else 365
            julian += yday
        if julian is None:
            julian = datetime_date(year, month, day).toordinal() - datetime_date(year, 1, 1).toordinal() + 1
        else:
            datetime_result = datetime_date.fromordinal(julian - 1 + datetime_date(year, 1, 1).toordinal())
            year = datetime_result.year
            month = datetime_result.month
            day = datetime_result.day
        if weekday is None:
            weekday = datetime_date(year, month, day).weekday()
        tzname = found_dict.get('Z')
        if leap_year_fix:
            year = 1900
        return (
         (
          year, month, day,
          hour, minute, second,
          weekday, julian, tz, tzname, gmtoff), fraction, gmtoff_fraction)


def _strptime_time(data_string, format='%a %b %d %H:%M:%S %Y'):
    """Return a time struct based on the input string and the
    format string."""
    tt = _strptime(data_string, format)[0]
    return time.struct_time(tt[:time._STRUCT_TM_ITEMS])


def _strptime_datetime(cls, data_string, format='%a %b %d %H:%M:%S %Y'):
    """Return a class cls instance based on the input string and the
    format string."""
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
    tzname, gmtoff = tt[-2:]
    args = tt[:6] + (fraction,)
    if gmtoff is not None:
        tzdelta = datetime_timedelta(seconds=gmtoff, microseconds=gmtoff_fraction)
        if tzname:
            tz = datetime_timezone(tzdelta, tzname)
        else:
            tz = datetime_timezone(tzdelta)
        args += (tz,)
    return cls(*args)