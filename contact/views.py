from django.shortcuts import render, redirect
from .forms import ContactUsForm


def contact_us(request):
    contact_form = ContactUsForm()
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('contact:contact_us_url')

    return render(request, 'contact_us.html', {
        'form': contact_form
    })
