# forms.py
# pylint: disable=duplicate-code,line-too-long
from django import forms
from django.db.utils import OperationalError

from location_view.models import Pais, Provincia, Localidad
from .models import Iva_cat


class SujetoForm(forms.Form):
    # Modificar el campo de unidad para que sea un ChoiceField
    name = forms.CharField(label="Nombre del sujeto", max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input'}))

    pais = forms.ModelChoiceField(queryset=Pais.objects.all(
    ), empty_label="Seleccione un país", required=False)
    provincia = forms.ModelChoiceField(queryset=Provincia.objects.none(
    ), empty_label="Seleccione una provincia", required=False)
    localidad = forms.ModelChoiceField(queryset=Localidad.objects.none(
    ), empty_label="Seleccione una localidad", required=False)
    cuit = forms.IntegerField()

    try:
        iva_id = forms.ChoiceField(
            choices=[(iva.id, iva.name) for iva in Iva_cat.objects.all()])
    except OperationalError as e:
        print("Tabla no cargada - ", e)
