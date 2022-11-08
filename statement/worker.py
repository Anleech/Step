from statement import employee


class Worker(employee.Employee):
    def __init__(self, code, name, hours):
        super().__init__(code, name)
        self.__wage = 100
        self.__hours = hours
        self.__salary = 0

    def salary(self):
        self.__salary = self.__wage * self.__hours

    def show_info(self):
        self.salary()
        super().show_info()
        print(f'- Проверить сумму: {self.__salary}')
