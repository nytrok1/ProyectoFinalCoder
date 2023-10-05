from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    puesto = models.CharField(max_length=40)
    


class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    documento = models.IntegerField()
    


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()


