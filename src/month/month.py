"""
mdelta and month modules that mimic timedelta & datetime.date;
build on top of datetime;
"""
from datetime import datetime, date, timedelta


# from datetime:
def _cmp(x, y):
    return 0 if x == y else 1 if x > y else -1


# from datetime
MINYEAR = 1
MAXYEAR = 9999
_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# from datetime:
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
            raise TypeError('__int__ returned non-int (type %s)' %
                            type(value).__name__)
        raise TypeError('an integer is required (got type %s)' %
                        type(value).__name__)
    raise TypeError('integer argument expected, got float')


# from datetime
def _check_date_fields(year, month):
    year = _check_int_field(year)
    month = _check_int_field(month)
    if not MINYEAR <= year <= MAXYEAR:
        raise ValueError('year must be in %d..%d' % (MINYEAR, MAXYEAR), year)
    if not 1 <= month <= 12:
        raise ValueError('month must be in 1..12', month)

    return year, month


# derive from datetime
def _parse_isoformat_month(mstr):
    try:
        year, month = mstr.rsplit('-', 1)
        year = int(year)
        month = int(month)
        return year, month
    except ValueError:
        raise ValueError('Invalid month format, use %Y-%m')


def _add_month(year, month, additional_month):
    year, month = _check_date_fields(year, month)
    additional_month = _check_int_field(additional_month)
    years, months = divmod(month + additional_month, 12)
    new_year = year + years
    new_month = months
    return new_year, new_month


# from datetime
def _is_leap(year):
    "year -> 1 if leap year, else 0."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _days_before_year(year):
    "year -> number of days before January 1st of year."
    y = year - 1
    return y*365 + y//4 - y//100 + y//400


# from datetime;
def _days_in_month(year, month):
    "year, month -> number of days in that month in that year."
    assert 1 <= month <= 12, month
    if month == 2 and _is_leap(year):
        return 29
    return _DAYS_IN_MONTH[month]


class MDelta:
    """
    time delta for month:
    """
    def __new__(cls, months: int = 0, **kwargs):
        if 'years' in kwargs:
            years = kwargs.pop('years')
            _check_int_field(years)  # only int accepted;

        _check_int_field(months)
        self = object.__new__(cls)
        return self

    def __init__(self, months: int = 0, **kwargs):
        if 'years' in kwargs:
            years = kwargs.pop('years')
        else:
            years = 0

        self._months = int(years * 12 + months)

    def __str__(self):
        return "%dmonths" % self._months

    def __repr__(self):
        return 'mdelta(%d)' % self._months

    @property
    def months(self):
        """months"""
        return self._months

    def _add(self, other):
        if isinstance(other, MDelta):
            return MDelta(months=self._months + other._months)
        elif isinstance(other, int):
            return MDelta(months=self._months + other)
        else:
            return NotImplemented

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        if isinstance(other, MDelta):
            return self._add(other)
        else:
            return NotImplemented

    def _subtract(self, other):
        if isinstance(other, MDelta):
            return MDelta(months=self._months - other._months)
        elif isinstance(other, int):
            return MDelta(months=self._months - other)
        else:
            return NotImplemented

    def __sub__(self, other):
        return self._subtract(other)

    def __rsub__(self, other):
        if isinstance(other, MDelta):
            return -self + other
        else:
            return NotImplemented

    def __pos__(self):
        return self

    def __neg__(self):
        return MDelta(-self._months)

    def __abs__(self):
        if self._months < 0:
            return -self
        else:
            return self

    def __mul__(self, other):
        if isinstance(other, int):
            return MDelta(self._months * other)
        else:
            return NotImplemented

    __rmul__ = __mul__

    def __eq__(self, other):
        if isinstance(other, MDelta):
            return self._cmp(other) == 0
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, MDelta):
            return self._cmp(other) <= 0
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MDelta):
            return self._cmp(other) < 0
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, MDelta):
            return self._cmp(other) >= 0
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, MDelta):
            return self._cmp(other) > 0
        else:
            return NotImplemented

    def _cmp(self, other):
        assert isinstance(other, MDelta)
        return _cmp(self._months, other._months)


class Month:
    """
    month
    """
    def __new__(cls, year: int, month: int):
        _check_date_fields(year, month)
        self = object.__new__(cls)
        return self

    def __init__(self, year: int, month: int) -> None:
        self._year = year
        self._month = month

    @property
    def year(self):
        """year (1-9999)"""
        return self._year

    @property
    def month(self):
        """month (1-12)"""
        return self._month

    @property
    def quarter(self):
        return self.month // 3 + 1

    def tuple(self):
        return self.year, self.month

    @classmethod
    def fromtuple(cls, month_tuple):
        return cls(month_tuple[0], month_tuple[1])

    def isoformat(self):
        return "%04d-%02d" % (self._year, self._month)

    @classmethod
    def fromisoformat(cls, month_string):
        if not isinstance(month_string, str):
            raise TypeError('fromisoformat: argument must be str')

        return cls(*_parse_isoformat_month(month_string))

    __str__ = isoformat

    def __repr__(self):
        return 'Month(%d, %d)' % (self._year, self._month)

    @classmethod
    def fromordinal(cls, n):
        _date = date.fromordinal(n)
        return cls(_date.year, _date.month)

    @classmethod
    def this_month(cls):
        today = date.today()
        return cls(today.year, today.month)

    def __eq__(self, other):
        if isinstance(other, Month):
            return self._cmp(other) == 0
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Month):
            return self._cmp(other) <= 0
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return self._cmp(other) < 0
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Month):
            return self._cmp(other) >= 0
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Month):
            return self._cmp(other) > 0
        else:
            return NotImplemented

    def add(self, delta):
        if isinstance(delta, MDelta):
            new_year, new_month = _add_month(self.year, self.month, delta.months)
            return Month(new_year, new_month)
        elif isinstance(delta, int):
            return self.add(MDelta(months=delta))
        else:
            raise TypeError(f"adding {type(delta)} type is not allowed.")

    def subtract(self, delta):
        if isinstance(delta, MDelta):
            delta = -delta
            new_year, new_month = _add_month(self.year, self.month, delta.months)
            return Month(new_year, new_month)
        elif isinstance(delta, int):
            mdelta = MDelta(months=delta)
            return self.subtract(mdelta)
        else:
            raise TypeError(f"subtracting {type(delta)} type is not allowed.")

    def diff(self, other):
        """
        difference from
        :param other:
        :return:
        """
        if isinstance(other, Month):
            diff_month = self._year * 12 + self._month - other._year * 12 + other._month
            return MDelta(months=diff_month)
        else:
            raise TypeError(f"dif {type(other)} type is not allowed.")

    def __add__(self, m_delta):
        return self.add(m_delta)

    def __sub__(self, other):
        if isinstance(other, MDelta):
            return self.subtract(other)
        elif isinstance(other, Month):
            return self.diff(other)

    def strftime(self, fmt):
        return fmt.replace('%Y', self.year).replace("%m", self.month)

    @classmethod
    def strptime(cls, date_string, format):
        _datetime = datetime.strptime(date_string, format)
        return cls(_datetime.year, _datetime.month)

    def is_year(self, year):
        return self.year == year

    def is_month(self, month):
        return self.month == month

    def is_quarter(self, quarter):
        return self.quarter == quarter

    def if_leap_year(self):
        return _is_leap(self.year)

    def days(self):
        return _days_in_month(self.year, self.month)

    def _cmp(self, other):
        assert isinstance(other, Month)
        y, m = self._year, self._month
        y2, m2 = other._year, other._month
        return _cmp((y, m), (y2, m2))

