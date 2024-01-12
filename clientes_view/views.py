from django.shortcuts import render, redirect, get_object_or_404

from remito_view.models import Remito

from .models import Sujeto
# Create your views here.


def gestionar_sujetos(request):
    sujetos = Sujeto.objects.all()
    return render(request, 'index_u.html', {'sujetos': sujetos})


def del_sujeto(request, sujeto_id):
    sujeto = get_object_or_404(Sujeto, id=sujeto_id)

    if request.method == 'POST':
        sujeto.delete()
        return redirect('gestionar_sujetos')

    return render(request, 'del_sujeto.html', {'sujeto': sujeto})


def gestionar_sujeto(request, cuit):
    sujeto = Sujeto.objects.get(cuit=cuit)

    # Obtén todas las transacciones asociadas a este Articulo
    remito_cliente = Remito.objects.filter(cliente=sujeto).order_by("-fecha")

    remito_provedor = Remito.objects.filter(provedor=sujeto).order_by("-fecha")

    return render(request, 'gestionar_sujeto.html',
                  {'sujeto': sujeto,
                   'remitos_cliente': remito_cliente,
                   'remitos_provedor': remito_provedor})
