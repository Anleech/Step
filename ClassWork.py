from abc import ABC, abstractmethod


class Currency(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def covert_to_rub(self):
        pass

    def print_value(self):
        print(self.value, end=' ')


class Dollar(Currency):
    rate_to_rub = 74.16
    suffix = 'USD'

    def covert_to_rub(self):
        rub = self.value * Dollar.rate_to_rub
        return rub

    def print_value(self):
        super().print_value()
        print(Dollar.suffix, end=' ')


class Euro(Currency):
    rate_to_rub = 90.14
    suffix = 'EUR'

    def covert_to_rub(self):
        rub = self.value * Euro.rate_to_rub
        return rub

    def print_value(self):
        super().print_value()
        print(Euro.suffix, end=' ')


d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
e = [Euro(5), Euro(10), Euro(50), Euro(100)]

print('*' * 30)
for elem in d:
    elem.print_value()
    print(f'= {elem.covert_to_rub():.2f} RUB')

print('*' * 30)
for elem in e:
    elem.print_value()
    print(f'= {elem.covert_to_rub():.2f} RUB')
