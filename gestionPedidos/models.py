from django.db import models

# Create your models here.

#Creamos una clase por cada tabla que va a tener la base de datos
# tambien se conoce como modelos
class Clientes(models.Model):
    #Campos y tipos de datos
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    tfno = models.CharField(max_length = 15)

#Tabla artículos
class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la sección es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)

#Tabla pedidos
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()