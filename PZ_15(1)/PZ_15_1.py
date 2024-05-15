# Вариант 20

"""
Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации.
БД должна содержать таблицу Нотариальные услуги со следующей структурой запи
ФИО клиента, услуга, сумма сделки, комиссионные (доход конторы).

"""
import sqlite3 as sq

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Notarial_Services")
cur.execute('''
    CREATE TABLE IF NOT EXISTS Notarial_Services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name VARCHAR NOT NULL,
        service VARCHAR NOT NULL,
        deal_amount DECIMAL NOT NULL,
        commission DECIMAL NOT NULL
    )
''')

info_tm = [
    (1, 'Иванова Анна Петровна',  'Услуга 1', 15000.99,  50.99),
    (2, 'Смирнов Дмитрий Александрович',  'Услуга 2', 6000.99,  50.99),
    (3, 'Кузнецова Екатерина Сергеевна',  'Услуга 3', 15000.99,  50.99),
    (4, 'Попов Артем Владимирович',  'Услуга 4', 8000.99,  50.99),
    (5, 'Васильева Ольга Ивановна',  'Услуга 5', 5000.99,  50.99),
    (6, 'Петров Игорь Николаевич',  'Услуга 6', 9000.99,  50.99),
    (7, 'Соколова Мария Алексеевна',  'Услуга 7', 15000.99,  50.99),
    (8, 'Михайлов Александр Васильевич',  'Услуга 8', 15000.99,  50.99),
    (9, 'Новикова Татьяна Дмитриевна',  'Услуга 9', 17000.99,  50.99),
    (10, 'Федоров Сергей Павлович',  'Услуга 10', 15500.99,  50.99)
]

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO Notarial_Services VALUES (?, ?, ?, ?, ?)", info_tm)


with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Notarial_Services")
    result = cur.fetchall()
    print(f'Полное содержание таблицы "Нотариальная контора":\n{result}')

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Notarial_Services WHERE deal_amount<6000")
    result = cur.fetchall()
    print(f'Содержание таблицы "Нотариальная контора", где цена меньше 6000:\n{result}')

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Notarial_Services WHERE deal_amount>15000")
    result = cur.fetchall()
    print(f'Содержание таблицы "Нотариальная контора, где цена больше 15000":\n{result}')

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE Notarial_Services SET deal_amount = deal_amount+80 WHERE client_name='Иванова Анна Петровна'")

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE Notarial_Services SET deal_amount = deal_amount+877 WHERE client_name='Петров Игорь Николаевич'")

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE Notarial_Services SET deal_amount = deal_amount+291 WHERE deal_amount>15500")

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM Notarial_Services WHERE service ='Услуга 10'")

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM Notarial_Services WHERE client_name ='Федоров Сергей Павлович'")

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM Notarial_Services WHERE deal_amount>15050")

with sq.connect('tp.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Notarial_Services")
    result = cur.fetchall()
    print(f'Итоговое содержание таблицы "Нотариальная контора":\n{result}')



