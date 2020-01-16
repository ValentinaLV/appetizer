from django.shortcuts import render
from .models import Post, Category, Tag


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {
        'posts': posts
    })


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {
        'tags': tags
    })


def post_details(request, slug):
    pass
