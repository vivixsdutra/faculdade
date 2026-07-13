
from db import get_db
from bson.objectid import ObjectId

class Event:
    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description

    @staticmethod
    def create_event(name, date, description):
        db = get_db()
        event = {
            "name": name,
            "date": date,
            "description": description
        }
        db.events.insert_one(event)

    @staticmethod
    def read_events():
        db = get_db()
        return list(db.events.find())

    @staticmethod
    def update_event(event_id, update_fields):
        db = get_db()
        db.events.update_one({"_id": ObjectId(event_id)}, {"$set": update_fields})

    @staticmethod
    def delete_event(event_id):
        db = get_db()
        db.events.delete_one({"_id": ObjectId(event_id)})