from database.game_database import GameDatabase
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Obter dados do Neo4j do .env
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

def main():
    # Instanciar a classe GameDatabase
    db = GameDatabase(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

    # Exemplo de uso
    db.create_player("1", "Alice")
    db.create_player("2", "Bob")
    db.create_match("match1", "1", "2", "Alice wins")

    # Atualizar e recuperar informações
    db.update_match_result("match1", "Bob wins")
    print(db.get_player("1"))
    print(db.get_match("match1"))
    print(db.get_player_matches("1"))

    # Fechar a conexão
    db.close()

if __name__ == "__main__":
    main()
