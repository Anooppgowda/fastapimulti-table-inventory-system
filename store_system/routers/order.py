from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.connection import get_db
from models.order import Order
from models.product import Product
from models.user import User
from schemas.order import OrderCreate

router = APIRouter(prefix="/orders", tags=["Orders System"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def place_order(payload: OrderCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == payload.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    product = db.query(Product).filter(Product.id == payload.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
        
    if product.stock_quantity < payload.quantity_ordered:
        raise HTTPException(
            status_code=400, 
            detail=f"Insufficient stock. Only {product.stock_quantity} units available."
        )
        
    product.stock_quantity -= payload.quantity_ordered
    
    new_order = Order(
        user_id=payload.user_id,
        product_id=payload.product_id,
        quantity_ordered=payload.quantity_ordered,
        status="Processed"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    return {
        "message": "Transaction complete! Order processed.",
        "order_id": new_order.id,
        "remaining_stock": product.stock_quantity
    }