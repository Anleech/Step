from flask import Flask, render_template, url_for

app = Flask(__name__)

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


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Контакты", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
