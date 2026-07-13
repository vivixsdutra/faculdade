
from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['lily_blooms']
    return db

def initialize_db():
    db = get_db()
    if db.products.count_documents({}) == 0:  # Verifica se a coleção está vazia
        products = [
            {"name": "Rosas Vermelhas", "description": "Buquê de rosas vermelhas", "price": 50.0, "stock": 10},
            {"name": "Lírios Brancos", "description": "Buquê de lírios brancos", "price": 60.0, "stock": 15},
            {"name": "Tulipas Amarelas", "description": "Buquê de tulipas amarelas", "price": 70.0, "stock": 20},
            {"name": "Orquídeas Roxas", "description": "Buquê de orquídeas roxas", "price": 80.0, "stock": 5},
            {"name": "Girassóis", "description": "Buquê de girassóis", "price": 55.0, "stock": 12},
            {"name": "Margaridas", "description": "Buquê de margaridas", "price": 45.0, "stock": 18},
            {"name": "Cravos", "description": "Buquê de cravos", "price": 50.0, "stock": 10},
            {"name": "Hortênsias", "description": "Buquê de hortênsias", "price": 65.0, "stock": 8},
            {"name": "Peônias", "description": "Buquê de peônias", "price": 75.0, "stock": 7},
            {"name": "Lavandas", "description": "Buquê de lavandas", "price": 40.0, "stock": 20},
            {"name": "Amor-perfeito", "description": "Buquê de amor-perfeito", "price": 35.0, "stock": 25},
            {"name": "Camélias", "description": "Buquê de camélias", "price": 60.0, "stock": 10},
            {"name": "Dálias", "description": "Buquê de dálias", "price": 55.0, "stock": 15},
            {"name": "Jasmim", "description": "Buquê de jasmim", "price": 50.0, "stock": 12},
            {"name": "Magnólias", "description": "Buquê de magnólias", "price": 70.0, "stock": 6},
            {"name": "Narcisos", "description": "Buquê de narcisos", "price": 45.0, "stock": 18},
            {"name": "Petúnias", "description": "Buquê de petúnias", "price": 50.0, "stock": 10},
            {"name": "Violetas", "description": "Buquê de violetas", "price": 35.0, "stock": 20},
            {"name": "Zínias", "description": "Buquê de zínias", "price": 40.0, "stock": 15},
            {"name": "Begônias", "description": "Buquê de begônias", "price": 55.0, "stock": 10}
        ]
        db.products.insert_many(products)

    if db.services.count_documents({}) == 0:  # Verifica se a coleção está vazia
        services = [
            {"name": "Decoração de Casamento", "description": "Serviço completo de decoração para casamentos", "price": 5000.0},
            {"name": "Decoração de Festa de Aniversário", "description": "Serviço completo de decoração para festas de aniversário", "price": 3000.0},
            {"name": "Decoração de Evento Corporativo", "description": "Serviço completo de decoração para eventos corporativos", "price": 4000.0},
            {"name": "Decoração de Chá de Bebê", "description": "Serviço completo de decoração para chá de bebê", "price": 2500.0},
            {"name": "Decoração de Formatura", "description": "Serviço completo de decoração para formaturas", "price": 3500.0}
        ]
        db.services.insert_many(services)