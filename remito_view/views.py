from django.shortcuts import render, redirect, get_object_or_404

from .models import Remito, Transaccion
from .forms import RemitoForm, TransaccionForm

# Create your views here.
# views.py


def gestionar_remito(request):
    if request.method == 'POST':
        if (request.POST['provedor'] != request.POST['cliente']):
            try:
                Remito.objects.create(
                    nro_remito=request.POST['nro_remito'].upper(),
                    provedor_id=request.POST['provedor'],
                    cliente_id=request.POST['cliente'],
                    fecha=request.POST['fecha'])
            except Exception as e:
                print(e)
        return redirect('gestionar_remito')

    remitos = Remito.objects.all().order_by('-fecha')

    return render(request, 'index_r.html',
                  {'form': RemitoForm(), 'remitos': remitos})


def del_remito(request, remito_id):
    remito = get_object_or_404(Remito, id=remito_id)

    if request.method == 'POST':
        remito.delete()
        return redirect('gestionar_remito')

    return render(request, 'del_remito.html', {'remito': remito})


def gestionar_transacciones(request, nro_remito):
    remito = get_object_or_404(Remito, nro_remito=nro_remito)

    if request.method == 'POST':
        try:
            Transaccion.objects.create(
                remito=remito,
                articulo_id=request.POST['articulo'],
                cantidad=request.POST['cantidad'],
            )
        except Exception as e:
            print(e)
        return redirect('gestionar_transacciones', nro_remito)

    transacciones = Transaccion.objects.filter(
        remito=remito).order_by('-articulo__name')

    return render(request, 'index_transacciones.html',
                  {'form': TransaccionForm(),
                   'remito': remito, 'transacciones': transacciones})


def del_transaccion(request, nro_remito, transaccion_id):
    transaccion = get_object_or_404(Transaccion, id=transaccion_id)

    transaccion.delete()
    return redirect('gestionar_transacciones', nro_remito)
