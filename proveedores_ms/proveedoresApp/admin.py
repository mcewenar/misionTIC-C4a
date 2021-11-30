from django.contrib import admin

# Register your models here.
from .models.proveedor import Proveedor
admin.site.register(Proveedor)