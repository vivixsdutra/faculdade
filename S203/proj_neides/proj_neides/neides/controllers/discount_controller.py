from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from neides.models import Discount
from neides.forms import DiscountForm

@login_required
def list_discounts(request):
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