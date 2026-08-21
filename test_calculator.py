import pytest
from calculator import add, divide


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (0, 5, 5),
        (5, 0, 5),
        (0, 0, 0),
        (2.5, 3.1, 5.6),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),
        (-6, -3, 2.0),
        (-6, 3, -2.0),
        (6, -3, -2.0),
        (0, 5, 0.0),
        (5.0, 2.0, 2.5),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)