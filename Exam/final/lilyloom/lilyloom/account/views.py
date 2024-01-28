from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class SellerViewSet(viewsets.ModelViewSet):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer
