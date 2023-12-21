from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) 
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return self.title