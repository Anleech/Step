from statement import employee


class Manager(employee.Employee):
    def __init__(self, code, name, commission):
        super().__init__(code, name)
        self.__wage = 1000
        self.__commission = commission / 100
        self.__salary = 0

    def salary(self):
        self.__salary = self.__wage + (self.__wage * self.__commission)

    def show_info(self):
        self.salary()
        super().show_info()
        print(f'- Проверить сумму: {self.__salary:.0f}')
