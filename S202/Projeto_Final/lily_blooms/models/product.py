
from db import get_db
from bson.objectid import ObjectId
    
class Product:
        def __init__(self, name, description, price, stock):
            self.name = name
            self.description = description
            self.price = price
            self.stock = stock
    
        @staticmethod
        def create_product(name, description, price, stock):
            db = get_db()
            product = {
                "name": name,
                "description": description,
                "price": price,
                "stock": stock
            }
            db.products.insert_one(product)
    
        @staticmethod
        def read_products():
            db = get_db()
            return list(db.products.find())
    
        @staticmethod
        def update_product(product_id, update_fields):
            db = get_db()
            db.products.update_one({"_id": ObjectId(product_id)}, {"$set": update_fields})
    
        @staticmethod
        def delete_product(product_id):
            db = get_db()
            db.products.delete_one({"_id": ObjectId(product_id)})