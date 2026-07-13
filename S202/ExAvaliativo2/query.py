
from database import Database

class Queries:
    def __init__(self, db: Database):
        self.db = db

    def questao_1_1(self):
        query = """
        MATCH (t:Teacher{name: 'Renzo'})
        RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        return self.db.execute_query(query)

    def questao_1_2(self):
        query = """
        MATCH (t:Teacher)
        WHERE t.name STARTS WITH 'M'
        RETURN t.name AS name, t.cpf AS cpf
        """
        return self.db.execute_query(query)

    def questao_1_3(self):
        query = """
        MATCH (c:City)
        RETURN c.name AS city_name
        """
        return self.db.execute_query(query)

    def questao_1_4(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name AS school_name, s.address AS address, s.number AS number
        """
        return self.db.execute_query(query)



    def questao_2_1(self):
        query = """
        MATCH (t:Teacher)
        RETURN min(t.ano_nasc) AS mais_velho, max(t.ano_nasc) AS mais_jovem
        """
        return self.db.execute_query(query)

    def questao_2_2(self):
        query = """
        MATCH (c:City)
        RETURN avg(c.population) AS media_habitantes
        """
        return self.db.execute_query(query)

    def questao_2_3(self):
        query = """
        MATCH (c:City {cep: '37540-000'})
        RETURN replace(c.name, 'a', 'A') AS city_name
        """
        return self.db.execute_query(query)

    def questao_2_4(self):
        query = """
        MATCH (t:Teacher)
        RETURN substring(t.name, 2, 1) AS terceira_letra_nome
        """
        return self.db.execute_query(query)
