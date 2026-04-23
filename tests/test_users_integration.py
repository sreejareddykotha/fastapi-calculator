import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_success():
    response = client.post(
        "/users",
        json={
            "username": "alice_test",
            "email": "alice_test@example.com",
            "password": "secret123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice_test"
    assert data["email"] == "alice_test@example.com"
    assert "password_hash" not in data

def test_create_user_duplicate_username():
    client.post(
        "/users",
        json={
            "username": "bob_test",
            "email": "bob_test1@example.com",
            "password": "secret123"
        }
    )

    response = client.post(
        "/users",
        json={
            "username": "bob_test",
            "email": "bob_test2@example.com",
            "password": "secret123"
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already exists"

def test_create_user_invalid_email():
    response = client.post(
        "/users",
        json={
            "username": "charlie_test",
            "email": "bad-email",
            "password": "secret123"
        }
    )
    assert response.status_code == 422