class Book:
    title = "Название"
    issue_year = "00.00.0000"
    publisher = "Издатель"
    genre = "Жанр"
    autor = "Автор"
    price = "00"

    def print_info(self):
        print(" Данные о книге ".center(50, "*"))
        print(f"Название: {self.title}\nГод выпуска: {self.issue_year}\n"
              f"Издатель: {self.publisher}\nЖанр: {self.genre}\n"
              f"Автор: {self.autor}\nЦена: {self.price}")
        print("=" * 50)

    def input_info(self, first_title, issue_year, publisher, genre, autor, price):
        self.title = first_title
        self.issue_year = issue_year
        self.publisher = publisher
        self.genre = genre
        self.autor = autor
        self.price = price

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_issue_year(self, issue_year):
        self.issue_year = issue_year

    def get_issue_year(self):
        return self.issue_year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_autor(self, autor):
        self.autor = autor

    def get_autor(self):
        return self.autor

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


b1 = Book()
b1.input_info("Начинаем программировать на Python.", "2022", "БХВ", "Языки программирования", "Гэддис Тони", "1758 ₽")
b1.print_info()

