import pytest
from calculator import add, divide


def test_add_positive_numbers():
    assert add(5, 3) == 8


def test_add_negative_numbers():
    assert add(-4, -6) == -10


def test_add_mixed_numbers():
    assert add(-5, 5) == 0


def test_add_zero():
    assert add(0, 10) == 10
    assert add(0, 0) == 0


def test_add_floats():
    assert add(1.5, 2.3) == pytest.approx(3.8)


def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0


def test_divide_negative_numbers():
    assert divide(-12, -3) == 4.0
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0


def test_divide_zero_numerator():
    assert divide(0, 5) == 0.0


def test_divide_floats():
    assert divide(7.5, 2.5) == pytest.approx(3.0)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)