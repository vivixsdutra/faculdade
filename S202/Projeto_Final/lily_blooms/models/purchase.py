
from db import get_db
from bson.objectid import ObjectId

class Purchase:
    def __init__(self, product_id, quantity, total_price, date):
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
        self.date = date

    @staticmethod
    def create_purchase(product_id, quantity, total_price, date):
        db = get_db()
        purchase = {
            "product_id": ObjectId(product_id),
            "quantity": quantity,
            "total_price": total_price,
            "date": date
        }
        db.purchases.insert_one(purchase)

    @staticmethod
    def read_purchases():
        db = get_db()
        return list(db.purchases.find())