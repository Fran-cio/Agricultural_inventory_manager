from django.shortcuts import render, redirect, get_object_or_404
from django.db import models

from remito_view.models import Transaccion
from clientes_view.models import Sujeto

from .models import Articulo
from .forms import ArticuloForm
# Create your views here.


def gestionar_articulos(request):
    if request.method == 'POST':
        Articulo.objects.create(
            name=request.POST['name'].upper(),
            unity_id=request.POST['unity_id'])
        return redirect('gestionar_articulos')

    articulos_info = []

    for articulo in Articulo.objects.all():
        ingresos = Transaccion.objects.filter(
            articulo=articulo,
            remito__cliente__cuit=20160761661,
        ).aggregate(
            models.Sum('cantidad'))['cantidad__sum'] or 0
        egresos = Transaccion.objects.filter(
            articulo=articulo,
            remito__provedor__cuit=20160761661,
        ).aggregate(
            models.Sum('cantidad'))['cantidad__sum'] or 0

        stock_total = ingresos - egresos

        # Crear una estructura de datos personalizada para contener
        # información del artículo y stock total
        articulo_info = {
            'id': articulo.id,
            'name': articulo.name,
            'unity': articulo.unity,
            'stock_total': stock_total,
        }
        # Agregar la información del artículo a la lista
        articulos_info.append(articulo_info)

    # Ordenar la lista de artículos según el stock_total
    articulos_info = sorted(
        articulos_info, key=lambda x: x['stock_total'], reverse=True)

    return render(request, 'index.html',
                  {'form': ArticuloForm(), 'articulos': articulos_info})


def del_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    if request.method == 'POST':
        articulo.delete()
        return redirect('gestionar_articulos')

    return render(request, 'del_articulo.html', {'articulo': articulo})


def gestionar_articulo(request, articulo_name):
    articulo = Articulo.objects.get(name=articulo_name)
    usuario = Sujeto.objects.get(cuit=20160761661)

    # Obtén todas las transacciones asociadas a este Articulo
    transacciones_cliente = Transaccion.objects.filter(
        articulo=articulo, remito__cliente=usuario).order_by("-remito__fecha")

    transacciones_provedor = Transaccion.objects.filter(
        articulo=articulo, remito__provedor=usuario).order_by("-remito__fecha")


# Calcular la suma del campo cantidad para cada lista de transacciones
    suma_cantidad_cliente = transacciones_cliente.aggregate(
        suma_cantidad=models.Sum('cantidad'))['suma_cantidad'] or 0
    suma_cantidad_proveedor = transacciones_provedor.aggregate(
        suma_cantidad=models.Sum('cantidad'))['suma_cantidad'] or 0

    return render(request, 'articulo.html',
                  {'articulo_name': articulo_name,
                   'transacciones_cliente': transacciones_cliente,
                   'transacciones_provedor': transacciones_provedor,
                   'cantidad_ingresados': suma_cantidad_cliente,
                   'cantidad_egresados': suma_cantidad_proveedor,
                   'stock_neto': suma_cantidad_cliente
                           - suma_cantidad_proveedor})
