from django.shortcuts import render


def home_page(request):
    return render(request, 'base.html')


def catering(request):
    return render(request, 'catering.html')
