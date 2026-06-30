# database/connection.py

from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Safely encode the special character '@' inside your password
raw_password = "mysql@8971494596"
encoded_password = quote_plus(raw_password)

# 2. Combine it into your standard MySQL engine string
DATABASE_URL = f"mysql+pymysql://root:{encoded_password}@localhost:3306/store_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()