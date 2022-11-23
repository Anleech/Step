from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text



def write_csv(data):
    with open("best_recipes.csv", "a") as f:
        writer = csv.writer(f, lineterminator="\n", delimiter=";")
        writer.writerow((data['tittle'], data['time'], data['url']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    recipes = soup.find_all('div', class_='rating-block ib')[3]
    recipes_best = recipes.find_all('div', class_='cn-item')

    for i in recipes_best:
        title = i.find("a", class_='h5').text
        time = i.find('div', class_='level-right').find('span').text
        url = i.find('div', class_='photo is-relative').find('a').get('href')
        u = 'https://1000.menu' + url

        data = {'tittle': title, 'time': time, 'url': u}

        write_csv(data)


def main():
    url = "https://1000.menu/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
