from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# Create your views here.
def add_car_model(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, 'Added Car Model Successfully')
            return redirect('add_car')
    else:
        car_form = forms.CarForm()
    return render(request, 'add_car.html', {'form' : car_form})