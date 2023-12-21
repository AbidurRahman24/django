from django.urls import path
from . import views
urlpatterns = [
    path("add/", views.add_car_model, name='add_car')
]