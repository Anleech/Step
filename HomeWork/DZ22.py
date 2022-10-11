# 1 get и set
# ===========================================================
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(__value, rate):
#         return __value * rate
#
#     def get_num(self):
#         return self.__num
#
#     def set_num(self, num):
#         self.__num = num
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def get_value(self):
#         return self.__value
#
#     def set_value(self, value):
#         self.__value = value
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.__value} {Account.suffix}')
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты были успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# print(f'Счет #{acc.get_num()} принадлежит {acc.get_surname()} был открыт.')
# print('*' * 50)
# print(f'Информация о счете:')
# print('-' * 20)
# print(f'#{acc.get_num()}')
# print(f'Владелец: {acc.get_surname()}')
# acc.print_balance()
# print(f'Проценты: {acc.get_percent():.0%}')
# print('-' * 20)
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.set_surname('Дюма')
#
# print(f'Информация о счете:')
# print('-' * 20)
# print(f'#{acc.get_num()}')
# print(f'Владелец: {acc.get_surname()}')
# acc.print_balance()
# print(f'Проценты: {acc.get_percent():.0%}')
# print('-' * 20)
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()


# 2 property
# =======================================================

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        # print(f'Счет #{self.__num} принадлежит {self.__surname} был открыт.')
        # print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(__value, rate):
        return __value * rate

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent):
        self.__percent = percent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')

    def print_balance(self):
        print(f'Текущий баланс {self.__value} {Account.suffix}')

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению у вас нет {val} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()


acc = Account('12345', 'Долгих', 0.03, 1000)

print(f'Счет #{acc.num} принадлежит {acc.surname} был открыт.')
print('*' * 50)
print(f'Информация о счете:')
print('-' * 20)
print(f'#{acc.num}')
print(f'Владелец: {acc.surname}')
acc.print_balance()
print(f'Проценты: {acc.percent:.0%}')
print('-' * 20)
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()

Account.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.surname = 'Дюма'
print(f'Счет #{acc.num} принадлежит {acc.surname} был открыт.')
print('*' * 50)
print(f'Информация о счете:')
print('-' * 20)
print(f'#{acc.num}')
print(f'Владелец: {acc.surname}')
acc.print_balance()
print(f'Проценты: {acc.percent:.0%}')
print('-' * 20)
print()

acc.add_percents()
print()

acc.withdraw_money(3000)
print()

acc.withdraw_money(100)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()
