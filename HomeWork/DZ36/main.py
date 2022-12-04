from parse import Parser


def main():
    for i in range(3, 5):
        pars = Parser(f"https://www.gastronom.ru/recipe/group/3206/chto-prigotovit-na-novyj-god?page={i}", "recipes.txt")
        pars.run()


if __name__ == '__main__':
    main()
