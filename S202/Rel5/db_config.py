from pymongo import MongoClient

def get_db():
    # Conectar ao MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    return client['biblioteca']
