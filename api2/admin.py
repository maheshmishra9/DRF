from atexit import register
from django.contrib import admin

from api2.models import (
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