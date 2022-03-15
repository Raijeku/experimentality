import sqlite3

conn = sqlite3.connect("products/products.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE Product (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    description text NOT NULL,
    price float NOT NULL,
    discount float NOT NULL,
    country text NOT NULL,
    searches integer NOT NULL
)"""
cursor.execute(sql_query)

sql_query = """ CREATE TABLE Image (
    id integer PRIMARY KEY AUTOINCREMENT,
    product_id integer NOT NULL,
    data blob NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Product (id)
)"""
cursor.execute(sql_query)