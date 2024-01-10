from django.shortcuts import render, redirect

from .models import Remito, Transaccion
from .forms import RemitoForm, TransaccionFormSet

# Create your views here.
# views.py


def agregar_remito(request):
    if request.method == 'POST':
        remito_form = RemitoForm(request.POST)
        transaccion_formset = TransaccionFormSet(
            request.POST, instance=Remito())

        if remito_form.is_valid() and transaccion_formset.is_valid():
            remito = remito_form.save()
            transaccion_formset.instance = remito
            transaccion_formset.save()

            return redirect('lista_remitos')

    else:
        remito_form = RemitoForm()
        transaccion_formset = TransaccionFormSet(instance=Remito())

    return render(request, 'index_r.html',
                  {'remito_form': remito_form,
                   'transaccion_formset': transaccion_formset})
