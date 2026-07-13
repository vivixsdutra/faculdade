from django import forms
from .models import Item, Discount

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'stock']

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['name', 'percentage']