from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers

class ViewerViewset(viewsets.ModelViewSet):
    queryset = models.Viewer.objects.all()
    serializer_class = serializers.ViewerSerializer
