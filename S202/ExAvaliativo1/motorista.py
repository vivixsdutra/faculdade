from corrida import Corrida 

class Motorista:
    def __init__(self, nome: str, cnh: str, corridas: list):
        self.nome = nome
        self.cnh = cnh
        self.corridas = corridas  

    def adicionar_corrida(self, corrida: Corrida):
        self.corridas.append(corrida)

    def __repr__(self):
        return f"Motorista(nome={self.nome}, cnh={self.cnh}, corridas={self.corridas})"
