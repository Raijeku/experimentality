import unittest
from ..products.models.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product('Computer', 'Cool computer', 1000, 0.1, None, 'COL')