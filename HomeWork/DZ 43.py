import sqlite3 as sq

data = [('Стол', 12), ('Стул', 15), ('Шкаф', 7), ('Тумба', 30), ('Ковёр', 58)]

with sq.connect("goods.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS goods (
        goods_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        amount INTEGER
    )""")

    cur.executemany("INSERT INTO goods VALUES(NULL,?,?)", data)
