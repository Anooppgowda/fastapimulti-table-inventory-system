from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from database.connection import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="RESTRICT"), nullable=False)
    quantity_ordered = Column(Integer, nullable=False)
    status = Column(String(50), default="Processed")
    order_date = Column(DateTime, default=datetime.utcnow)