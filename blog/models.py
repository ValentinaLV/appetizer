from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from meals.models import get_slug


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='posts/', null=True)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    tags = models.ManyToManyField('Tag', related_name='posts')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.category_name}"


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.title}"
