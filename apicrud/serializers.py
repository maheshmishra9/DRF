from rest_framework import serializers
from apicrud.models import (
    Category,
    Brand,
    Item
)

class CategorySerializers(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    category_id = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Category.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get("name",instance.name)
        instance.description = validate_data.get("description", instance.description)
        instance.category_id = validate_data.get("category_id", instance.category_id)
        instance.save()
        return instance
