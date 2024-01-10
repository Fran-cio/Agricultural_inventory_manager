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
                    id_remito=request.POST['id_remito'].upper(),
                    provedor_id=request.POST['provedor'],
                    cliente_id=request.POST['cliente'],
                    fecha=request.POST['fecha'])
            except Exception as e:
                print(e)
        return redirect('gestionar_remito')

    remitos = Remito.objects.all().order_by('-fecha')
    print(remitos.values())

    return render(request, 'index_r.html',
                  {'form': RemitoForm(), 'remitos': remitos})


def del_remito(request, remito_id):
    remito = get_object_or_404(Remito, id=remito_id)

    if request.method == 'POST':
        remito.delete()
        return redirect('gestionar_remito')

    return render(request, 'del_remito.html', {'remito': remito})
