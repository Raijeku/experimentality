"""Module that stores all the methods used in the API.

This module works as the controller of the API and connects to the database.
"""

import io
import sqlite3
import json
from typing import List
from PIL import Image

from ..models.product import Product
from ..models.image import ProductImage

def db_connection() -> sqlite3.Connection:
    """Connects to the database or creates it."""
    conn = None
    try:
        conn = sqlite3.connect('products/products.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

def downscale_image(image_path: str) -> bytes:
    image = Image.open(image_path)
    scale = 1
    size = image.size
    if size[1] >= size[0] and size[1] > 1024:
        scale = 1024/size[1]
    if size[0] >= size[1] and size[0] > 1024:
        scale = 1024/size[0]
    image = image.resize((int(size[0]*scale),int(size[1]*scale)),Image.ANTIALIAS)
    stream = io.BytesIO()
    image.save(stream, format="JPEG", optimize=True, quality=95)
    img_bytes = stream.getvalue()
    return img_bytes


def post_products(name: str, description: str, price: float, discount: float, images: List[str], country: str, searches: int) -> str:
    valid = True
    if (country == 'Colombia' or country == 'Mexico') and float(discount) > 0.5:
        valid = False
    if (country == 'Chile' or country == 'Peru') and float(discount) >= 0.3:
        valid = False
    if valid:
        conn = db_connection()
        cursor = conn.cursor()

        sql = """INSERT INTO Product (name, description, price, discount, country, searches)
                VALUES (?, ?, ?, ?, ?, ?)"""
        cursor = conn.execute(sql, (name, description, price, discount, country, searches))
        conn.commit()

        product_id = cursor.lastrowid

        images = [downscale_image(image) for image in images]

        sql = """INSERT INTO Image (product_id, data)
                VALUES (?, ?)"""
        for image in images:
            cursor = conn.execute(sql, (product_id, image))
            conn.commit()

        return 'Producto con identificación {0} fue creado.\n Última imágen con identificación {1} fue creada.'.format(product_id, cursor.lastrowid)
    else:
        return 'Descuento no adecuado.'

def get_products() -> str:
    conn = db_connection()
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM Product")
    elems = cursor.fetchall()

    products = [Product(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6]) for elem in elems]
    return json.dumps([product.__dict__ for product in products])

def get_images() -> str:
    conn = db_connection()
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM Image")
    images = cursor.fetchall()

    images = [ProductImage(image[0], image[1], image[2].decode("utf-8", "ignore")) for image in images]
    return json.dumps([image.__dict__ for image in images])

def get_most_searched(amount: int) -> str:
    conn = db_connection()
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM Product")
    elems = cursor.fetchall()
    products = [Product(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6]) for elem in elems]
    sorted_products = sorted(products, key=lambda x: x.searches, reverse=True)
    if amount > 1: sorted_products = sorted_products[:amount]
    products_dict = [product.__dict__ for product in sorted_products]
    
    sql = "SELECT * FROM Image where product_id in ({0})".format(','.join(['?']*amount))
    cursor.execute(sql, [product_dict['id'] for product_dict in products_dict])
    images = cursor.fetchall()

    images = [ProductImage(image[0], image[1], image[2].decode("utf-8", "ignore")) for image in images]
    images_dict = [image.__dict__ for image in images]

    for product_dict in products_dict:
        product_dict['images'] = []
        del product_dict['country']
        del product_dict['searches']
        for image_dict in images_dict:
            if product_dict['id'] == image_dict['product_id'] and len(product_dict['images']) <= 2: product_dict['images'].append(image_dict)

    return json.dumps(products_dict)

