from django.urls import path
from .views import order_create, order_history, order_details


urlpatterns = [
    path('create_order/', order_create, name='order_create_url'),
    path('order_history/', order_history, name='order_history_url'),
    path('order_details/<int:order_id>', order_details, name='order_details_url'),

]
