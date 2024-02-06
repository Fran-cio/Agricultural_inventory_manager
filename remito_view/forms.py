# forms.py
from django import forms

from clientes_view.models import Sujeto

from articulo_view.models import Articulo


def getSujetos():
    sujetos = [(sujeto.id, str(sujeto.cuit) + " - " + sujeto.name)
               for sujeto in Sujeto.objects.all().order_by("name")]

    # Obtener el ID de "FERNANDO CESAR CIORDIA"
    fernando_ciordia_id = Sujeto.objects.get(cuit=20160761661).id

    # Mover la opción de "FERNANDO CESAR CIORDIA" al principio de la lista
    fernando_ciordia_option = [
        option for option in sujetos if option[0] == fernando_ciordia_id]
    sujetos.remove(fernando_ciordia_option[0])
    sujetos.insert(0, fernando_ciordia_option[0])

    # Agregar opción vacía después del "Sujeto"
    sujetos.insert(1, ("", "-----------------------------------------------------------------------------"))

    return sujetos


class RemitoForm(forms.Form):
    id_remito = forms.IntegerField()
    provedor = forms.ChoiceField(choices=getSujetos)

    cliente = forms.ChoiceField(choices=getSujetos)
    fecha = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'date'}))


def getArticulos():
    return [(articulo.id, articulo.name)
            for articulo in Articulo.objects.all().order_by("name")]


class TransaccionForm(forms.Form):
    articulo = forms.ChoiceField(choices=getArticulos)
    cantidad = forms.IntegerField()
