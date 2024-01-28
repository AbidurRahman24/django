from django.db import models
from django.contrib.auth.models import User
from account.models import Seller
# Create your models here.
ORDER_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]
class FlowerCategory(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
        return self.name
    
class Flower(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="flower/images/")
    category = models.ManyToManyField(FlowerCategory)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    

class Order(models.Model):
    user = models.ForeignKey(Seller, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices = ORDER_STATUS, max_length = 10, default = "Pending")
    cancel = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.user.user.first_name} {self.flower.title}"
        # return f"Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name}"