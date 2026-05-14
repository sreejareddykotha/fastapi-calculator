import pytest

from operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulus
)


def test_add():

    assert add(2, 3) == 5


def test_subtract():

    assert subtract(10, 4) == 6


def test_multiply():

    assert multiply(5, 2) == 10


def test_divide():

    assert divide(20, 5) == 4


def test_divide_by_zero():

    with pytest.raises(ZeroDivisionError):

        divide(10, 0)


def test_power():

    assert power(2, 3) == 8


def test_modulus():

    assert modulus(10, 3) == 1


def test_modulus_by_zero():

    with pytest.raises(ZeroDivisionError):

        modulus(10, 0)