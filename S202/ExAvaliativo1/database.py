from typing import Collection
import pymongo # pip install pymongo
from dataset import dataset  

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://root:<password>@cluster0.ci2yf.mongodb.net/"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)


# Pré Inserção de motoristas para teste do banco.

    def resetDatabase(self):
        try:
            # Limpar a coleção atual
            self.db.drop_collection(self.collection.name)

            # Inserir os motoristas do dataset
            self.collection.insert_many(dataset)
        except Exception as e:
            print(e)
