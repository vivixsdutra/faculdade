import mysql.connector
from mysql.connector import Error
from datetime import date
from neides.models import Item, Sale

def conectar():
    """Estabelece a conexão com o banco de dados"""
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="trabalhojonas"
        )
        if conexao.is_connected():
            print("Conexão estabelecida com sucesso!")
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def criar_tabelas():
    """Cria todas as tabelas necessárias no banco de dados"""
    try:
        conexao = conectar()
        if conexao is None:
            return

        cursor = conexao.cursor()

        # Tabela Item
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Item (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            categoria VARCHAR(50),
            preco DECIMAL(10, 2),
            quantidade INT,
            desconto FLOAT DEFAULT 0.0
        );
        """)

        # Tabela Venda
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Venda (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data DATE NOT NULL,
            total DECIMAL(10, 2) NOT NULL
        );
        """)

        # Tabela Venda_Item
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Venda_Item (
            id INT AUTO_INCREMENT PRIMARY KEY,
            venda_id INT,
            item_id INT,
            quantidade INT,
            preco_unitario DECIMAL(10, 2),
            FOREIGN KEY (venda_id) REFERENCES Venda(id),
            FOREIGN KEY (item_id) REFERENCES Item(id)
        );
        """)

        print("Tabelas criadas com sucesso!")
        cursor.close()
        conexao.close()
    except Error as e:
        print(f"Erro ao criar tabelas: {e}")


def adicionar_item(name, price, stock, category):
    item = Item(name=name, price=price, stock=stock, category=category)
    item.save()
    print(f'Item {name} adicionado com sucesso.')

def listar_itens():
    items = Item.objects.all()
    for item in items:
        print(f'ID: {item.id}, Nome: {item.name}, Preço: {item.price}, Estoque: {item.stock}, Categoria: {item.category}')

def atualizar_estoque(item_id, nova_quantidade):
    try:
        item = Item.objects.get(id=item_id)
        item.stock = nova_quantidade
        item.save()
        print(f'Estoque do item {item.name} atualizado para {nova_quantidade}.')
    except Item.DoesNotExist:
        print('Item não encontrado.')

def remover_item(item_id):
    try:
        item = Item.objects.get(id=item_id)
        item.delete()
        print(f'Item {item.name} removido com sucesso.')
    except Item.DoesNotExist:
        print('Item não encontrado.')

def registrar_venda(itens_vendidos):
    for item_id, quantidade in itens_vendidos:
        try:
            item = Item.objects.get(id=item_id)
            sale = Sale(item=item, quantity=quantidade)
            sale.save()
            item.stock -= quantidade
            item.save()
            print(f'Venda registrada: {quantidade} x {item.name}')
        except Item.DoesNotExist:
            print(f'Item com ID {item_id} não encontrado.')

def gerar_relatorio_vendas():
    sales = Sale.objects.all()
    for sale in sales:
        print(f'Data: {sale.date}, Item: {sale.item.name}, Quantidade: {sale.quantity}')

def aplicar_desconto(item_id, desconto_percentual=None, desconto_valor_fixo=None):
    try:
        item = Item.objects.get(id=item_id)
        if desconto_percentual:
            item.price = item.price * (1 - desconto_percentual / 100)
        elif desconto_valor_fixo:
            item.price = max(0, item.price - desconto_valor_fixo)
        item.save()
        print(f'Desconto aplicado ao item {item.name}. Novo preço: {item.price}')
    except Item.DoesNotExist:
        print('Item não encontrado.')
        
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Listar itens")
        print("3. Atualizar estoque")
        print("4. Remover item")
        print("5. Registrar venda")
        print("6. Gerar relatório de vendas")
        print("7. Aplicar desconto")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            name = input("Nome do item: ")
            price = float(input("Preço do item: "))
            stock = int(input("Estoque do item: "))
            category = input("Categoria do item (salgado, doce, bebida): ")
            adicionar_item(name, price, stock, category)
        elif opcao == "2":
            listar_itens()
        elif opcao == "3":
            item_id = int(input("ID do item: "))
            nova_quantidade = int(input("Nova quantidade: "))
            atualizar_estoque(item_id, nova_quantidade)
        elif opcao == "4":
            item_id = int(input("ID do item: "))
            remover_item(item_id)
        elif opcao == "5":
            itens_vendidos = []
            while True:
                item_id = int(input("ID do item vendido (0 para sair): "))
                if item_id == 0:
                    break
                quantidade = int(input(f"Quantidade vendida do item {item_id}: "))
                itens_vendidos.append((item_id, quantidade))
            registrar_venda(itens_vendidos)
        elif opcao == "6":
            gerar_relatorio_vendas()
        elif opcao == "7":
            item_id = int(input("ID do item: "))
            print("1. Desconto percentual")
            print("2. Desconto fixo")
            tipo_desconto = input("Escolha o tipo de desconto: ")
            if tipo_desconto == "1":
                desconto_percentual = float(input("Percentual de desconto: "))
                aplicar_desconto(item_id, desconto_percentual=desconto_percentual)
            elif tipo_desconto == "2":
                desconto_valor_fixo = float(input("Valor fixo de desconto: "))
                aplicar_desconto(item_id, desconto_valor_fixo=desconto_valor_fixo)
            else:
                print("Tipo de desconto inválido.")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Executa o menu
if __name__ == "__main__":
    import django
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_neides.settings')
    django.setup()
    menu()        