from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.connection import get_db
from models.user import User
from schemas.user import UserSignup
from core.security import hash_password

router = APIRouter(prefix="/auth", tags=["User Authentication"])

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(payload: UserSignup, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
        
    new_user = User(
        full_name=payload.full_name,
        email=payload.email,
        password=hash_password(payload.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully!", "user_id": new_user.id}