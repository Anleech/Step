import pickle
import os.path


class Article:
    def __init__(self, title, genre, producer, year, duration, studio, actor):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actor = actor

    def __str__(self):
        return f"{self.title} (Жанр - {self.genre}. {self.year} год)"


class ArticleModel:
    def __init__(self):
        self.db_film = 'film.txt'
        self.articles = self.load_data()

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_singe_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название фильма": article.title,
            "жанр": article.genre,
            "режиссер": article.producer,
            "год выпуска": article.year,
            "длительность": article.duration,
            "студия": article.studio,
            "актеры": article.actor
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_film):
            with open(self.db_film, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_film, 'wb') as f:
            pickle.dump(self.articles, f)
