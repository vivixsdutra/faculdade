# setup_db.py

from pymongo import MongoClient

def setup_database():
    # Conectando ao MongoDB
    client = MongoClient('localhost', 27017)

    # Criando o banco de dados 'bancoiot'
    db = client['bancoiot']

    # Criando a coleção 'sensores'
    collection = db['sensores']

    # Criando documentos para os sensores
    sensores = [
        {"nomeSensor": "Temp1", "valorSensor": 30, "unidadeMedida": "C°", "sensorAlarmado": False},
        {"nomeSensor": "Temp2", "valorSensor": 35, "unidadeMedida": "C°", "sensorAlarmado": False},
        {"nomeSensor": "Temp2", "valorSensor": 38.5, "unidadeMedida": "C°", "sensorAlarmado": False},
        {"nomeSensor": "Temp3", "valorSensor": 40, "unidadeMedida": "C°", "sensorAlarmado": False}
    ]

    # Inserindo os documentos na coleção
    collection.insert_many(sensores)
    print("Banco de dados, colecao e sensores criados com sucesso!")

if __name__ == "__main__":
    setup_database()
