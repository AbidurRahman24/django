from django.shortcuts import render
from rest_framework import viewsets

from . import models
from . import serializers
# Create your views here.

class PatientViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer