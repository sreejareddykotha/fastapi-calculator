import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from schemas import CalculationCreate
from main import create_calculation
from database import SessionLocal
from models import Calculation


def test_create_calculation_add():
    db = SessionLocal()
    try:
        calc = CalculationCreate(a=2, b=3, type="Add")
        result = create_calculation(calc, db)

        assert result.id is not None
        assert result.a == 2
        assert result.b == 3
        assert result.type == "Add"
        assert result.result == 5

        saved = db.query(Calculation).filter(Calculation.id == result.id).first()
        assert saved is not None
        assert saved.result == 5
    finally:
        db.close()


def test_create_calculation_divide():
    db = SessionLocal()
    try:
        calc = CalculationCreate(a=8, b=2, type="Divide")
        result = create_calculation(calc, db)

        assert result.result == 4
    finally:
        db.close()