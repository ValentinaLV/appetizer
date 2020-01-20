from django.db import models
from catering.models import CateringProduct


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return f'{self.cart_id}'


class CartItem(models.Model):
    product = models.ForeignKey(CateringProduct, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product}'
