import sqlite3
import time
import math

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_post(self, title, text, url):
        try:
            self.__cur.execute("SELECT COUNT() as 'count' FROM posts WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Статья с таким URL уже существует")
                return False
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)", (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления поста " + str(e))
            return False
        return True

    def get_posts_anonce(self):
        try:
            self.__cur.execute("SELECT id, title, text, url FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения поста " + str(e))
        return []

    def get_post(self, alias):
        try:
            self.__cur.execute(f"SELECT title, text, url FROM posts WHERE url='{alias}' LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения поста !!!! " + str(e))

        return False, False





    def add_work(self, title, text, url, price):
        try:
            price = int(price)
            self.__cur.execute("SELECT COUNT() as 'count' FROM works WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Работа с таким URL уже существует")
                return False
            if price < 0:
                print('Стоимость работы не может быть отрицательной')
                return False
            self.__cur.execute("INSERT INTO works VALUES(NULL, ?, ?, ?, ?)", (title, text, url, price))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления работы " + str(e))
            return False
        return True


    def get_works_anonce(self):
        try:
            self.__cur.execute("SELECT id, title, text, url, price FROM works ORDER BY price DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения работы " + str(e))
        return []


    def get_work(self, alias):
        try:
            self.__cur.execute(f"SELECT title, text, url, price FROM works WHERE url='{alias}' LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения работы !!!! " + str(e))

        return False, False