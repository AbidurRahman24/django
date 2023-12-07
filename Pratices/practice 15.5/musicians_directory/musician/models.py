from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length = 50)
    Phone_number = models.CharField(max_length=12)
    Instrument_Type = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name


