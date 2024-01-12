from django.db import models

from articulo_view.models import Articulo
from clientes_view.models import Sujeto

# Create your models here.


class Remito(models.Model):
    nro_remito = models.IntegerField(default=0, unique=True)
    provedor = models.ForeignKey(
        Sujeto, on_delete=models.CASCADE, related_name='remitos_proveedor')
    cliente = models.ForeignKey(
        Sujeto, on_delete=models.CASCADE, related_name='remitos_cliente')
    fecha = models.DateField()


class Transaccion(models.Model):
    remito = models.ForeignKey(Remito, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
