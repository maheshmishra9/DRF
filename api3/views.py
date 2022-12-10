from django.shortcuts import render
from api3.serializers import BrandSerializer, CategorySerializer, ItemSerializer
from api3.models import Brand, Category, Item
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
# Create your views here.

class CategoryAPI(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BrandAPI(ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class ItemAPI(ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetailAPI(RetrieveAPIView):
    serializer_class =ItemSerializer
    
