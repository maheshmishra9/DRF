from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.renderers import JSONRenderer

from .models import (
    Category,
    Brand,
    Item
)
from .serializers import(
    CategorySerializer,
    BrandSerializer,
    ItemSerializer
)


def category_details(request, pk):
    cat = Category.objects.get(id = pk)
    serializer = CategorySerializer(cat)
    return JsonResponse(serializer.data)

def brand_details(request):
    bar = Brand.objects.all()
    serializer = BrandSerializer(bar, many=True)
    return JsonResponse(serializer.data, safe=False)

def item_details(request):
    ite = Item.objects.all()
    serializer = ItemSerializer(ite, many=True)
    return JsonResponse(serializer.data, safe=False)

