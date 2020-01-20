from django.urls import path
from .views import add_to_cart, cart_details


urlpatterns = [
    path('', cart_details, name='cart_details_url'),
    path('add/<str:slug>', add_to_cart, name='add_to_cart_url'),

]
