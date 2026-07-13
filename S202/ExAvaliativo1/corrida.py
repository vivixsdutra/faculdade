class Corrida:
    def __init__(self, nota: float, distancia: float, valor: float, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def __repr__(self):
        return (f"Corrida(nota={self.nota}, distancia={self.distancia} km, "
                f"valor={self.valor} R$, passageiro={self.passageiro})")


