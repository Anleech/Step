from jinja2 import Environment, FileSystemLoader

text = [
    {"header": "Домашнее задание", "body_h1": "Страница с домашним заданием", "body_p": "Домашнее задание выполнено!!!"}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(data=text)

print(msg)
