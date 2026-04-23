# FastAPI Calculator

A simple calculator web application built using FastAPI. It supports basic arithmetic operations and includes unit, integration, and end-to-end testing with CI using GitHub Actions.

---

## Features

- Addition, Subtraction, Multiplication, Division  
- Interactive web interface (HTML + JavaScript)  
- REST API endpoints  
- User authentication (register & login)
- Calculation CRUD operations
- Logging for operations and errors  
- Automated testing (unit, integration, end-to-end)
- Continuous Integration with GitHub Actions  

---

## Tech Stack

- Python  
- FastAPI  
- Pytest  
- Playwright  
- GitHub Actions  

## Run Locally

 1. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
pytest
```

## API Endpoints

### User
- POST /users/register
- POST /users/login

### Calculations
- GET /calculations
- GET /calculations/{id}
- POST /calculations
- PUT /calculations/{id}
- DELETE /calculations/{id}

## OpenAPI Docs
http://127.0.0.1:8000/docs

CI/CD

GitHub Actions automatically runs tests and builds a Docker image on every push.
If tests pass, the image is pushed to Docker Hub.

## Docker Image
https://hub.docker.com/r/sreejareddykotha/fastapi-calculator

## Tests
The test suite now includes calculation model, schema validation, factory logic, user integration, and calculator end-to-end tests.

AUTHOR
Sreeja Reddy Kotha
 
