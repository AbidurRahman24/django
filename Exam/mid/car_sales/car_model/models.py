from django.db import models
from car_brand.models import Brand
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='car')
    image = models.ImageField(upload_to='car_model/media/uploads/', blank = True, null = True)
    # image = models.ImageField(upload_to='uploads/', blank = True, null = True)
    # brand_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"Comments by {self.name}"