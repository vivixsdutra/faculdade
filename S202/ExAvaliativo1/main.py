import random
from motorista_dao import MotoristaDAO
from database import Database
from passageiro import Passageiro
from corrida import Corrida
from motorista import Motorista
from writeAJson import writeAJson  
from motorista_cli import MotoristaCLI


def main():
    
    database_name = "exa1"  
    collection_name = "motorista"   
    db = Database(database_name, collection_name)
    
    # Resetar o banco de dados e inserir motoristas do dataset
    db.resetDatabase()

    # Criar a instância do MotoristaDAO
    motorista_dao = MotoristaDAO(db)
    
    # Iniciar a interface CLI com o MotoristaDAO
    cli = MotoristaCLI(motorista_dao)

    # Exibir o menu para o usuário
    cli.menu()

if __name__ == "__main__":
    main()
