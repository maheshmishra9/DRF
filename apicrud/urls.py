from django.urls import path
from apicrud.views import (
    CategoryAPI,
    category_api
    
)


app_name = "apicrud"

urlpatterns = [
    path("function/based/crud/category/", category_api, name="crud_category"),
    path("class/based/crud/category/", CategoryAPI.as_view(), name="crud_category"),
]