import pytest
from calculator import add, divide


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2
    assert add(-5, 10) == 5


def test_add_zero():
    assert add(0, 5) == 5
    assert add(0, 0) == 0


def test_add_floats():
    assert pytest.approx(add(1.5, 2.25)) == 3.75


def test_divide_positive():
    assert divide(10, 2) == 5


def test_divide_negative():
    assert divide(-10, 2) == -5
    assert divide(-12, -3) == 4


def test_divide_zero_numerator():
    assert divide(0, 5) == 0


def test_divide_floats():
    assert pytest.approx(divide(7.5, 2.5)) == 3.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)