from django.urls import path
from .views import posts_list, posts_categories, post_leave_comment, tags_list
from .views import PostDetail, TagDetail


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('categories', posts_categories, name='posts_categories_url'),
    path('post/<str:slug>', PostDetail.as_view(), name='post_details_url'),
    path('comment/<str:slug>', post_leave_comment, name='post_leave_comment_url'),
    path('tag_s', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_details_url'),
]
