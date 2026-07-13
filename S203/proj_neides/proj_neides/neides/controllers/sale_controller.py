from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from neides.models import Sale

@login_required
def list_sales(request):
    sales = Sale.objects.all()
    return render(request, 'neides/reports.html', {'sales': sales})