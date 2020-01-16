from django.shortcuts import render
from django.views.generic import View

from .models import Post, Category, Tag
from .utils import ObjectDetailMixin


def posts_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    return render(request, 'blog.html', {
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
