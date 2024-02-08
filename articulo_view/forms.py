# forms.py

# pylint: disable=duplicate-code,line-too-long

from django import forms
from django.db.utils import OperationalError

from .models import Unity_cat


class ArticuloForm(forms.Form):
    # Modificar el campo de unidad para que sea un ChoiceField
    name = forms.CharField(label="Titulo de tarea", max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input'}))

    try:
        unity_id = forms.ChoiceField(
            choices=[(unity.id, unity.name) for
                     unity in Unity_cat.objects.all()])
    except OperationalError as e:
        print("Tabla no cargada - ", e)
