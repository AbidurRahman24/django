from django.db import models
# from task.models import TaskModel
# Create your models here.
class TaskCategory(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name