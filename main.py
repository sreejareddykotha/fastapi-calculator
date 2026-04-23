import logging
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from operations import add, subtract, multiply, divide
from database import SessionLocal, engine
from models import Base, User, Calculation
from schemas import UserCreate, UserRead, CalculationCreate, CalculationRead
from security import hash_password
from calculation_factory import CalculationFactory

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_calculation(calc: CalculationCreate, db: Session) -> Calculation:
    result = CalculationFactory.calculate(calc.a, calc.b, calc.type)

    new_calc = Calculation(
        a=calc.a,
        b=calc.b,
        type=calc.type,
        result=result
    )

    db.add(new_calc)
    db.commit()
    db.refresh(new_calc)
    return new_calc


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    logger.info("Root endpoint accessed")
    return templates.TemplateResponse(request, "index.html", {})


@app.get("/add")
def add_numbers(a: float, b: float):
    result = add(a, b)
    logger.info(f"Addition: {a} + {b} = {result}")
    return {"result": result}


@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    result = subtract(a, b)
    logger.info(f"Subtraction: {a} - {b} = {result}")
    return {"result": result}


@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    result = multiply(a, b)
    logger.info(f"Multiplication: {a} * {b} = {result}")
    return {"result": result}


@app.get("/divide")
def divide_numbers(a: float, b: float):
    try:
        result = divide(a, b)
        logger.info(f"Division: {a} / {b} = {result}")
        return {"result": result}
    except ZeroDivisionError:
        logger.error(f"Division by zero attempted: {a} / {b}")
        raise HTTPException(status_code=400, detail="Cannot divide by zero")


@app.post("/users", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_username = db.query(User).filter(User.username == user.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists")

    existing_email = db.query(User).filter(User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user