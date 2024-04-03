"""
Приложение ХИМЧИСТКА для некоторой организации. БД должна содержать
таблицу Услуги со следующей структурой записи: ФИО мастера, ФИО клиента, тип
чистки, стоимость, скидка.
"""

import sqlite3 as sq
from client_data import client_data

with sq.connect("services.db") as conn:
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS services""")
    cur.execute("""CREATE TABLE IF NOT EXISTS services (
        id_service INTEGER PRIMARY KEY AUTOINCREMENT,
        fio_master TEXT,
        fio_client TEXT,
        type TEXT,
        price INTEGER,
        discount INTEGER
    )""")

with sq.connect("services.db") as conn:
    cur = conn.cursor()
    cur.executemany(
        """INSERT INTO services (fio_master, fio_client, type, price, discount) VALUES (?,?,?,?,?)""", client_data
    )

# Поиск
with sq.connect("services.db") as conn:
    cur = conn.cursor()

    cur.execute("""SELECT * FROM services WHERE price < 1000 AND type LIKE 'Химчистка%' """)
    print(f"\nХимчистка < 1000: {cur.fetchall()}")

    cur.execute("""SELECT  * FROM services WHERE type LIKE 'Чистка%' """)
    print(f"Чистка: {cur.fetchall()}")

    cur.execute("""SELECT  * FROM services WHERE fio_master = 'Сергеев Сергей Сергеевич' """)
    print(f"Сергеев Сергей Сергеевич: {cur.fetchall()}\n\n")

# Редактирование
with sq.connect("services.db") as conn:
    cur = conn.cursor()

    cur.execute("""SELECT * FROM services WHERE discount = 5""")
    print(f"discount 5 to 7: {cur.fetchall()}\n\tUPDATE...")
    cur.execute("""UPDATE services SET discount = 7 WHERE discount = 5""")
    cur.execute("""SELECT * FROM services WHERE discount = 7""")
    print(f"discount 5 to 7: {cur.fetchall()}\n")

    cur.execute("""SELECT * FROM services WHERE type LIKE 'Чистка%' """)
    print(f"Чистка to Порча: {cur.fetchall()}\n\tUPDATE...")
    cur.execute("""UPDATE services SET type =  REPLACE(type, 'Чистка', 'Порча') WHERE type LIKE 'Чистка%' """)
    cur.execute("""SELECT * FROM services WHERE type LIKE 'Порча%' """)
    print(f"Чистка to Порча: {cur.fetchall()}\n")

    cur.execute("""SELECT * FROM services WHERE discount = 15 AND type LIKE 'Химчистка%' """)
    print(f"discount 15 to 2: {cur.fetchall()}\n\tUPDATE...")
    cur.execute("""UPDATE services SET discount = 2 WHERE discount = 15 AND type LIKE 'Химчистка%'""")
    cur.execute("""SELECT * FROM services WHERE discount = 2 AND type LIKE 'Химчистка%' """)
    print(f"discount 15 to 2: {cur.fetchall()}\n")


# Удаление
with sq.connect("services.db") as conn:
    cur = conn.cursor()

    cur.execute("""SELECT * FROM services WHERE discount > 15 """)
    print(f"discount > 15: {cur.fetchall()}\n\tDELETE...")
    cur.execute("""DELETE FROM services WHERE discount > 15 """)
    cur.execute("""SELECT * FROM services WHERE discount > 15 """)
    print(f"discount > 15: {cur.fetchall()}\n")

    cur.execute("""SELECT * FROM services WHERE price < 1000 AND type LIKE 'Химчистка%' """)
    print(f"Химчистка < 1000: {cur.fetchall()}\n\tDELETE...")
    cur.execute("""DELETE FROM services WHERE  price < 1000 AND type LIKE 'Химчистка%' """)
    cur.execute("""SELECT * FROM services WHERE price < 1000 AND type LIKE 'Химчистка%' """)
    print(f"Химчистка < 1000: {cur.fetchall()}\n")

    cur.execute("""SELECT * FROM services WHERE fio_master = 'Александров Александр Александрович' """)
    print(f"Александров Александр Александрович: {cur.fetchall()}\n\tDELETE...")
    cur.execute("""DELETE FROM services WHERE fio_master = 'Александров Александр Александрович' """)
    cur.execute("""SELECT * FROM services WHERE fio_master = 'Александров Александр Александрович' """)
    print(f"Александров Александр Александрович: {cur.fetchall()}")
