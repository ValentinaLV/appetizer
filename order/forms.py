from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['billing_first_name', 'billing_last_name',
                  'phone', 'email', 'billing_address', 'billing_postal_code',
                  'billing_city']

        widgets = {
            'billing_first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'billing_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+38093 777 7777', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'appetizer@email.com'}),
            'billing_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'billing_postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '01034'}),
            'billing_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
        }
