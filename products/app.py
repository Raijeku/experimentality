from distutils.log import debug
from flask import Flask, request
from models.product import Product
from resources import methods

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the products API.'

@app.route('/products', methods=['POST','GET'])
def products():
    if request.method == 'GET':
        return methods.get_products()

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        discount = request.form['discount']
        images = request.form['images']
        country = request.form['country']
        searches = request.form['searches']

        return methods.post_products(name, description, price, discount, images, country, searches)

@app.route('/most_searched/<amount>')
def most_searched(amount):
    return methods.get_most_searched(int(amount))

if __name__ == '__main__':
    app.run(debug=True)