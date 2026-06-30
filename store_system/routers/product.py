from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.connection import get_db
from models.product import Product
from schemas.product import ProductCreate

router = APIRouter(prefix="/products", tags=["Product Inventory"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_product(payload: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        title=payload.title,
        price=payload.price,
        stock_quantity=payload.stock_quantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product