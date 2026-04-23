import pytest
from pydantic import ValidationError
from schemas import UserCreate

def test_user_create_valid():
    user = UserCreate(
        username="alice",
        email="alice@example.com",
        password="secret123"
    )
    assert user.username == "alice"

def test_user_create_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            username="alice",
            email="not-an-email",
            password="secret123"
        )

def test_user_create_short_password():
    with pytest.raises(ValidationError):
        UserCreate(
            username="alice",
            email="alice@example.com",
            password="123"
        )