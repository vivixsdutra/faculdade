
from db import get_db
from bson.objectid import ObjectId

class Order:
    def __init__(self, product_id, quantity, status):
        self.product_id = product_id
        self.quantity = quantity
        self.status = status

    @staticmethod
    def create_order(product_id, quantity, status):
        db = get_db()
        order = {
            "product_id": ObjectId(product_id),
            "quantity": quantity,
            "status": status
        }
        db.orders.insert_one(order)

    @staticmethod
    def read_orders():
        db = get_db()
        return list(db.orders.find())

    @staticmethod
    def update_order(order_id, update_fields):
        db = get_db()
        db.orders.update_one({"_id": ObjectId(order_id)}, {"$set": update_fields})

    @staticmethod
    def delete_order(order_id):
        db = get_db()
        db.orders.delete_one({"_id": ObjectId(order_id)})