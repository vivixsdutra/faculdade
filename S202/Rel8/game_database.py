from neo4j import GraphDatabase

class GameDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

# Método para criar um jogador
    def create_player(self, player_id, name):
        with self.driver.session() as session:
            session.run(
                "CREATE (p:Player {id: $player_id, name: $name})",
                player_id=player_id, name=name
            )

    # Método para atualizar informações de um jogador
    def update_player(self, player_id, name):
        with self.driver.session() as session:
            session.run(
                "MATCH (p:Player {id: $player_id}) "
                "SET p.name = $name",
                player_id=player_id, name=name
            )

    # Método para excluir um jogador
    def delete_player(self, player_id):
        with self.driver.session() as session:
            session.run(
                "MATCH (p:Player {id: $player_id}) "
                "DETACH DELETE p",
                player_id=player_id
            )

    # Método para criar uma partida entre jogadores
    def create_match(self, match_id, player1_id, player2_id, result):
        with self.driver.session() as session:
            session.run(
                "CREATE (m:Match {id: $match_id, result: $result}) "
                "WITH m "
                "MATCH (p1:Player {id: $player1_id}), (p2:Player {id: $player2_id}) "
                "MERGE (p1)-[:PARTICIPATED_IN]->(m) "
                "MERGE (p2)-[:PARTICIPATED_IN]->(m)",
                match_id=match_id, player1_id=player1_id, player2_id=player2_id, result=result
            )

    # Método para atualizar o resultado de uma partida
    def update_match_result(self, match_id, result):
        with self.driver.session() as session:
            session.run(
                "MATCH (m:Match {id: $match_id}) "
                "SET m.result = $result",
                match_id=match_id, result=result
            )

    # Método para excluir uma partida
    def delete_match(self, match_id):
        with self.driver.session() as session:
            session.run(
                "MATCH (m:Match {id: $match_id}) "
                "DETACH DELETE m",
                match_id=match_id
            )

    # Método para obter informações de um jogador
    def get_player(self, player_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Player {id: $player_id}) RETURN p",
                player_id=player_id
            )
            return result.single()

    # Método para obter informações de uma partida
    def get_match(self, match_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (m:Match {id: $match_id}) RETURN m",
                match_id=match_id
            )
            return result.single()

    # Método para obter histórico de partidas de um jogador
    def get_player_matches(self, player_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match) "
                "RETURN m",
                player_id=player_id
            )
            return [record["m"] for record in result]

# Exemplo de uso
db = GameDatabase("bolt://localhost:7687", "neo4j", "password")

# Criando jogadores
db.create_player("1", "Alice")
db.create_player("2", "Bob")

# Criando uma partida entre Alice e Bob
db.create_match("match1", "1", "2", "Alice wins")

# Atualizando o resultado da partida
db.update_match_result("match1", "Bob wins")

# Recuperando informações de um jogador
print(db.get_player("1"))

# Recuperando informações de uma partida
print(db.get_match("match1"))

# Recuperando o histórico de partidas de Alice
print(db.get_player_matches("1"))

# Fechando a conexão
db.close()