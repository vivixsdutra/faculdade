from django.contrib import admin
from .models import Item, Sale, Discount

admin.site.register(Item)
admin.site.register(Sale)
admin.site.register(Discount)