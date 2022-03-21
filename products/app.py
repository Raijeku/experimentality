"""Flask application module.

This module holds the required code to initialize the Flask app and includes the routes for accessing the API.
"""

from distutils.log import debug
from flask import Flask, request
from .models.product import Product
from .resources import methods

app = Flask(__name__)

@app.route('/')
def index():
    """Home route for the Flask app. The browser first opens this route."""
    return 'This is the products API.'

@app.route('/products', methods=['POST','GET'])
def products():
    """Route to retrieve all the products when using the GET method and to add a product when using the POST method."""
    if request.method == 'GET':
        return methods.get_products()

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        discount = request.form['discount']
        images = request.form.getlist('images')
        country = request.form['country']
        searches = request.form['searches']

        return methods.post_products(name, description, price, discount, images, country, searches)

@app.route('/images', methods=['GET'])
def images():
    """Route to retrieve all the product images using the GET method."""
    return methods.get_images()

@app.route('/most_searched/<int:amount>')
def most_searched(amount):
    """Route to retrieve the most searched products up to a number specified by the amount parameter.
    
    Args:
        amount: The number of products to be returned as the most search products.
    """
    return methods.get_most_searched(int(amount))

if __name__ == '__main__':
    app.run(debug=True)