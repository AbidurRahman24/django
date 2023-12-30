from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    borrowing_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ManyToManyField(Category) # ekta post multiple categorir moddhe thakte pare abar ekta categorir moddhe multiple post thakte pare
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='books/media/uploads/', blank = True, null = True)
    
    def __str__(self):
        return self.title 
    
    

    
    