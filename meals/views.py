from django.shortcuts import render
from .models import Meals, Category


def meal_list(request):
    meals = Meals.objects.all()
    categories = Category.objects.all()

    return render(request, 'menu.html', {
        'meals': meals,
        'categories': categories,
    })


def meal_details(request, slug):
    meal = Meals.objects.get(slug=slug)
    return render(request, 'menu_details.html', {
        'meal': meal
    })
