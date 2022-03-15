import sqlite3

conn = sqlite3.connect("products.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE Product (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    description text NOT NULL,
    price float NOT NULL,
    discount float NOT NULL,
    images text NOT NULL,
    country text NOT NULL,
    searches integer NOT NULL
)"""
cursor.execute(sql_query)