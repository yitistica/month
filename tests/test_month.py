#!/usr/bin/env python

"""Tests for `month` package."""

#!/usr/bin/env python

"""Tests for `month` package."""

from mock import patch, call
import pytest
from month import month as month_module
from month.month import Month, MDelta


@patch.object(month_module, '_check_date_fields', wraps=month_module._check_date_fields)
def test_month_construct(_check_date_fields):
    # normal case:
    mon = Month(2019, 11)
    _check_date_fields.assert_called_once_with(2019, 11)
    assert mon._year == 2019
    assert mon._month == 11

    # out of bound error (year):
    with pytest.raises(ValueError) as exec_info:
        Month(-1, 2)
    assert exec_info.value.args[0] == 'year must be in %d..%d' % (month_module.MINYEAR, month_module.MAXYEAR)
    assert exec_info.value.args[1] == -1

    with pytest.raises(ValueError) as exec_info:
        Month(2019, -1)
    assert exec_info.value.args[0] == 'month must be in 1..12'
    assert exec_info.value.args[1] == -1

    # float type error:
    with pytest.raises(TypeError) as exec_info:
        Month(2019, 1.5)
    assert exec_info.value.args[0] == 'integer argument expected, got float'
