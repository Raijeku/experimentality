import unittest
#from ..products.models.product import Product
from products.resources import methods

class TestProduct(unittest.TestCase):
    #def setUp(self):
    #    self.product = Product(1000, 'Computer', 'Cool computer', 1000, 0.1, "G:\Images June 17\IMG_20200203_172021 (2).jpg", 'Colombia', 15)
    
    def test_get_products(self):
        assert methods.get_products() == """"[
    {
        "id": 1,
        "name": "Shirt",
        "description": "Gray",
        "price": 10.0,
        "discount": 0.4,
        "country": "Colombia",
        "searches": 9
    },
    {
        "id": 2,
        "name": "Jacket",
        "description": "Black",
        "price": 10.0,
        "discount": 0.4,
        "country": "Colombia",
        "searches": 20
    },
    {
        "id": 3,
        "name": "Jeans",
        "description": "Blue",
        "price": 40.0,
        "discount": 0.4,
        "country": "Mexico",
        "searches": 40
    }
]"""

    def test_get_products_len(self):
        assert len(methods.get_products()) != 0

    def test_get_images_len(self):
        assert len(methods.get_products()) != 0

    def test_get_most_searched_len(self):
        assert len(methods.get_most_searched(2)) != 0