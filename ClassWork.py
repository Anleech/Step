# from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name").get_text()
# row = soup.findAll("div", class_="name")
# row = soup.find_all("div", class_="row")[1].find("div", class_='links').text
# row = soup.find("div", {"class": "name"})
# row = soup.find("div", {"data_set": "salary"})
# row = soup.find("div", text="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)


# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)

# import re

# def get_salary(s):
#     pattern = r"\d+"
#     res = re.findall(pattern, s)[0]
#     print(res)
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)

from bs4 import BeautifulSoup
import requests
import re
import csv

# req = requests.get('https://ru.wordpress.org/')
#
# print(req.text)


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title")
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


def get_html(url):
    r = requests.get(url)
    return r.text


def refind(s):
    res = re.sub(r"\D+", "", s)
    return res


def write_csv(data):
    with open("plugins.csv", "a") as f:
        writer = csv.writer(f, lineterminator="\n", delimiter=";")
        writer.writerow((data['name'], data['url'], data['rating']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all('section', class_="plugin-section")[1]
    plugins = p1.find_all('article')

    for plugin in plugins:
        name = plugin.find("h3").text
        # url = plugin.find("h3").find("a")['href']
        url = plugin.find("h3").find("a").get('href')
        rating = plugin.find("span", class_="rating-count").find("a").text
        r = refind(rating)

        data = {'name': name, 'url': url, 'rating': r}

        write_csv(data)

    # return len(plugins)


def main():
    url = "https://ru.wordpress.org/plugins/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()

