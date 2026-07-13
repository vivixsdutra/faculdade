from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['biblioteca']

# Definir o schema de validação
schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id", "titulo", "autor", "ano", "preco"],
        "properties": {
            "_id": {
                "bsonType": "int",
                "description": "deve ser um número inteiro e é obrigatório"
            },
            "titulo": {
                "bsonType": "string",
                "description": "deve ser uma string e é obrigatório"
            },
            "autor": {
                "bsonType": "string",
                "description": "deve ser uma string e é obrigatório"
            },
            "ano": {
                "bsonType": "int",
                "description": "deve ser um número inteiro e é obrigatório"
            },
            "preco": {
                "bsonType": "double",
                "description": "deve ser um número e é obrigatório"
            }
        }
    }
}

# Criar a collection com validação
db.create_collection("Livros", validator={"$jsonSchema": schema})
