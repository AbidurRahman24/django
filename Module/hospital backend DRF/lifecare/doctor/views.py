from django.shortcuts import render
from rest_framework import viewsets

from . import models
from . import serializers
# Create your views here.

class DoctorViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer

class DesignationViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class SpecializationViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class AvailableTimeViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer

class ReviewViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer