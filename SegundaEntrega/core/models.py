from django.db import models

# Create your models here.
class Insumos(models.Model):
    nombre= models.CharField(max_length=120)
    precio= models.IntegerField()
    descripcion= models.CharField(max_length=200)
    stock= models.IntegerField()
    def __str__(self):
        return self.nombre

class Registros(models.Model):
    nombre= models.CharField(max_length=80)
    apellido=models.CharField(max_length=80)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=12)
    contraseña= models.CharField(max_length=20)
    contraseña2= models.CharField(max_length=20)
    def __str__(self):
        return self.username

