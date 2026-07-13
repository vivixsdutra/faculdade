import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_neides.settings')
django.setup()

from neides.models import Item, Sale

# Assumindo que os itens já foram criados
items = {
    'Coxinha': Item.objects.get(name='Coxinha'),
    'Pastel': Item.objects.get(name='Pastel'),
    'Empada': Item.objects.get(name='Empada'),
    'Esfiha': Item.objects.get(name='Esfiha'),
    'Quibe': Item.objects.get(name='Quibe'),
    'Brigadeiro': Item.objects.get(name='Brigadeiro'),
    'Beijinho': Item.objects.get(name='Beijinho'),
    'Bolo de Cenoura': Item.objects.get(name='Bolo de Cenoura'),
    'Pudim': Item.objects.get(name='Pudim'),
    'Torta de Limão': Item.objects.get(name='Torta de Limão'),
    'Refrigerante': Item.objects.get(name='Refrigerante'),
    'Suco de Laranja': Item.objects.get(name='Suco de Laranja'),
    'Água': Item.objects.get(name='Água'),
    'Café': Item.objects.get(name='Café'),
    'Chá': Item.objects.get(name='Chá'),
}

# Criar vendas de exemplo
sales = [
    {'item': items['Coxinha'], 'quantity': 2},
    {'item': items['Pastel'], 'quantity': 3},
    {'item': items['Empada'], 'quantity': 1},
    {'item': items['Esfiha'], 'quantity': 4},
    {'item': items['Quibe'], 'quantity': 2},
    {'item': items['Brigadeiro'], 'quantity': 5},
    {'item': items['Beijinho'], 'quantity': 6},
    {'item': items['Bolo de Cenoura'], 'quantity': 1},
    {'item': items['Pudim'], 'quantity': 2},
    {'item': items['Torta de Limão'], 'quantity': 1},
    {'item': items['Refrigerante'], 'quantity': 3},
    {'item': items['Suco de Laranja'], 'quantity': 2},
    {'item': items['Água'], 'quantity': 5},
    {'item': items['Café'], 'quantity': 4},
    {'item': items['Chá'], 'quantity': 3},
]

for sale in sales:
    Sale.objects.create(**sale)

print("Vendas de exemplo criadas com sucesso.")