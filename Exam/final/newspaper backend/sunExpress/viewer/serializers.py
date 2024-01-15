from rest_framework import serializers
from . import models

class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Viewer
        fields = '__all__'