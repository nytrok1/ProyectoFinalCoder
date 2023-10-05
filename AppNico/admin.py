from django.contrib import admin
from .models import Empleado , Cliente , Producto

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Producto)