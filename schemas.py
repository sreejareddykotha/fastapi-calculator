from datetime import datetime
from typing import Literal
from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CalculationCreate(BaseModel):
    a: float
    b: float
    type: Literal["Add", "Sub", "Multiply", "Divide"]

    @field_validator("b")
    @classmethod
    def validate_divide_by_zero(cls, v, info):
        if info.data.get("type") == "Divide" and v == 0:
            raise ValueError("Division by zero is not allowed")
        return v


class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: str
    result: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)