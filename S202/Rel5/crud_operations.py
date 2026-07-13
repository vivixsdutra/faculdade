def inserir_livro(db):
    _id = int(input("ID: "))
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    preco = float(input("Preço: "))

    livro = {"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco}
    db.Livros.insert_one(livro)
    print("Livro inserido com sucesso!")

def exibir_livros(db):
    livros = db.Livros.find()
    for livro in livros:
        print(livro)

def atualizar_livro(db):
    _id = int(input("ID do livro a ser atualizado: "))
    campo = input("Campo a ser atualizado (titulo, autor, ano, preco): ")
    valor = input(f"Novo valor para {campo}: ")

    if campo == "ano" or campo == "_id":
        valor = int(valor)
    elif campo == "preco":
        valor = float(valor)

    db.Livros.update_one({"_id": _id}, {"$set": {campo: valor}})
    print("Livro atualizado com sucesso!")

def remover_livro(db):
    _id = int(input("ID do livro a ser removido: "))
    db.Livros.delete_one({"_id": _id})
    print("Livro removido com sucesso!")
