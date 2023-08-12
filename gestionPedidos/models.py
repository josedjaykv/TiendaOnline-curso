from django.db import models

# Create your models here.

#Creamos una clase por cada tabla que va a tener la base de datos
# tambien se conoce como modelos
class Clientes(models.Model):
    #Campos y tipos de datos
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name = "La dirección")
    email = models.EmailField(blank = True, null = True)
    tfno = models.CharField(max_length = 15)

    def __str__(self):
        return 'Nombre: %s - Direccion: %s - Email: %s - Telefono: %s' %(self.nombre, self.direccion , self.email, self.tfno)

#Tabla artículos
class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'Nombre: %s - Sección: %s - Precio: %s' %(self.nombre, self.seccion, self.precio)

#Tabla pedidos
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return 'Numero: %s - Fecha: %s - Entregado: %s' %(self.numero, self.fecha, self.entregado)