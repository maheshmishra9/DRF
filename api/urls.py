from django.urls import path

from .views import (
    brand_details,
    category_details,
    item_details,

)

app_name = "api"

urlpatterns = [
    path("api/category/<int:pk>", category_details, name = "category"),
    path("api/brand/", brand_details, name="brand"),
    path("api/item/", item_details, name="item")
]
