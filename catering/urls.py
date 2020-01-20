from django.urls import path
from .views import catering_products_list, catering_product_details


urlpatterns = [
    path('', catering_products_list, name='catering_products_list_url'),
    path('<str:slug>', catering_product_details, name='catering_product_details_url'),
]
