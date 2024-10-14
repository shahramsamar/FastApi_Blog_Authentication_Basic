from fastapi import APIRouter, status, HTTPException, Query, Depends,Path
from sqlalchemy.orm import Session
from core.config_database.database import get_db
from schemas.names import NamesSchema, ResponseNamesSchema, RegisterUserSchema
from models import StudentModel, Users
from typing import Annotated, Optional, List
from fastapi.security import HTTPBasicCredentials, HTTPBasic
import secrets
from fastapi.responses import JSONResponse
from passlib.context import CryptContext  # For hashing passwords

router = APIRouter(tags=["Authentication"])
security = HTTPBasic()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash the password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify the hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Authentication function to verify both username and password from database
def get_current_user(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.email == credentials.username).first()
    print(user)
    if not user or not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return {"username": user.email, "user_id": user.id}

@router.get("/current-user")
def current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)], db: Session = Depends(get_db)):
    user = get_current_user(credentials, db)
    if user:
        return {"username": user["username"], "is_authenticated": True, 'login': True}
    else:
        return {"is_authenticated": False, 'login': False}

@router.post("/register", response_model=dict)
def register_user(user_data: RegisterUserSchema, db: Session = Depends(get_db)):
    # Check if the email already exists
    existing_user = db.query(Users).filter(Users.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create a new user with hashed password
    new_user = Users(
        email=user_data.email,
        user=user_data.user,
        password=hash_password(user_data.password)
    )

    # Add and commit the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "email": new_user.email}

@router.post("/login", response_model=dict)
def login(user_data: RegisterUserSchema, db: Session = Depends(get_db)):
    # Find the user by email
    user = db.query(Users).filter(Users.email == user_data.email).first()

    if not user or not verify_password(user_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    return {"message": f"Welcome {user.email}!", "role": user.user}
