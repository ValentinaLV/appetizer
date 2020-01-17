from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View

from .models import Post, Category, Tag
from .utils import ObjectDetailMixin


def posts_search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )
    else:
        posts = Post.objects.all()
    return posts


def posts_list(request):
    return render(request, 'blog.html', {
        'posts': posts_search(request),
    })


def posts_categories(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    return render(request, 'posts_categories.html', {
        'posts': posts,
        'categories': categories
    })


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {
        'tags': tags
    })


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'post_details.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'tag_details.html'
