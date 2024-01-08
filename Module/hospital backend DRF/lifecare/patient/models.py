from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    image = models.ImageField(upload_to='patient/images/')
    phone_no = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'