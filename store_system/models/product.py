from sqlalchemy import Column, Integer, String, Float
from database.connection import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)