from faker import Faker

from HomeWork.DZ44.gds.database import create_db, Session
from HomeWork.DZ44.gds.product import Product
from HomeWork.DZ44.gds.shipment import Shipment


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    products_names = ['Гвозди', 'Болты', 'Гайки', 'Шурупы', 'Шайбы', 'Гвозди-small', 'Болты-small',
                      'Гайки-small', 'Шурупы-small', 'Шайбы-small']

    storage1 = Shipment(storage_name="Main")
    storage2 = Shipment(storage_name="Second")
    session.add(storage1)
    session.add(storage2)



    faker = Faker('ru_RU')
    storage_list = [storage1, storage2]
    session.commit()

    for _ in range(25):
        customer = faker.last_name()
        product_name = faker.random.choice(products_names)
        price = faker.random.randint(100, 5000)
        amount = faker.random.randint(10, 500)
        storage = faker.random.choice(storage_list)
        product = Product(customer, product_name, price, amount, storage.id)
        session.add(product)
    session.commit()



    session.commit()
    session.close()
