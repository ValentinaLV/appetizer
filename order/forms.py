from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['billing_first_name', 'billing_last_name',
                  'phone', 'email', 'billing_address', 'billing_postal_code',
                  'billing_city']
