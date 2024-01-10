from django.shortcuts import render, redirect, get_object_or_404

from django.db.models import Count, Value
from django.db.models.functions import Coalesce

from .models import Pais, Provincia, Localidad
from .forms import addForm, addSujetoLocalidadForm

from clientes_view.models import Sujeto
# Create your views here.


def gestionar_paises(request):
    if request.method == 'POST':
        Pais.objects.create(
            name=request.POST['name'].upper())
        return redirect('gestionar_paises')

    sujetos_por_pais = Pais.objects.annotate(
        cantidad_sujetos=Coalesce(
            Count('provincia__localidad__sujeto'), Value(0))
    ).values('id', 'name', 'cantidad_sujetos').order_by('-cantidad_sujetos')

    return render(request, 'paises.html',
                  {'form': addForm(), 'paises': sujetos_por_pais})


def del_pais(request, pais_id):
    pais = get_object_or_404(Pais, id=pais_id)

    if request.method == 'POST':
        pais.delete()
        return redirect('gestionar_paises')

    return render(request, 'del_pais.html', {'pais': pais})


def gestionar_provincias(request, pais_name):
    pais = get_object_or_404(Pais, name=pais_name)

    if request.method == 'POST':
        Provincia.objects.create(
            name=request.POST['name'].upper(),
            pais=pais)
        return redirect('gestionar_provincias', pais_name)

    sujetos_por_provincia = Provincia.objects.filter(pais=pais).annotate(
        cantidad_sujetos=Coalesce(Count('localidad__sujeto'), Value(0))
    ).values('id', 'name', 'cantidad_sujetos').order_by('-cantidad_sujetos')
    print(sujetos_por_provincia)

    return render(request, 'provincias.html',
                  {'form': addForm(),
                   'pais': pais_name,
                   'provincias': sujetos_por_provincia})


def del_provincia(request, pais_name, provincia_id):
    provincia = get_object_or_404(Provincia, id=provincia_id)

    if request.method == 'POST':
        provincia.delete()
        return redirect('gestionar_provincias', pais_name)

    return render(request, 'del_provincia.html', {'pais': pais_name,
                                                  'provincia': provincia})


def gestionar_localidades(request, pais_name, provincia_name):
    pais = get_object_or_404(Pais, name=pais_name)
    provincia = get_object_or_404(
        Provincia, pais=pais, name=provincia_name)
    if request.method == 'POST':
        Localidad.objects.create(
            name=request.POST['name'].upper(),
            provincia=provincia)
        return redirect('gestionar_localidades', pais_name, provincia_name)

    sujetos_por_localidad = Localidad.objects.filter(provincia=provincia)\
        .annotate(cantidad_sujetos=Coalesce(Count('sujeto'), Value(0))
                  ).values('id', 'name', 'cantidad_sujetos')\
        .order_by('-cantidad_sujetos')

    return render(request, 'localidades.html',
                  {'form': addForm(),
                   'pais': pais_name,
                   'provincia': provincia_name,
                   'localidades': sujetos_por_localidad})


def del_localidad(request, pais_name, provincia_name, localidad_id):
    localidad = get_object_or_404(Localidad, id=localidad_id)

    if request.method == 'POST':
        localidad.delete()
        return redirect('gestionar_localidades', pais_name, provincia_name)

    return render(request, 'del_localidad.html', {'pais': pais_name,
                                                  'provincia': provincia_name,
                                                  'localidad': localidad})


def gestionar_localidad(request, pais_name, provincia_name, localidad_name):
    pais = get_object_or_404(Pais, name=pais_name)
    provincia = get_object_or_404(
        Provincia, pais=pais, name=provincia_name)
    localidad = get_object_or_404(Localidad, provincia=provincia,
                                  name=localidad_name)
    if request.method == 'POST':
        Sujeto.objects.create(
            name=request.POST['name'].upper(),
            cuit=request.POST['cuit'],
            address=request.POST['address'].upper(),
            location=localidad,
            iva_id=request.POST['iva_id']
        )
        return redirect('gestionar_localidad', pais_name, provincia_name,
                        localidad_name)

    sujetos_de_localidad = Sujeto.objects.filter(location=localidad)
    return render(request, 'localidad.html',
                  {'form': addSujetoLocalidadForm(),
                   'pais': pais_name,
                   'provincia': provincia_name,
                   'localidad': localidad_name,
                   'sujetos': sujetos_de_localidad})
