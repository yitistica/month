#!/usr/bin/env python

"""Tests for `month` package."""

from mock import patch, call
import pytest
from month import month
from month.month import MDelta
import pickle

con_data = [({}, 0),  # null case;
            (15, 15),  # case without kwargs;

            ({'years': 2, 'months': 3}, 27),
            ({'years': 1}, 12),
            ({'months': 2}, 2),

            ({'years': 2.5, 'months': 1.2}, 'TypeError'),
            ]


@pytest.mark.parametrize("kwargs, expected", con_data)
@patch.object(month, '_check_int_field', wraps=month._check_int_field)
def test_mdelta_construct(check_int_field_func, kwargs, expected):
    if isinstance(expected, int):  # expected, expected month is given;
        if isinstance(kwargs, dict):
            case = MDelta(**kwargs)

            if 'months' in kwargs:
                months = kwargs['months']
            else:
                months = 0

            if 'years' in kwargs:
                int_check_calls = [call(kwargs['years']), call(months)]
            else:
                int_check_calls = [call(months)]

        elif isinstance(kwargs, int):
            # optional is supplied, representing months;
            case = MDelta(kwargs)
            int_check_calls = [call(kwargs)]
        else:
            raise TypeError('check arg types.')

        check_int_field_func.assert_has_calls(int_check_calls, any_order=False)
        assert case.months == expected  # test conversion;

    else:  # test wrong input:
        if expected == 'TypeError':
            with pytest.raises(TypeError) as execinfo:
                MDelta(**kwargs)
            assert \
                execinfo.value.args[0] == \
                'integer argument expected, got float'


def test_delta_operations():
    delta_1 = MDelta(years=2, months=5)
    delta_2 = MDelta(months=29)
    delta_3 = MDelta(months=30)
    delta_4 = MDelta(years=-1, months=5)

    # str & repr:
    assert str(delta_1) == '29months'
    assert repr(delta_1) == 'mdelta(29)'

    # equality & inequality
    assert delta_1 == delta_2
    assert not delta_1 == delta_3
    assert delta_1 <= delta_2
    assert not delta_1 < delta_2
    assert delta_1 < delta_3
    assert delta_1 >= delta_2
    assert not delta_1 > delta_2
    assert delta_3 > delta_1

    # operators:
    assert delta_1 + delta_3 == delta_3 + delta_1
    assert delta_1 * 2 == 2 * delta_1

    assert delta_1 + delta_3 == MDelta(59)
    assert delta_1 - delta_3 == MDelta(-1)
    assert +delta_1 == delta_1
    assert -delta_1 == MDelta(years=-2, months=-5)
    assert abs(delta_4) == MDelta(7)
    assert delta_1 * 2 == 2 * delta_1 == MDelta(58)

    assert delta_1 + 5 == MDelta(34)
    assert delta_1 - 5 == MDelta(24)

    assert pickle.loads(
        pickle.dumps(delta_1,
                     protocol=pickle.HIGHEST_PROTOCOL))._months == 29
