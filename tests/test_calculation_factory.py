import pytest

from calculation_factory import CalculationFactory


def test_addition():

    result = CalculationFactory.calculate(
        2,
        3,
        "Add"
    )

    assert result == 5


def test_subtraction():

    result = CalculationFactory.calculate(
        10,
        4,
        "Subtract"
    )

    assert result == 6


def test_multiplication():

    result = CalculationFactory.calculate(
        5,
        2,
        "Multiply"
    )

    assert result == 10


def test_division():

    result = CalculationFactory.calculate(
        20,
        5,
        "Divide"
    )

    assert result == 4


def test_power():

    result = CalculationFactory.calculate(
        2,
        3,
        "Power"
    )

    assert result == 8


def test_modulus():

    result = CalculationFactory.calculate(
        10,
        3,
        "Modulus"
    )

    assert result == 1


def test_invalid_calculation_type():

    with pytest.raises(ValueError):

        CalculationFactory.calculate(
            1,
            2,
            "Invalid"
        )