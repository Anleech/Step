import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase

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


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/home")
@app.route("/")
def home():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("home.html", title="Главная", menu=dbase.get_menu())


@app.route("/works")
def works():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("works.html", title="Курсы", menu=dbase.get_menu(), works=dbase.get_works_anonce())

@app.route("/add_work", methods=["POST", "GET"])
def add_work():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        if len(request.form['name']) < 30 and len(request.form['work']) > 10 and len(request.form['price']) > 0:
            res = dbase.add_work(request.form['name'], request.form['work'], request.form['url'], request.form['price'])
            if not res:
                flash("Ошибка добавления работы", category="error")
            else:
                flash("Работа добавлен успешно", category="success")
        else:
            flash("Ошибка добавления работы", category="error")

    return render_template('add_work.html', menu=dbase.get_menu(), title="Добавление работы")


@app.route("/work/<alias>")
def show_work(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, work, url, price = dbase.get_work(alias)
    if not title:
        abort(404)

    return render_template('work.html', menu=dbase.get_menu(), title=title, work=work, url=url, price=price)










@app.route("/skills")
def skills():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("skills.html", title="Технологии", menu=dbase.get_menu())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash("Ошибка добавления поста", category="error")
            else:
                flash("Пост добавлен успешно", category="success")
        else:
            flash("Ошибка добавления поста", category="error")

    return render_template('add_post.html', menu=dbase.get_menu(), title="Добавление поста")


@app.route("/post/<alias>")
def show_post(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, post, url = dbase.get_post(alias)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)



@app.route("/blog")
def blog():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("blog.html", title="Блог", menu=dbase.get_menu(), posts=dbase.get_posts_anonce())


@app.route("/contact", methods=["POST", "GET"])
def contact():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        if len(request.form['message']) >= 10:
            flash('Сообщение отправлено!', category='success')
        else:
            flash('Сообщение не отправлено.Минимальная длинна должна быть 10 символов', category='error')
    return render_template("contact.html", title="Контакты", menu=dbase.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template("page404.html", title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)
