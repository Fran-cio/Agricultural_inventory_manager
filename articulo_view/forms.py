# forms.py

# pylint: disable=duplicate-code,line-too-long

from django import forms

from .models import Unity_cat


def get_unity():
    unitys = [(unity.id, unity.name) for unity in Unity_cat.objects.all()]

    # Agregar opción vacía
    unitys.insert(0, ("", "-"*100))

    return unitys


class ArticuloForm(forms.Form):
    # Modificar el campo de unidad para que sea un ChoiceField
    name = forms.CharField(label="Titulo de tarea", max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input'}))

    unity_id = forms.ChoiceField(choices=get_unity)
