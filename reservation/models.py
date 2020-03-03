from django.db import models

from .utils import send_email


class Reservation(models.Model):
    NUMBER_OF_PERSONS = [
        ('One', '1'),
        ('Two', '2'),
        ('Three', '3'),
        ('Four', '4'),
        ('Five', '5'),
        ('Six', '6'),
        ('More than six', '6+')
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    number_of_persons = models.CharField(max_length=30, choices=NUMBER_OF_PERSONS)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.id:
            send_email(f"Reservation Appetizer restaurant",
                       f"Hi {self.name},\n"
                       f"Your reservation confirmed successfully\n"
                       f"Reservation date and time {self.date} {self.time}\n"
                       f"Number of persons {self.number_of_persons}",
                       [self.email])
        super().save(*args, **kwargs)
