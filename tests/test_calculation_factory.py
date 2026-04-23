import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculation_factory import CalculationFactory


def test_add():
    assert CalculationFactory.calculate(2, 3, "Add") == 5


def test_subtract():
    assert CalculationFactory.calculate(5, 2, "Sub") == 3


def test_multiply():
    assert CalculationFactory.calculate(4, 3, "Multiply") == 12


def test_divide():
    assert CalculationFactory.calculate(8, 2, "Divide") == 4


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        CalculationFactory.calculate(8, 0, "Divide")


def test_invalid_type():
    with pytest.raises(ValueError, match="Invalid calculation type"):
        CalculationFactory.calculate(2, 3, "Power")