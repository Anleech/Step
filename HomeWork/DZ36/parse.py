from bs4 import BeautifulSoup
import requests


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        recipes = self.html.find_all('article', class_='col-ms-12')
        for item in recipes:
            try:
                title = item.find('a', class_='material-anons__title').text
            except ValueError:
                title = ''

            try:
                complexity = item.find('span', class_='material-anons__tags').text.strip()
            except ValueError:
                complexity = ''

            try:
                rating = item.find('span', class_='material-anons__like').text.strip()
            except ValueError:
                rating = ''

            try:
                description = item.find('p', class_='material-anons__des').text
            except ValueError:
                description = ''

            try:
                href = 'https://www.gastronom.ru' + item.find('a').get('href')
            except ValueError:
                href = ''

            self.res.append({
                'title': title,
                'complexity': complexity,
                'rating': rating,
                'description': description,
                'href': href
            })

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(f"Рецепт №{i}\n\nНазвание:{item['title']}\n"
                        f"Сложность: {item['complexity']}\nРейтинг {item['rating']}/5\n"
                        f"Краткое описание:\n{item['description']}\n\nСсылка:{item['href']}"
                        f"\n{'='* 50}\n\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()