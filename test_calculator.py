import pytest
from calculator import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (0, 5, -5),
    (1, -12, 13)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 3, -6),
    (0, 3, 0)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert str(excinfo.value) == "Деление на ноль"
