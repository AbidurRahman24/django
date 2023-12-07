from django.shortcuts import render
from category.models import TaskCategory

def home(request):
    # data = TaskCategory.objects.all()
    return render(request, 'home.html')