#!/usr/bin/env python

"""Tests for `month` package."""


from month.x_month import XMonth, Month, date


def test_x_month():
    assert isinstance(XMonth(2020, 1), Month)

    assert XMonth.from_integer(202001) == XMonth(2020, 1)
    assert XMonth(2020, 1).to_int() == 202001
    assert XMonth(2020, 11).to_int() == 202011

    assert XMonth(2020, 1).first_date() == date(2020, 1, 1)
    assert XMonth(2020, 1).last_date() == date(2020, 1, 31)
    assert XMonth(2020, 2).last_date() == date(2020, 2, 29)

    assert XMonth(2020, 1).is_leap_year()
    assert not XMonth(2019, 1).is_leap_year()
    assert not XMonth(1900, 1).is_leap_year()

    assert XMonth(2020, 1).is_year(2020)
    assert XMonth(2020, 1).is_month(1)
    assert XMonth(2020, 1).is_quarter(1)

    assert XMonth(2020, 1).days() == 31
    assert XMonth(2020, 2).days() == 29

    assert XMonth(2020, 1).contain_date(date(2020, 1, 10))
    assert XMonth(2020, 1).next_month(2) == XMonth(2020, 3)

    # range
    _total_dates = 0
    for index, _date in XMonth(2020, 1).dates(step=-5):
        _total_dates += 1
        if index == 0:
            assert _date == date(2020, 1, 31)
        elif index == 1:
            assert _date == date(2020, 1, 26)
        elif index == 6:
            assert _date == date(2020, 1, 1)

    assert _total_dates == 7

    _total_months = 0
    for index, mon in XMonth.range(201911, 202002, 1):
        _total_months += 1
        if index == 0:
            assert mon == XMonth(2019, 11)
        elif index == 2:
            assert mon == XMonth(2020, 1)

    assert _total_months == 3


def test_x_month_operator():
    assert XMonth(2020, 1) + 1 == XMonth(2020, 2)
    assert isinstance(XMonth(2020, 1) + 1, XMonth)
    assert isinstance(XMonth(2020, 1) - 1, XMonth)
    assert isinstance(Month(2020, 1) - 1, Month)
    assert isinstance(Month(2020, 1) + 1, Month)
