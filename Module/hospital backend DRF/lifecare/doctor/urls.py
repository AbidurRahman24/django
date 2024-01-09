
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter() # amader router
router.register('list', views.DoctorViewset)
router.register('designation', views.DesignationViewset)
router.register('specializetion', views.SpecializationViewset)
router.register('availableTime', views.AvailableTimeViewset)
router.register('review', views.ReviewViewset)
urlpatterns = [
    path('', include(router.urls)),
]

