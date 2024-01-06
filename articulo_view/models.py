from django.db import models

# Create your models here.


class Unity_cat(models.Model):
    name = models.CharField(max_length=100)


class Articulo(models.Model):
    name = models.CharField(max_length=100)
    unity = models.ForeignKey(Unity_cat, on_delete=models.DO_NOTHING)
