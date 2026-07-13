from db_config import get_db
from livro_schema import create_livros_collection
from crud_operations import inserir_livro, exibir_livros, atualizar_livro, remover_livro

def menu():
    print("\nMenu CRUD Livros")
    print("1. Inserir Livro")
    print("2. Exibir Livros")
    print("3. Atualizar Livro")
    print("4. Remover Livro")
    print("5. Sair")

def crud():
    db = get_db()

    # Cria a collection com validação (apenas uma vez)
    try:
        create_livros_collection(db)
    except Exception as e:
        print("Collection já existe ou erro ao criar:", e)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_livro(db)
        elif opcao == "2":
            exibir_livros(db)
        elif opcao == "3":
            atualizar_livro(db)
        elif opcao == "4":
            remover_livro(db)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Executa o CRUD
crud()
