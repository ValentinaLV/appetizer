from django.shortcuts import render


def home_page(request):
    return render(request, 'base.html')


def about_us(request):
    return render(request, 'about.html')


def catering(request):
    return render(request, 'catering.html')
