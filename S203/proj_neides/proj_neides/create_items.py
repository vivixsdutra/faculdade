import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_neides.settings')
django.setup()

from neides.models import Item

# Criar itens de exemplo
items = [
    # Salgados
    {'name': 'Coxinha', 'price': 5.00, 'stock': 30, 'category': 'salgado'},
    {'name': 'Pastel', 'price': 4.00, 'stock': 25, 'category': 'salgado'},
    {'name': 'Empada', 'price': 6.00, 'stock': 20, 'category': 'salgado'},
    {'name': 'Esfiha', 'price': 3.50, 'stock': 40, 'category': 'salgado'},
    {'name': 'Quibe', 'price': 4.50, 'stock': 35, 'category': 'salgado'},
    # Doces
    {'name': 'Brigadeiro', 'price': 2.00, 'stock': 50, 'category': 'doce'},
    {'name': 'Beijinho', 'price': 2.00, 'stock': 50, 'category': 'doce'},
    {'name': 'Bolo de Cenoura', 'price': 3.00, 'stock': 20, 'category': 'doce'},
    {'name': 'Pudim', 'price': 4.00, 'stock': 15, 'category': 'doce'},
    {'name': 'Torta de Limão', 'price': 5.00, 'stock': 10, 'category': 'doce'},
    # Bebidas
    {'name': 'Refrigerante', 'price': 5.00, 'stock': 50, 'category': 'bebida'},
    {'name': 'Suco de Laranja', 'price': 4.00, 'stock': 30, 'category': 'bebida'},
    {'name': 'Água', 'price': 2.00, 'stock': 100, 'category': 'bebida'},
    {'name': 'Café', 'price': 3.00, 'stock': 40, 'category': 'bebida'},
    {'name': 'Chá', 'price': 3.00, 'stock': 40, 'category': 'bebida'},
]

for item in items:
    Item.objects.create(**item)

print("Itens de exemplo criados com sucesso.")