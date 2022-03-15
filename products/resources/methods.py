import sqlite3
import json

from models.product import Product

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('products.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

def post_products(name, description, price, discount, images, country, searches):
    valid = True
    if (country == 'Colombia' or country == 'Mexico') and discount > 0.5:
        valid = False
    if (country == 'Chile' or country == 'Peru') and discount >= 0.3:
        valid = False
    if valid:
        conn = db_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO Product (name, description, price, discount, images, country, searches)
                VALUES (?, ?, ?, ?, ?, ?, ?)"""
        cursor = conn.execute(sql, (name, description, price, discount, images, country, searches))
        conn.commit()

        return 'Producto con identificación {0} fue creado.'.format(cursor.lastrowid)
    else:
        return 'Descuento no adecuado.'

def get_products():
    conn = db_connection()
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM Product")
    elems = cursor.fetchall()
    products = [Product(elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7]) for elem in elems]
    return json.dumps([product.__dict__ for product in products])

def get_most_searched(amount):
    conn = db_connection()
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM Product")
    elems = cursor.fetchall()
    products = [Product(elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7]) for elem in elems]
    sorted_products = sorted(products, key=lambda x: x.searches, reverse=True)
    if amount > 1: sorted_products = sorted_products[:amount]
    return json.dumps([product.__dict__ for product in sorted_products])

