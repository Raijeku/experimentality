"""Module that stores the ProductImage class."""

import json

class ProductImage:
    """Class that represents the product images and that is used as a model to persist images.
    
    Args:
        id: Identification for the product image.
        product_id: Identification of the product the image is tied to.
        data: The image content.
    """
    def __init__(self, id, product_id, data):
        self.id = id
        self.product_id = product_id
        self.data = data

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)