from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Us"

    def __str__(self):
        return f"{self.title}"


class Benefit(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name = "Benefit"
        verbose_name_plural = "Benefits"

    def __str__(self):
        return f"{self.title}"


class Chef(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    bio = models.TextField()
    image = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return f"{self.name}"
