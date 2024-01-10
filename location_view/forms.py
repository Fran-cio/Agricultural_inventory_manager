# forms.py

from django import forms


class addForm(forms.Form):
    # Modificar el campo de unidad para que sea un ChoiceField
    name = forms.CharField(label="Titulo", max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input'}))
