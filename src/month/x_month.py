from .month import Month, MDelta, _check_int_field, _check_date_fields
from datetime import date, timedelta

# from datetime:
_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# from datetime
def _is_leap(year):
    """year -> 1 if leap year, else 0."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# from datetime
def _days_before_year(year):
    """year -> number of days before January 1st of year."""
    y = year - 1
    return y * 365 + y // 4 - y // 100 + y // 400


# from datetime;
def _days_in_month(year, month):
    """year, month -> number of days in that month in that year."""
    assert 1 <= month <= 12, month
    if month == 2 and _is_leap(year):
        return 29
    return _DAYS_IN_MONTH[month]


class XMonth(Month):
    """
    extended month:
    """

    def __new__(cls, year: int, month: int):
        return super().__new__(cls, year=year, month=month)

    def __init__(self, year: int, month: int):
        super().__init__(year=year, month=month)

    @classmethod
    def from_integer(cls, date_int: int):
        """
        convert int representation to month;
        :param date_int: yearmonth, 202001,
            month must consist of 2 places, i.e., Jan is represented by 01;
        :return:
        """
        date_int = _check_int_field(date_int)
        year = int(str(date_int)[:-2])
        month = int(str(date_int)[-2:])
        year, month = _check_date_fields(year, month)
        return cls(year, month)

    def to_int(self):
        return int(str(self.year) + ('0' + str(self.month)
                                     if self.month < 10 else str(self.month)))

    def first_date(self):
        return date(self.year, self.month, 1)

    def last_date(self):
        next_month = self + 1
        return date(next_month.year, next_month.month, 1) - timedelta(days=1)

    def is_leap_year(self):
        return _is_leap(self.year)

    def is_year(self, year: int):
        return self.year == year

    def is_month(self, month: int):
        return self.month == month

    def is_quarter(self, quarter: int):
        return self.quarter == quarter

    def days(self):
        return _days_in_month(self.year, self.month)

    def contain_date(self, date_time):
        return self._year == date_time.year and self._month == date_time.month

    def next_month(self, n=1):
        return self + n

    def __iter__(self):
        return self

    def __next__(self):
        return self.next_month(n=1)

    def dates(self, step: int = 1):
        if step == 0:
            raise ValueError("step cannot be of magnitude 0.")
        step = _check_int_field(step)

        if step < 0:
            _date = self.last_date()
        else:
            _date = self.first_date()

        index = 0
        while self.contain_date(_date):
            yield index, _date
            index += 1
            _date = _date + timedelta(days=step)

    @classmethod
    def range(cls, starting_month, ending_month, step=None):
        def _convert(m):
            if isinstance(m, Month):
                pass
            elif isinstance(m, int):
                m = XMonth.from_integer(date_int=m)
            else:
                raise TypeError("type of month (%s) is not supported." % m)

            return m

        current_month = _convert(m=starting_month)
        ending_month = _convert(m=ending_month)

        if step is None:
            if ending_month >= current_month:
                step = 1
            else:
                step = -1

        if isinstance(step, MDelta):
            pass
        elif isinstance(step, int):
            if step == 0:
                raise ValueError("step cannot be of magnitude 0.")
            step = MDelta(months=step)
        else:
            raise TypeError("type of step (%s) is not supported." % step)

        trend = 1 if step > MDelta(0) else -1

        index = 0
        while trend * (ending_month - current_month) > MDelta(0):
            yield index, current_month
            index += 1
            current_month = current_month + step
