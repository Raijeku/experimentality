import json

class Product:
    def __init__(self, name, description, price, discount, images, country, searches):
        self.name = name
        self.description = description
        self.price = price
        self.discount = discount
        self.images = images
        self.country = country
        self.searches = searches

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)