from sqlalchemy import Column, Integer, String
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    stock_quantity = Column(Integer)
    price = Column(Integer)
    description = Column(String)
