from django.urls import path
from .views import posts_list, post_details, tags_list


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>', post_details, name='post_details_url'),
    path('tag_s', tags_list, name='tags_list_url'),
]
