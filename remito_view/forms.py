# forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Remito, Transaccion


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['articulo', 'cantidad']


TransaccionFormSet = inlineformset_factory(
    Remito, Transaccion, form=TransaccionForm, extra=1)


class RemitoForm(forms.ModelForm):
    class Meta:
        model = Remito
        fields = ['provedor', 'cliente', 'fecha']
