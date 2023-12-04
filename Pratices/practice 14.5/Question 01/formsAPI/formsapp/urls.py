from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('show/', views.show, name='show'),
    path('', views.DjangoForm, name="django_form")
]
