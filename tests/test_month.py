#!/usr/bin/env python

"""Tests for `month` package."""

import pytest
from mock import patch
from month import month as month_module
from month.month import Month, MDelta, date
import pickle


@patch.object(month_module, '_check_date_fields',
              wraps=month_module._check_date_fields)
def test_month_construct(_check_date_fields):
    # normal case:
    mon = Month(2019, 11)
    _check_date_fields.assert_called_once_with(2019, 11)
    assert mon._year == 2019
    assert mon._month == 11

    # out of bound error (year):
    with pytest.raises(ValueError) as exec_info:
        Month(-1, 2)
    assert \
        exec_info.value.args[0] == 'year must be in %d..%d' \
        % (month_module.MINYEAR, month_module.MAXYEAR)
    assert exec_info.value.args[1] == -1

    with pytest.raises(ValueError) as exec_info:
        Month(2019, -1)
    assert exec_info.value.args[0] == 'month must be in 1..12'
    assert exec_info.value.args[1] == -1

    # float type error:
    with pytest.raises(TypeError) as exec_info:
        Month(2019, 1.5)
    assert exec_info.value.args[0] == 'integer argument expected, got float'


def test_properties():
    mon = Month(2019, 11)
    assert mon.year == 2019
    assert mon.month == 11
    assert mon.quarter == 4

    assert mon.tuple() == (2019, 11)
    assert Month.fromtuple((2019, 11)) == mon

    assert str(mon) == mon.isoformat() == "2019-11"
    assert repr(mon) == 'Month(2019, 11)'
    assert Month.fromisoformat("2019-11") == mon

    with pytest.raises(TypeError) as exec_info:
        Month.fromisoformat(201911)
    assert exec_info.value.args[0] == 'fromisoformat: argument must be str'

    with pytest.raises(ValueError) as exec_info:
        Month.fromisoformat('2019/11')
    assert exec_info.value.args[0] == 'Invalid month format, use %Y-%m'

    with pytest.raises(ValueError) as exec_info:
        Month.fromisoformat('2019-13')
    assert exec_info.value.args[0] == 'month must be in 1..12'

    assert Month.fromordinal(737390) == mon

    with patch('month.month.date') as mock_date:
        mock_date.today.return_value = date(2019, 11, 1)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

        assert Month.this_month() == mon

    assert Month(2019, 11) == Month(2019, 11)
    assert Month(2019, 11) >= Month(2019, 11)
    assert Month(2019, 11) <= Month(2019, 11)
    assert Month(2019, 11) != Month(2019, 12)
    assert Month(2019, 11) > Month(2019, 10)
    assert Month(2019, 10) < Month(2019, 11)

    assert \
        Month(2019, 11).add(MDelta(2)) \
        == Month(2019, 11).add(2) \
        == Month(2019, 11) + MDelta(2) \
        == Month(2019, 11) + 2 \
        == Month(2019, 11) - MDelta(-2) \
        == Month(2020, 1)
    assert \
        Month(2019, 11).subtract(MDelta(2)) \
        == Month(2019, 11).subtract(2) \
        == Month(2019, 11) - 2 \
        == Month(2019, 11) - MDelta(2) \
        == Month(2019, 11) + MDelta(-2) \
        == Month(2019, 9)

    assert \
        Month(2019, 11).diff(Month(2019, 9)) \
        == Month(2019, 11) - Month(2019, 9) == MDelta(2)

    assert Month(2019, 1).strftime('%Y/%m') == '2019/01'

    assert Month.strptime('2019/1', '%Y/%m') == Month(2019, 1)

    assert \
        pickle.loads(pickle.dumps(Month(2019, 1),
                                  protocol=pickle.HIGHEST_PROTOCOL)) \
        == Month(2019, 1)
