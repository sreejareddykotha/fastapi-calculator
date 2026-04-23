import logging
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from operations import add, subtract, multiply, divide
from database import SessionLocal, engine
from models import Base, User, Calculation
from schemas import UserCreate, UserRead, UserLogin, CalculationCreate, CalculationRead
from security import hash_password, verify_password
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


@app.post("/users/register", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
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


@app.post("/users", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)


@app.post("/users/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return {"message": "Login successful"}


@app.post("/calculations", response_model=CalculationRead)
def add_calculation(calc: CalculationCreate, db: Session = Depends(get_db)):
    new_calc = create_calculation(calc, db)
    return new_calc


@app.get("/calculations", response_model=list[CalculationRead])
def get_calculations(db: Session = Depends(get_db)):
    calculations = db.query(Calculation).all()
    return calculations


@app.get("/calculations/{calc_id}", response_model=CalculationRead)
def get_calculation(calc_id: int, db: Session = Depends(get_db)):
    calc = db.query(Calculation).filter(Calculation.id == calc_id).first()

    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")

    return calc


@app.put("/calculations/{calc_id}", response_model=CalculationRead)
def update_calculation(calc_id: int, updated_calc: CalculationCreate, db: Session = Depends(get_db)):
    calc = db.query(Calculation).filter(Calculation.id == calc_id).first()

    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")

    calc.a = updated_calc.a
    calc.b = updated_calc.b
    calc.type = updated_calc.type
    calc.result = CalculationFactory.calculate(updated_calc.a, updated_calc.b, updated_calc.type)

    db.commit()
    db.refresh(calc)
    return calc


@app.delete("/calculations/{calc_id}")
def delete_calculation(calc_id: int, db: Session = Depends(get_db)):
    calc = db.query(Calculation).filter(Calculation.id == calc_id).first()

    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")

    db.delete(calc)
    db.commit()
    return {"message": "Calculation deleted successfully"}