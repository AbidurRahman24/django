from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
def add_car_brand(request):
    if request.method == 'POST':
        brand_form = forms.BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            messages.success(request, 'Added Brand Name Successfully')
            return redirect('add_brand')
    else:
        brand_form = forms.BrandForm()
    # print(album_form)
    return render(request, 'add_brand.html', {'form' : brand_form})