"""Module that stores the Product class."""

import json

class Product:
    """Class that represents the products and that is used as a model to persist products.
    
    Args:
        id: Identification for the product.
        name: Name of the product.
        description: Description of the product.
        price: Normal price of the product.
        discount: Discount percentage of the product.
        country: Country where the product is available.
        searches: Number of searches made for that product.
    """
    def __init__(self, id, name, description, price, discount, country, searches):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.discount = discount
        self.country = country
        self.searches = searches

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)