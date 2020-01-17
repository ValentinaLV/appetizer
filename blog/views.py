from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Post, Category, Tag
from .forms import CommentForm
from .utils import ObjectDetailMixin, PostDetailMixin


def posts_search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(tags__title__icontains=search_query)
        ).distinct()
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


def post_leave_comment(request, slug):
    post_details = Post.objects.get(slug=slug)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post_details
            new_comment.save()
            return redirect('blog:post_details_url', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'leave_comment.html', {
        'post_details': post_details,
        'form': comment_form
    })


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {
        'tags': tags
    })


class PostDetail(PostDetailMixin, View):
    model = Post
    template = 'post_details.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'tag_details.html'
