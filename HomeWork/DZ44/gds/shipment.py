from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from HomeWork.DZ44.gds.database import Base

# association_table = Table()


class Shipment(Base):
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True)
    storage_name = Column(String, nullable=False)
    product_name = relationship('Product')

    def __repr__(self):
        return f"Склад(ID: {self.id}, Название: {self.storage_name}"
