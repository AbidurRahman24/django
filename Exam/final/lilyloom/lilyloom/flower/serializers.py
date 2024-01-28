from rest_framework import serializers
from . import models

class FlowerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FlowerCategory
        fields = '__all__'

class FlowerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Flower
        fields = ['title', 'description', 'price', 'image', 'category', 'created_by']
        read_only_fields = ['created_by']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'