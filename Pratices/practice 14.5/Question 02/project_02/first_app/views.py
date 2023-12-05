from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home(request):
    student = models.Student.objects.all()
    return render(request,"first_app/home.html", {'data': student})