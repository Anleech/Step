import os

from sqlalchemy import and_, not_, or_, desc, text, distinct, func

from HomeWork.DZ44.gds.database import DATABASE_NAME, Session
import HomeWork.DZ44.create_database as db_creator

from HomeWork.DZ44.gds.product import Product
from HomeWork.DZ44.gds.shipment import Shipment

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

    print("Запрос №1")
    for it in session.query(Product):
        print(it.customer)
    print("*" * 60 + "\n")
    print("Запрос №2")
    print(session.query(Shipment).all())
    print("*" * 60 + "\n")
    print("Запрос №3")
    print(session.query(Product).count())
    print("*" * 60 + "\n")
    print("Запрос №4")
    print(session.get(Product, 3))
    print("*" * 60 + "\n")
    print("Запрос №5")
    for it in session.query(Product).filter(and_(Product.price>=1000, Product.product_name.like('Г%'))):
        print(it)
    print("*" * 60 + "\n")
    print("Запрос №6")
    for it in session.query(Product).order_by(Product.price):
        print(it)
    print("*" * 60 + "\n")
    print("Запрос №7")
    for it in session.query(distinct(Product.storage)):
        print(it)
    print("*" * 60 + "\n")
    print("Запрос №8")
    for it in session.query(func.count(Product.product_name), Shipment.storage_name).join(Shipment).group_by(Shipment.storage_name).having(func.count(Product.price) < 100):
        print(it)
    print("*" * 60 + "\n")
    print("Запрос №9")
    for it in session.query(Product).filter(Product.storage.like("1")).limit(4):
        print(it)
    print("*" * 60 + "\n")
    print("Запрос №10")
    print(session.query(Product).filter(Product.amount.between(0, 20)).all())

