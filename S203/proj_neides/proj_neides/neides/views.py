from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Item, Sale, Discount
from .forms import ItemForm, DiscountForm
from .strategies import FixedDiscount, PercentageDiscount

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from neides.controllers.item_controller import list_items, add_item, edit_item, delete_item, client_dashboard
from neides.controllers.discount_controller import list_discounts, add_discount, edit_discount, delete_discount
from neides.controllers.sale_controller import list_sales

def index(request):
    return redirect('login')

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    else:
        return redirect('client_dashboard')

@login_required
def admin_dashboard(request):
    return render(request, 'neides/admin_dashboard.html')


def index(request):
    return redirect('login')

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    else:
        return redirect('client_dashboard')

@login_required
def admin_dashboard(request):
    return render(request, 'neides/admin_dashboard.html')

@login_required
def client_dashboard(request):
    salgados = Item.objects.filter(category='salgado')
    doces = Item.objects.filter(category='doce')
    bebidas = Item.objects.filter(category='bebida')

    # Apply discount strategies
    for item in salgados:
        item.set_discount_strategy(FixedDiscount(1.00))  # Example: Fixed discount of 1.00
    for item in doces:
        item.set_discount_strategy(PercentageDiscount(10))  # Example: 10% discount

    return render(request, 'neides/client_dashboard.html', {
        'salgados': salgados,
        'doces': doces,
        'bebidas': bebidas,
    })

@login_required
def items(request):
    items = Item.objects.all()
    return render(request, 'neides/items.html', {'items': items})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm()
    return render(request, 'neides/add_item.html', {'form': form})

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'neides/edit_item.html', {'form': form})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('items')
    return render(request, 'neides/delete_item.html', {'item': item})

@login_required
def stock(request):
    items = Item.objects.all()
    return render(request, 'neides/stock.html', {'items': items})

@login_required
def reports(request):
    sales = Sale.objects.all()
    return render(request, 'neides/reports.html', {'sales': sales})

@login_required
def discounts(request):
    discounts = Discount.objects.all()
    return render(request, 'neides/discounts.html', {'discounts': discounts})

@login_required
def add_discount(request):
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discounts')
    else:
        form = DiscountForm()
    return render(request, 'neides/add_discount.html', {'form': form})

@login_required
def edit_discount(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    if request.method == 'POST':
        form = DiscountForm(request.POST, instance=discount)
        if form.is_valid():
            form.save()
            return redirect('discounts')
    else:
        form = DiscountForm(instance=discount)
    return render(request, 'neides/edit_discount.html', {'form': form})

@login_required
def delete_discount(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    if request.method == 'POST':
        discount.delete()
        return redirect('discounts')
    return render(request, 'neides/delete_discount.html', {'discount': discount})