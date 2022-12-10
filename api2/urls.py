from django.urls import path

from .views import (
    category_create,
    update
)

app_name = "api2"

urlpatterns = [
    path("api2/category/create/", category_create, name = "category"),

]
