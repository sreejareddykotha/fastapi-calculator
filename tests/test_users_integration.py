from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


def test_create_user_success():

    unique = str(int(time.time()))

    response = client.post(
        "/users",
        json={
            "username": f"alice_{unique}",
            "email": f"alice_{unique}@example.com",
            "password": "secret123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "username" in data
    assert "email" in data

    assert "password_hash" not in data


def test_create_user_duplicate():

    unique = str(int(time.time()))

    user_data = {
        "username": f"bob_{unique}",
        "email": f"bob_{unique}@example.com",
        "password": "secret123"
    }

    client.post("/users", json=user_data)

    response = client.post("/users", json=user_data)

    assert response.status_code == 400


def test_login_user_success():

    unique = str(int(time.time()))

    username = f"user_{unique}"

    client.post(
        "/users",
        json={
            "username": username,
            "email": f"{username}@example.com",
            "password": "secret123"
        }
    )

    response = client.post(
        "/users/login",
        json={
            "username": username,
            "password": "secret123"
        }
    )

    assert response.status_code == 200