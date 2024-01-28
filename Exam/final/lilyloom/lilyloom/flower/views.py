from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import generics, permissions
from rest_framework import filters

class FlowerCategoryViewset(viewsets.ModelViewSet):
    queryset = models.FlowerCategory.objects.all()
    serializer_class = serializers.FlowerCategorySerializer

class FlowerCreateViewset(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = models.Flower.objects.all()
    serializer_class = serializers.FlowerCreateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name','title']

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)

class OrderViewset(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset() # 7 no line ke niye aslam ba patient ke inherit korlam
        print(self.request.query_params)
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset