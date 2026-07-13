class MotoristaCLI:
    def __init__(self, motorista_dao):
        self.motorista_dao = motorista_dao

    def menu(self):
        while True:
            print("\n--- Menu Motorista ---")
            print("1. Criar motorista")
            print("2. Ler motorista")
            print("3. Atualizar motorista")
            print("4. Deletar motorista")
            print("5. Exibir ranking de motoristas por pontuação")
            print("6. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.create_motorista()
            elif escolha == '2':
                self.read_motorista()
            elif escolha == '3':
                self.update_motorista()
            elif escolha == '4':
                self.delete_motorista()
            elif escolha == '5':
                self.exibir_ranking_motoristas()
            elif escolha == '6':
                break
            else:
                print("Opção inválida, tente novamente.")

    
    def exibir_ranking_motoristas(self):
        motoristas = self.motorista_dao.listar_todos_motoristas()

        
        ranking = []
        for motorista in motoristas:
            total_nota = 0
            total_corridas = len(motorista['corridas'])

            if total_corridas > 0:
                for corrida in motorista['corridas']:
                    total_nota += corrida['nota']
                media_nota = total_nota / total_corridas
                ranking.append((motorista['nome'], media_nota))

        
        ranking.sort(key=lambda x: x[1], reverse=True)

        
        print("\n--- Ranking de Motoristas ---")
        for i, (nome, media_nota) in enumerate(ranking, 1):
            print(f"{i}. {nome} - Média de notas: {media_nota:.2f}")

    def create_motorista(self):
        nome = input("Digite o nome do motorista: ")
        cnh = input("Digite a CNH do motorista: ")
        corridas = []
        while True:
            corrida = input("Deseja adicionar uma corrida? (s/n): ")
            if corrida.lower() == 's':
                nota = float(input("Nota da corrida: "))
                distancia = float(input("Distância percorrida (km): "))
                valor = float(input("Valor da corrida: "))
                nome_passageiro = input("Nome do passageiro: ")
                documento_passageiro = input("Documento do passageiro: ")
                passageiro = {"nome": nome_passageiro, "documento": documento_passageiro}
                corridas.append({"nota": nota, "distancia": distancia, "valor": valor, "passageiro": passageiro})
            else:
                break
        self.motorista_dao.criar_motorista(nome, cnh, corridas)

    def read_motorista(self):
        id_motorista = input("Digite o ID do motorista: ")
        motorista = self.motorista_dao.ler_motorista_por_id(id_motorista)
        if motorista:
            print(f"Motorista encontrado: {motorista}")
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        id_motorista = input("Digite o ID do motorista: ")
        nome = input("Novo nome do motorista (deixe em branco para não alterar): ")
        cnh = input("Nova CNH do motorista (deixe em branco para não alterar): ")
        self.motorista_dao.atualizar_motorista(id_motorista, nome, cnh)

    def delete_motorista(self):
        id_motorista = input("Digite o ID do motorista: ")
        self.motorista_dao.deletar_motorista(id_motorista)
