from pydantic import BaseModel, EmailStr, Field

class UserSignup(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)