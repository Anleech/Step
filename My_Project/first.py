import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, get_flashed_messages


DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'e9e701b7815f5dce89f37cd8ea3f7f2b19fffb75'


app = Flask(__name__)
app.config.from_object(__name__)


app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [
    {"name": "Главная страница", "url": "home"},
    {"name": "Мои проекты", "url": "works"},
    {"name": "Технологии", "url": "skills"},
    {"name": "Блог", "url": "blog"},
    {"name": "Контакты", "url": "contact"}
]


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html", title="Главная", menu=menu)


@app.route("/works")
def works():
    return render_template("works.html", title="Мои проекты", menu=menu)


@app.route("/skills")
def skills():
    return render_template("skills.html", title="Технологии", menu=menu)


@app.route("/blog")
def blog():
    return render_template("blog.html", title="Блог", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['message']) >= 10:
            flash('Сообщение отправлено!', category='success')
        else:
            flash('Сообщение не отправлено.Минимальная длинна должна быть 10 символов', category='error')
    return render_template("contact.html", title="Контакты", menu=menu)


@app.errorhandler(404)
def page_nat_found(error):
    return render_template("page404.html", title="Страница не найденна", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
