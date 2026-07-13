alunos = []
contadores_matricula = {}


def gerar_matricula(curso):
    curso = curso.upper()

    if curso not in contadores_matricula:
        contadores_matricula[curso] = 1
    else:
        contadores_matricula[curso] += 1

    return f"{curso}{contadores_matricula[curso]}"


def cadastrar_aluno():
    print("\n--- CADASTRAR ALUNO ---")
    nome = input("Digite o nome do aluno: ").strip()
    email = input("Digite o email do aluno: ").strip()
    curso = input("Digite o curso (GES, GEC, GET...): ").strip().upper()

    matricula = gerar_matricula(curso)

    aluno = {
        "nome": nome,
        "email": email,
        "curso": curso,
        "matricula": matricula
    }

    alunos.append(aluno)

    print(f"\nAluno cadastrado com sucesso! Matrícula: {matricula}")


def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(f"\nNome: {aluno['nome']}")
        print(f"Email: {aluno['email']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Matrícula: {aluno['matricula']}")


def buscar_aluno_por_matricula(matricula):
    for aluno in alunos:
        if aluno["matricula"] == matricula.upper():
            return aluno
    return None


def buscar_aluno():
    print("\n--- BUSCAR ALUNO ---")
    matricula = input("Digite a matrícula: ").strip().upper()

    aluno = buscar_aluno_por_matricula(matricula)

    if aluno:
        print("\nAluno encontrado:")
        print(f"Nome: {aluno['nome']}")
        print(f"Email: {aluno['email']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Matrícula: {aluno['matricula']}")
    else:
        print("Aluno não encontrado.")


def atualizar_aluno():
    print("\n--- ATUALIZAR ALUNO ---")
    matricula = input("Digite a matrícula: ").strip().upper()

    aluno = buscar_aluno_por_matricula(matricula)

    if not aluno:
        print("Aluno não encontrado.")
        return

    novo_nome = input(f"Novo nome ({aluno['nome']}): ").strip()
    novo_email = input(f"Novo email ({aluno['email']}): ").strip()
    novo_curso = input(f"Novo curso ({aluno['curso']}): ").strip().upper()

    if novo_nome:
        aluno["nome"] = novo_nome
    if novo_email:
        aluno["email"] = novo_email
    if novo_curso:
        aluno["curso"] = novo_curso

    print("Aluno atualizado com sucesso!")


def excluir_aluno():
    print("\n--- EXCLUIR ALUNO ---")
    matricula = input("Digite a matrícula: ").strip().upper()

    aluno = buscar_aluno_por_matricula(matricula)

    if not aluno:
        print("Aluno não encontrado.")
        return

    confirmacao = input(f"Tem certeza que deseja excluir {aluno['nome']}? (s/n): ").strip().lower()

    if confirmacao == "s":
        alunos.remove(aluno)
        print("Aluno excluído com sucesso!")
    else:
        print("Operação cancelada.")


def menu():
    while True:
        print("\n********** PRÁTICA 1 - CRUD EM PYTHON **********")
        print("\n====== MENU ======")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno por matrícula")
        print("4 - Atualizar aluno")
        print("5 - Excluir aluno")
        print("6 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            atualizar_aluno()
        elif opcao == "5":
            excluir_aluno()
        elif opcao == "6":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


menu()