from django.contrib import admin
from apicrud.models import (
    Category,
    Brand,
    Item
)


admin.site.register(
    [
    Category,
    Brand,
    Item,
    ]
)