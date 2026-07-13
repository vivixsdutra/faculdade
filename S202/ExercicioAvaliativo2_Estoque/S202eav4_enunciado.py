   ###                           ##              ####
  ####                          ###              ####
  ###  ##########   ######## ########  #######   ####
 ####  ##### ####  ####  ####  ###   ####  #### #### 
 ####  ###   ####   ########  ####  ########### #### 
####  ####   #### ####  ####  ####  ####        ###  
####  ###    ### ########### ###### ########## ####                 S202 - Banco de dados II
#### ####   ####  ##########  ####   ######    ###       Prof. Dr. Jonas Lopes de Vilas Boas

# Exercício Avaliativo 4 - Banco de dados orientado à colunas e Cassandra

"""
Estoque da Montadora 

Um fabricante de automóveis contratou você para desenvolver um sistema de banco de dados distribuído usando o Cassandra para as linhas de montagem de toda a corporação, onde cada máquina pudesse acessar a base de dados e buscar as peças de maneira correta para ser montada nos respectivos modelos de veículos. Para isso, você deverá criar a tabela estoque no sistema DataStax ASTRA e inserir as colunas usando o arquivo auxiliar disponibilizado junto com essa atividade. 

Questão 1: Siga os itens listados abaixo: 

Faça a inserção de uma nova peça com os dados abaixo: 

id: 5 
nome: Pistao 
carro: Mustang 
estante: 4 
nível: 1 
quantidade: 167 

Faça a inserção de uma nova peça com os dados abaixo: 

id: 4
nome: Suspencao 
carro: Argo 
estante: 1 
nível: 1 
quantidade: 3500 

Questão 2: Escreva o comando CQL utilizado para cada item abaixo: 

Faça uma busca no banco de dados que retorno todos os dados do item com nome 'Pistão';
Faça uma busca no banco que calcule a média aritmética da quantidade de todas as colunas armazenadas na tabela;
Faça uma busca que retorne quantas colunas tem armazenadas na tabela;
Busque a maior e a menor quantidade de peças usando as alias "maior quantidade" e "menor quantidade" para a tabela estoque. 
Faça uma busca que retorne os atributos nome, carro e quantidade, onde a estante seja igual a 3;
Faça uma busca que retorne a média aritmética da quantidade onde o nível seja igual a 1; 
Faça uma busca retornando todos os atributos onde a estante seja menor do que 3 e o nível seja maior do que 4.
 

Questão 3: Elabore um script Python que seja capaz de fazer uma consulta mostrando nome, estante e quantidade do carro fornecido pelo usuário. 

"""
import json
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

class CassandraConnector:
    
    def get_cassandra_connector(self):
        if not hasattr(self, 'cassandra_session'):
            self.cassandra_session = None

        if self.cassandra_session is None:
            cloud_config = {
                'secure_connect_bundle': 'secure-connect-dbiot.zip'
            }

            with open("dbiot-token.json") as f:
                secrets = json.load(f)

            CLIENT_ID = secrets["clientId"]
            CLIENT_SECRET = secrets["secret"]

            auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

            self.cassandra_session = cluster.connect()
            self.cassandra_session.row_factory = dict_factory

            self.cassandra_session.set_keyspace("ksiot")
        
        return self.cassandra_session

    
class AutoPart:
    def __init__(self, name, car, shelf, level, amount):
      self.name = name
      self.car = car
      self.shelf = shelf
      self.level = level
      self.amount = amount

    def to_dict(self):
      return {
          "name": self.name,
          "car": self.car,
          "shelf": self.shelf,
          "level": self.level,
          "amount": self.amount
	}


class AutoPartDAO:
    def __init__(self):
        connector = CassandraConnector()  
        self.cassandra_session = connector.get_cassandra_connector()  
        
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS estoque (
            id int PRIMARY KEY,
            name text,
            car text,
            shelf int,
            level int,
            amount int
        )
        """
        self.cassandra_session.execute(query)

    def add_part(self, part):
        query = """
        
        INSERT INTO estoque (id, name, car, shelf, level, amount)
        VALUES (%s, %s, %s, %s, %s, %s);

        """
        self.cassandra_session.execute(query, (part.id, part.name, part.car, part.shelf, part.level, part.amount))

    def get_part(self, name):
        query = "SELECT * FROM estoque WHERE name=%s"
        result = self.cassandra_session.execute(query, (name,))
        return list(result)

    def get_average_amount(self):
        query = "SELECT AVG(amount) AS average_amount FROM estoque"
        result = self.cassandra_session.execute(query)
        return result.one()["average_amount"]

    def get_total_amount(self):
        query = "SELECT COUNT(*) AS total_parts FROM estoque"
        result = self.cassandra_session.execute(query)
        return result.one()["total_parts"]

    def get_max_min(self):
        query = """
        SELECT MAX(amount) AS max_amount, MIN(amount) AS min_amount
        FROM estoque
        """
        result = self.cassandra_session.execute(query)
        return result.one()

    def get_parts_from_shelf(self, shelf):
        query = "SELECT name, car, amount FROM estoque WHERE shelf=%s"
        result = self.cassandra_session.execute(query, (shelf,))
        return list(result)

    def get_average_amount_from_level(self, level):
        query = "SELECT AVG(amount) AS average_amount FROM estoque WHERE level=%s"
        result = self.cassandra_session.execute(query, (level,))
        return result.one()["average_amount"]

    def get_parts_from_shelf_and_level(self, shelf, level):
        query = "SELECT * FROM estoque WHERE shelf<%s AND level>%s"
        result = self.cassandra_session.execute(query, (shelf, level))
        return list(result)

    def get_parts_of_car(self, car):
        query = "SELECT name, shelf, amount FROM estoque WHERE car=%s"
        result = self.cassandra_session.execute(query, (car,))
        return list(result)


if __name__ == '__main__':
    dao = AutoPartDAO()
    dao.create_table()

   
    dao.add_part(AutoPart(5, 'Pistao', 'Mustang', 4, 1, 167))
    dao.add_part(AutoPart(4, 'Suspencao', 'Argo', 1, 1, 3500))

    
    print("Dados da peça 'Pistao':", dao.get_part('Pistao'))
    print("Média aritmética da quantidade de todas as peças:", dao.get_average_amount())
    print("Total de colunas armazenadas na tabela:", dao.get_total_amount())
    print("Maior e menor quantidade de peças:", dao.get_max_min())
    print("Peças na estante 3:", dao.get_parts_from_shelf(3))
    print("Média aritmética da quantidade para nível 1:", dao.get_average_amount_from_level(1))
    print("Peças com estante < 3 e nível > 4:", dao.get_parts_from_shelf_and_level(3, 4))

  
    car = input("Digite o nome do carro para buscar as peças: ")
    print("Peças do carro", car, ":", dao.get_parts_of_car(car))
