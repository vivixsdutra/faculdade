def create_livros_collection(db):
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

    db.create_collection("Livros", validator={"$jsonSchema": schema})
