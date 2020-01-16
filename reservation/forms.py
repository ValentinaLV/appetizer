from django import forms
from .models import Reservation


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required': 'required'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'number_of_persons': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YYYY', 'required': 'required'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'HH/MM/SS', 'required': 'required'})
        }
