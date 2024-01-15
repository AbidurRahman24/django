from django.db import models
from category.models import Category
from editor.models import Editor

# Create your models here.
class Article(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publishing_time = models.DateTimeField(auto_now_add=True)
    ratings = models.IntegerField(default=0)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)

    # Additional necessary fields
    image = models.ImageField(upload_to='article/images/', null=True, blank=True)

    def __str__(self):
        return self.headline