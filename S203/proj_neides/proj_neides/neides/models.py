from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .strategies import FixedDiscount, PercentageDiscount

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('salgado', 'Salgado'),
        ('doce', 'Doce'),
        ('bebida', 'Bebida'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    discount_strategy = None

    def __str__(self):
        return self.name

    def set_discount_strategy(self, strategy):
        self.discount_strategy = strategy

    def get_price_with_discount(self):
        if self.discount_strategy:
            return self.discount_strategy.apply_discount(self.price)
        return self.price

# Observer Pattern: Signal to notify changes in Item
@receiver(post_save, sender=Item)
@receiver(post_delete, sender=Item)
def notify_item_change(sender, instance, **kwargs):
    # Logic to notify views about the change
    print(f'Item {instance.name} has been updated/created/deleted.')

class Sale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.item.name}'

class Discount(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    


