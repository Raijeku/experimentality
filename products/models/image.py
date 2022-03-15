import json

class Image:
    def __init__(self, product_id, data):
        self.product_id = product_id
        self.data = data

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)