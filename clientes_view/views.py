from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError

from .models import Localidad, Sujeto
from .forms import SujetoForm
# Create your views here.


def gestionar_sujeto(request):
    if request.method == 'POST':
        try:
            Sujeto.objects.create(
                name=request.POST['name'].upper(),
                cuit=request.POST['cuit'],
                address=request.POST['address'].upper(),
                location=clean_location(request.POST['location']),
                iva_id=request.POST['iva_id']
            )
        except IntegrityError as e:
            print(f'Error de Integridad: {e}')

        except Exception as e:
            print(f'Otro tipo de error: {e}')

        return redirect('gestionar_sujetos')

    sujetos = Sujeto.objects.all()
    return render(request, 'index_u.html',
                  {'form': SujetoForm(), 'sujetos': sujetos})


def clean_location(location_name):
    existing_location = Localidad.objects.filter(name=location_name).first()

    if existing_location:
        return existing_location
    else:
        new_location = Localidad.objects.create(name=location_name.upper())
        return new_location


def del_sujeto(request, sujeto_id):
    sujeto = get_object_or_404(Sujeto, id=sujeto_id)

    if request.method == 'POST':
        sujeto.delete()
        return redirect('gestionar_sujetos')

    return render(request, 'del_sujeto.html', {'sujeto': sujeto})
