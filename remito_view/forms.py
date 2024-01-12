# forms.py
from django import forms

from clientes_view.models import Sujeto

from articulo_view.models import Articulo


def getSujetos():
    return [(sujeto.id, str(sujeto.cuit) + " - " + sujeto.name)
            for sujeto in Sujeto.objects.all().order_by("-name")]


class RemitoForm(forms.Form):
    id_remito = forms.IntegerField()
    provedor = forms.ChoiceField(choices=getSujetos)

    cliente = forms.ChoiceField(choices=getSujetos)
    fecha = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'date'}))


def getArticulos():
    return [(articulo.id, articulo.name)
            for articulo in Articulo.objects.all().order_by("-name")]


class TransaccionForm(forms.Form):
    articulo = forms.ChoiceField(choices=getArticulos)
    cantidad = forms.IntegerField()
