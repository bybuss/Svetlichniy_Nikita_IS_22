import sqlite3 as sq
from data_users import info_users

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )""")

# with sq.connect("saper.db") as con:
#     cur = con.cursor()
#     cur.execute("INSERT INTO users (user_id, name, sex, old, score) VALUES (?, ?, ?, ?, ?)", (1, "bob", 2, 1488, 228))

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO users (user_id, name, sex, old, score) VALUES (?, ?, ?, ?, ?)", info_users)

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE score > 100 AND old > 18")
    res = cur.fetchall()
    print(res)
