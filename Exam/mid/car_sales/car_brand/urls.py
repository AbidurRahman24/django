from django.urls import path
from . import views
urlpatterns = [

    path('add/', views.add_car_brand, name='add_brand')
]