from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from time import time


def get_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Meals(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=500)
    persons = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True, unique=True)

    def get_absolute_url(self):
        return reverse('meal_details_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_slug(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Meal"
        verbose_name_plural = "Meals"

    def __str__(self):
        return f"{self.name}"

