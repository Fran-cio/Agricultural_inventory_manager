from django.db import models

from location_view.models import Localidad
# Create your models here.


class Iva_cat(models.Model):
    name = models.CharField(max_length=100)


class Sujeto(models.Model):
    name = models.CharField(max_length=100)
    cuit = models.IntegerField(default=0, unique=True)
    address = models.CharField(max_length=100)
    location = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    iva = models.ForeignKey(Iva_cat, on_delete=models.DO_NOTHING)
