from django.db import models


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
