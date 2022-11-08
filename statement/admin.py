from statement import employee


class Admin(employee.Employee):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.__wage = 1500

    def show_info(self):
        super().show_info()
        print(f'- Проверить сумму: {self.__wage}')
