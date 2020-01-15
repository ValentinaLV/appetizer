from django.urls import path
from .views import meal_list, meal_details


urlpatterns = [
    path('', meal_list, name='meal_list_url'),
    path('<str:slug>', meal_details, name='meal_details_url'),
]
