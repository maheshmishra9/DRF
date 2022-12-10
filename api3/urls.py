from django.urls import path
from api3.views import BrandAPI, CategoryAPI, ItemAPI, ItemDetailAPI
app_name = "api3"

urlpatterns = [
    path("api3/category/", CategoryAPI.as_view(), name="cat"),
    path("api3/brand/", BrandAPI.as_view(), name="brand"),
    path("api3/item/", ItemAPI.as_view(), name="item"),
    path("api3/item/detail/<int:pk>", ItemDetailAPI.as_view(), name="tm")
]