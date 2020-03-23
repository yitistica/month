from .month import Month, _check_int_field, _check_date_fields
from datetime import date, timedelta


class XMonth(Month):
    """
    extended month functions:
    """
    def __new__(cls, year: int, month: int):
        return super().__new__(cls, year=year, month=month)

    def __init__(self, year: int, month: int):
        super().__init__(year=year, month=month)

    @classmethod
    def from_integer(cls, date_int):
        """
        convert int representation to month;
        :param date_int: yearmonth, 202001, month must consist of 2 places;
        :return:
        """
        date_int = _check_int_field(date_int)
        year = int(str(date_int)[:-2])
        month = int(str(date_int)[-2:])
        year, month = _check_date_fields(year, month)
        return cls(year, month)

    def to_int(self):
        return int(str(self.year) + str(self.month))

    def first_date(self):
        return date(self.year, self.month, 1)

    def last_date(self):
        next_month = self + 1
        return date(next_month.year, next_month.month, 1) - timedelta(days=1)

    def if_in_this_month(self, date_time):
        return self == Month(date_time.year, date_time.month)

    def next_n_month(self, n=1):
        return self + n

    def __next__(self):
        return self + 1

    def count(self):
        pass
