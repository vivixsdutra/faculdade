
# lily_blooms.py
from models.product import Product
from models.order import Order
from models.event import Event
from models.purchase import Purchase
from db import initialize_db, get_db
from datetime import datetime

def show_menu():
    print("1. Comprar buquês e arranjos")
    print("2. Solicitar serviços de decoração")
    print("3. Gerenciar pedidos")
    print("4. Acessar histórico de compras")
    print("5. Cadastrar novo produto")
    print("6. Cadastrar novo serviço de decoração")
    print("7. Sair")

def handle_product_menu():
    while True:
        print("\n1. Listar Produtos")
        print("2. Voltar")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            products = Product.read_products()
            for product in products:
                print(f"ID: {product['_id']}")
                print(f"Nome: {product['name']}")
                print(f"Descrição: {product['description']}")
                print(f"Preço: {product['price']}")
                print(f"Estoque: {product['stock']}")
                print("-" * 20)
        elif choice == '2':
            break
        else:
            print("Opção inválida. Tente novamente.")

def handle_service_menu():
    db = get_db()
    while True:
        print("\n1. Listar Serviços de Decoração")
        print("2. Voltar")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            services = db.services.find()
            for service in services:
                print(f"ID: {service['_id']}")
                print(f"Nome: {service['name']}")
                print(f"Descrição: {service['description']}")
                print(f"Preço: {service['price']}")
                print("-" * 20)
        elif choice == '2':
            break
        else:
            print("Opção inválida. Tente novamente.")

def handle_order_menu():
    while True:
        print("\n1. Adicionar Pedido")
        print("2. Listar Pedidos")
        print("3. Atualizar Pedido")
        print("4. Remover Pedido")
        print("5. Voltar")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            product_id = input("ID do Produto: ")
            quantity = int(input("Quantidade: "))
            status = input("Status: ")
            Order.create_order(product_id, quantity, status)
        elif choice == '2':
            orders = Order.read_orders()
            for order in orders:
                print(order)
        elif choice == '3':
            order_id = input("ID do Pedido: ")
            update_fields = {}
            product_id = input("Novo ID do Produto (deixe em branco para não alterar): ")
            if product_id:
                update_fields["product_id"] = product_id
            quantity = input("Nova Quantidade (deixe em branco para não alterar): ")
            if quantity:
                update_fields["quantity"] = int(quantity)
            status = input("Novo Status (deixe em branco para não alterar): ")
            if status:
                update_fields["status"] = status
            Order.update_order(order_id, update_fields)
        elif choice == '4':
            order_id = input("ID do Pedido: ")
            Order.delete_order(order_id)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def handle_event_menu():
    while True:
        print("\n1. Adicionar Evento")
        print("2. Listar Eventos")
        print("3. Atualizar Evento")
        print("4. Remover Evento")
        print("5. Voltar")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            name = input("Nome do Evento: ")
            date = input("Data: ")
            description = input("Descrição: ")
            Event.create_event(name, date, description)
        elif choice == '2':
            events = Event.read_events()
            for event in events:
                print(event)
        elif choice == '3':
            event_id = input("ID do Evento: ")
            update_fields = {}
            name = input("Novo Nome (deixe em branco para não alterar): ")
            if name:
                update_fields["name"] = name
            date = input("Nova Data (deixe em branco para não alterar): ")
            if date:
                update_fields["date"] = date
            description = input("Nova Descrição (deixe em branco para não alterar): ")
            if description:
                update_fields["description"] = description
            Event.update_event(event_id, update_fields)
        elif choice == '4':
            event_id = input("ID do Evento: ")
            Event.delete_event(event_id)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def handle_purchase_menu():
    while True:
        print("\n1. Listar Histórico de Compras")
        print("2. Voltar")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            purchases = Purchase.read_purchases()
            for purchase in purchases:
                print(purchase)
        elif choice == '2':
            break
        else:
            print("Opção inválida. Tente novamente.")

def handle_add_product():
    name = input("Nome do Produto: ")
    description = input("Descrição: ")
    price = float(input("Preço: "))
    stock = int(input("Estoque: "))
    Product.create_product(name, description, price, stock)
    print("Produto adicionado com sucesso!")

def handle_add_service():
    db = get_db()
    name = input("Nome do Serviço: ")
    description = input("Descrição: ")
    price = float(input("Preço: "))
    service = {"name": name, "description": description, "price": price}
    db.services.insert_one(service)
    print("Serviço adicionado com sucesso!")

def main():
    initialize_db()  # Inicializar o banco de dados com produtos e serviços padrão
    while True:
        show_menu()
        choice = input("Escolha uma opção: ")
        if choice == '1':
            handle_product_menu()
        elif choice == '2':
            handle_service_menu()
        elif choice == '3':
            handle_order_menu()
        elif choice == '4':
            handle_purchase_menu()
        elif choice == '5':
            handle_add_product()
        elif choice == '6':
            handle_add_service()
        elif choice == '7':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()