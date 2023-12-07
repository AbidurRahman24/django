from django.db import models
from category.models import TaskCategory
# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    category = models.ManyToManyField(TaskCategory)
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.taskTitle