from django.urls import path
from .views import posts_list, tags_list
from .views import PostDetail


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>', PostDetail.as_view(), name='post_details_url'),
    path('tag_s', tags_list, name='tags_list_url'),
]
