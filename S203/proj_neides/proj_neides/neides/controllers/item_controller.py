from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from neides.models import Item
from neides.forms import ItemForm
from neides.strategies import FixedDiscount, PercentageDiscount

@login_required
def list_items(request):
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