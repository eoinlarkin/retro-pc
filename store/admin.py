from django.contrib import admin
from .models import Product, ReleaseDecade, Manufacturer, Cpu

# Register your models here.
admin.site.register(Product)
admin.site.register(ReleaseDecade)
admin.site.register(Manufacturer)
admin.site.register(Cpu)