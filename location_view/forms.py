# forms.py

from django import forms

from clientes_view.models import Iva_cat


class addForm(forms.Form):
    # Modificar el campo de unidad para que sea un ChoiceField
    name = forms.CharField(label="Titulo", max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input'}))


class addSujetoLocalidadForm(forms.Form):
    # Modificar el campo de unidad para que sea un ChoiceField
    name = forms.CharField(label="Nombre del sujeto", max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input'}))
    cuit = forms.IntegerField()
    iva_id = forms.ChoiceField(
        choices=[(iva.id, iva.name) for iva in Iva_cat.objects.all()])
