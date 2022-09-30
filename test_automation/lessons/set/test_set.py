import pytest
import copy

from functions import get_function

set_ = get_function()


# BEGIN (write your solution here)
@pytest.fixture
def data():
    return {"a": {"b": {"c": "d"}}}


def test_plain_set(data):
    data_copy = copy.deepcopy(data)
    set_(data, ['a'], 'value')
    data_copy['a'] = 'value'
    assert data_copy == data


def test_nested_set(data):
    data_copy = copy.deepcopy(data)
    set_(data, ['a', 'b', 'c'], 'value')
    data_copy['a']['b']['c'] = 'value'
    assert data_copy == data


def test_new_property_set(data):
    data_copy = copy.deepcopy(data)
    set_(data, ['a', 'b', 'd'], 'value')
    data_copy['a']['b']['d'] = 'value'
    assert data_copy == data
# END
