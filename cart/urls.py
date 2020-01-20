from django.urls import path

from .views import cart_details, add_to_cart, remove_from_cart, full_remove_from_cart

urlpatterns = [
    path('', cart_details, name='cart_details_url'),
    path('add/<str:slug>', add_to_cart, name='add_to_cart_url'),
    path('remove/<str:slug>', remove_from_cart, name='remove_from_cart_url'),
    path('full_remove/<str:slug>', full_remove_from_cart, name='full_remove_from_cart_url')

]
