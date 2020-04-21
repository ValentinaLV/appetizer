from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from meals.models import get_slug


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 1 автор к множеству постов
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)  # 1 категория к множеству постов
    image = models.ImageField(upload_to='posts/', null=True)
    slug = models.SlugField(max_length=150, blank=True, null=True, unique=True)
    tags = models.ManyToManyField('Tag', related_name='posts')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_details_url', kwargs={'slug': self.slug})

    def get_comment_url(self):
        return reverse('blog:post_leave_comment_url', kwargs={'slug': self.slug})

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

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('blog:tag_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 1 юзер - много комментов
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 1 пост - много комментов
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.content}"
