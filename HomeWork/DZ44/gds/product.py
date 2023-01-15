from sqlalchemy import Column, ForeignKey, Integer, String

from HomeWork.DZ44.gds.database import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    customer = Column(String(100), nullable=False)
    product_name = Column(String(300), nullable=False)
    price = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    storage = Column(Integer, ForeignKey('shipments.id'))

    def __init__(self, customer, product_name, price, amount, storage):
        self.customer = customer
        self.product_name = product_name
        self.price = price
        self.amount = amount
        self.storage = storage

    def __repr__(self):
        return f"Товар(Название: {self.product_name}, Цена: {self.price}, Количество: {self.amount}, " \
               f"Номер склада: {self.storage})"
