from pydantic import BaseModel, Field

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity_ordered: int = Field(..., gt=0)