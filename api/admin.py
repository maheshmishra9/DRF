from django.contrib import admin

from api.models import (
    Brand,
    Category,
    Item
    )

# Register your models here.

admin.site.register(
    [
    Category,
    Brand,
    Item
    ]
)