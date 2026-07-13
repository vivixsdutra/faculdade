class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

    def __repr__(self):
        return f"Passageiro(nome={self.nome}, documento={self.documento})"

