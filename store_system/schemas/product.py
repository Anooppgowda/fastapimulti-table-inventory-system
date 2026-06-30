from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    title: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    stock_quantity: int = Field(..., ge=0)