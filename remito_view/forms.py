# forms.py
from django import forms

from clientes_view.models import Sujeto

from .models import Remito, Transaccion


class RemitoForm(forms.Form):
    id_remito = forms.IntegerField()
    provedor = forms.ChoiceField(
        choices=[(sujeto.id, str(sujeto.cuit) + " - " + sujeto.name)
                 for sujeto in Sujeto.objects.all().order_by("-name")])

    cliente = forms.ChoiceField(
        choices=[(sujeto.id, str(sujeto.cuit) + " - " + sujeto.name)
                 for sujeto in Sujeto.objects.all().order_by("-name")])
    fecha = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'date'}))


class TransaccionForm(forms.Form):
    print()
