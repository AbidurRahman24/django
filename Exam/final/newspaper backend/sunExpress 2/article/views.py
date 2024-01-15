from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class =  serializers.ArticleSerializer

class ReviewViewset(viewsets.ModelViewSet):
    
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer