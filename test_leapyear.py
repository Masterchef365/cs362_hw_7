import pytest
from leap_year import is_leap_year

def test_is_leap_year():
    assert(is_leap_year(2000))
    assert(is_leap_year(2020))
    assert(is_leap_year(1968))

    assert(not is_leap_year(2003))
    assert(not is_leap_year(2021))
    assert(not is_leap_year(1961))

def test_type():
    with pytest.raises(TypeError):
        is_leap_year(2.3)
    with pytest.raises(TypeError):
        is_leap_year("wow")

def test_negative():
    with pytest.raises(ValueError):
        is_leap_year(-213)
