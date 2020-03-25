#!/usr/bin/env python

"""Tests for `month` package."""

#!/usr/bin/env python

"""Tests for `month` package."""

from mock import patch
import pytest
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

    assert XMonth(2020, 1).days() == 31
    assert XMonth(2020, 2).days() == 29

    assert XMonth(2020, 1).is_in_this_month(date(2020, 1, 10))
    assert XMonth(2020, 1).next_n_month(2) == XMonth(2020, 3)

