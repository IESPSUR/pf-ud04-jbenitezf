from django.conf import settings
from django.db import models
from django.utils import timezone

class Compra(models.Model):
    fecha = models.DateTimeField(default=timezone.now)

    unidades = models.IntegerField()
    importe = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Marca(models.Model):
    nombremarca = models.TextField()

    def __str__(self):
        return self.nombremarca


class Producto(models.Model):
    nombre = models.TextField(primary_key=True)
    modelo = models.TextField()
    unidades = models.IntegerField()
    precio = models.FloatField()
    detalles = models.TextField()
    marca = models.ForeignKey(Marca, models.PROTECT)

    def __str__(self):
        return self.nombre


