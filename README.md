# FastAPI Calculator

A simple calculator web application built using FastAPI. It supports basic arithmetic operations and includes unit, integration, and end-to-end testing with CI using GitHub Actions.

---

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

## Docker Image
https://hub.docker.com/r/sreejareddykotha/fastapi-calculator

AUTHOR
Sreeja Reddy Kotha
 
