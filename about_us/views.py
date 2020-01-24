from django.shortcuts import render
from .models import AboutUs, Benefit, Chef


def index(request):
    return render(request, 'base.html')


def about_us(request):
    about = AboutUs.objects.all()
    benefits = Benefit.objects.all()
    chefs = Chef.objects.all()

    return render(request, 'about.html', {
        'about': about,
        'benefits': benefits,
        'chefs': chefs
    })
