import pytest
import source.utils as u


def test_add():
    result = u.add(1, 4)
    assert result == 5


def test_add_strings():
    result = u.add("hello ", "world")
    assert result == "hello world"


def test_divide():
    result = u.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        u.divide(10, 0)
