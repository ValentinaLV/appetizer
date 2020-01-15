from django.shortcuts import render
from .models import Meals


def meal_list(request):
    meals = Meals.objects.all()
    return render(request, 'menu.html', {
        'meals': meals
    })


def meal_details(request, slug):
    meal = Meals.objects.get(slug=slug)
    return render(request, 'menu_details.html', {
        'meal': meal
    })
