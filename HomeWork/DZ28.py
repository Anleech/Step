class Descriptor:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, (int or float)) or value <= 0:
            raise ValueError(f"{self.__name} должно быть положительным числом числом")
        instance.__dict__[self.__name] = value


class Order:
    price = Descriptor()
    amount = Descriptor()

    def __init__(self, name, price, amount):
        self.product = name
        self.price = price
        self.amount = amount

    def cost(self):
        return self.price * self.amount

    def info(self):
        print(f"Тест:\nOrder('{self.product}',{self.price},{self.amount})")


p = Order('apple', 5, 10)

p.info()
print()
print(p.cost())
