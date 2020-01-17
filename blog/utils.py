from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .models import Comment
from .forms import CommentForm


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)

        return render(request, self.template,
                      context={self.model.__name__.lower(): obj,
                               'admin_object': obj,
                               'detail': True
                               })


class PostDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        comments = Comment.objects.filter(post=obj)

        context = {self.model.__name__.lower(): obj,
                   'comments': comments,
                   'admin_object': obj,
                   'detail': True}

        return render(request, self.template,
                      context=context)
