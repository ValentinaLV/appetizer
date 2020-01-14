from django.shortcuts import render


def home_page(request):
    return render(request, 'base.html')


def blog(request):
    return render(request, 'blog.html')


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def reservation(request):
    return render(request, 'reservation.html')


def menu(request):
    return render(request, 'menu.html')


def catering(request):
    return render(request, 'catering.html')
