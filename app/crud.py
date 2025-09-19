from app.models import Product
from app.database import db_session

def create_product(name, stock_quantity, price, description):
    product = Product(name=name, stock_quantity=stock_quantity, price=price, description=description)
    db_session.add(product)
    db_session.commit()
    return product
