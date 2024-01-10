from django.db import models

# Create your models here.


class Pais(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Provincia(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Localidad(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
