from math import fsum
from django.db import models

from catering.models import CateringProduct


class Order(models.Model):
    email = models.EmailField(max_length=100, blank=True, verbose_name='Email Address')
    phone = models.CharField(max_length=100, blank=True)
    billing_first_name = models.CharField(max_length=250, blank=True)
    billing_last_name = models.CharField(max_length=250, blank=True)
    billing_address = models.CharField(max_length=250, blank=True)
    billing_postal_code = models.CharField(max_length=10, blank=True)
    billing_city = models.CharField(max_length=250, blank=True)
    billing_country = models.CharField(max_length=100, blank=True, default='Ukraine')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def get_totals(self):
        return fsum(order_item.sub_total() for order_item in self.items.all())

    def __str__(self):
        return f'{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(CateringProduct, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Price')
    quantity = models.PositiveIntegerField()

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return f'{self.product}'
