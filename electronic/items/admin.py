from django.contrib import admin
from .models import ItemA , ItemB, ItemC

# Register your models here.
admin.site.register(ItemB)
admin.site.register(ItemC)
admin.site.register(ItemA)
