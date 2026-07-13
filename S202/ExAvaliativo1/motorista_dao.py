from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    # Método para criar um motorista 
    def criar_motorista(self, nome: str, cnh: str, corridas: list):
        try:
            motorista = {
                "nome": nome,
                "cnh": cnh,
                "corridas": corridas  
            }
            res = self.db.motoristas.insert_one(motorista)
            print(f"Motorista criado com ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    # Método para ler um motorista pelo ID
    def ler_motorista_por_id(self, id: str):
        try:
            motorista = self.db.motoristas.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {motorista}")
            return motorista
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o motorista: {e}")
            return None

    # Método para atualizar um motorista
    def atualizar_motorista(self, id: str, nome: str = None, cnh: str = None):
        try:
            update_fields = {}
            if nome:
                update_fields["nome"] = nome
            if cnh:
                update_fields["cnh"] = cnh

            res = self.db.motoristas.update_one(
                {"_id": ObjectId(id)}, {"$set": update_fields}
            )
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o motorista: {e}")
            return None

    # Método para deletar um motorista
    def deletar_motorista(self, id: str):
        try:
            res = self.db.motoristas.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista: {e}")
            return None
        

     #Método para listar os motoristas    
    def listar_todos_motoristas(self):
        try:
            motoristas = list(self.db.collection.find())
            return motoristas
        except Exception as e:
            print(f"Erro ao buscar motoristas: {e}")
            return []
