import json

class Product:
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