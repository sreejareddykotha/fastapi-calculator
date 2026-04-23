# FastAPI Calculator

A simple calculator web application built using FastAPI. It supports basic arithmetic operations and includes unit, integration, and end-to-end testing with CI using GitHub Actions.

## Features

- Addition, Subtraction, Multiplication, Division  
- Interactive web interface (HTML + JavaScript)  
- REST API endpoints  
- Logging for operations and errors  
- Automated testing:
  - Unit tests  
  - Integration tests  
  - End-to-end tests (Playwright)  
- Continuous Integration with GitHub Actions  

## Tech Stack

- Python  
- FastAPI  
- Pytest  
- Playwright  
- GitHub Actions  

## Run Locally

### 1. Create virtual environment
python3 -m venv venv  
source venv/bin/activate  

### 2. Install dependencies
python3 -m pip install -r requirements.txt  

### 3. Run the app
python -m uvicorn main:app --reload  

### 4. Open in browser
http://127.0.0.1:8000  

## Run Tests

pytest  

## Project Structure

fastapi-calculator/  
│── main.py  
│── operations.py  
│── requirements.txt  
│  
├── templates/  
│   └── index.html  
│  
├── tests/  
│   ├── test_main.py  
│   └── test_operations.py  
│  
├── e2e/  
│   └── test_app.py  
│  
└── .github/workflows/  
    └── ci.yml  
    
pgAdmin is configured via Docker Compose using environment variables and is accessible at http://localhost:5050.

## Run Tests Locally

```bash
pytest
```

https://hub.docker.com/r/sreejareddykotha/fastapi-calculator





## Author

Sreeja Reddy Kotha
