# forms.py

from django import forms

from .models import Articulo, Unity_cat


class ArticuloForm(forms.Form):
    # Modificar el campo de unidad para que sea un ChoiceField
    name = forms.CharField(label="Titulo de tarea", max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input'}))
    unity_id = forms.ChoiceField(
        choices=[(unity.id, unity.name) for unity in Unity_cat.objects.all()])
