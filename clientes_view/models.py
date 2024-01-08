from django.db import models

# Create your models here.


class Localidad(models.Model):
    name = models.CharField(max_length=100)


class Iva_cat(models.Model):
    name = models.CharField(max_length=100)


class Sujeto(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location = models.ForeignKey(Localidad, models.CASCADE)
    iva = models.ForeignKey(Iva_cat, models.DO_NOTHING)
