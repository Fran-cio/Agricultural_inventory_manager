from django.shortcuts import render, redirect, get_object_or_404

from .models import Pais, Provincia, Localidad
from .forms import addForm
# Create your views here.


def gestionar_paises(request):
    if request.method == 'POST':
        Pais.objects.create(
            name=request.POST['name'].upper())
        return redirect('gestionar_paises')

    paises = Pais.objects.all()
    return render(request, 'paises.html',
                  {'form': addForm(), 'paises': paises})


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

    provincias = Provincia.objects.filter(pais=pais)
    return render(request, 'provincias.html',
                  {'form': addForm(),
                   'pais': pais_name,
                   'provincias': provincias})


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
    print(provincia)
    if request.method == 'POST':
        Localidad.objects.create(
            name=request.POST['name'].upper(),
            provincia=provincia)
        return redirect('gestionar_localidades', pais_name, provincia_name)

    localidades = Localidad.objects.filter(provincia=provincia)
    return render(request, 'localidades.html',
                  {'form': addForm(),
                   'pais': pais_name,
                   'provincia': provincia_name,
                   'localidades': localidades})


def del_localidad(request, pais_name, provincia_name, localidad_id):
    localidad = get_object_or_404(Localidad, id=localidad_id)

    if request.method == 'POST':
        localidad.delete()
        return redirect('gestionar_localidades', pais_name, provincia_name)

    return render(request, 'del_localidad.html', {'pais': pais_name,
                                                  'provincia': provincia_name,
                                                  'localidad': localidad})
