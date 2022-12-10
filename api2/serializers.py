from enum import auto
from rest_framework import serializers

from api2.models import Category


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    category_id = serializers.CharField(max_length=100)
    
    def create(self, validate_data):
        return Category.objects.create(**validate_data)


class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    item_id = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    image = serializers.ImageField()
    model_number = serializers.CharField(max_length=255)
    serial_number = serializers.CharField(max_length=255)
    brand_name = serializers.CharField(max_length=255)
    remarks = serializers.CharField(max_length=255)