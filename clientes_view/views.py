from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError

from .models import Localidad, Sujeto
from .forms import SujetoForm
# Create your views here.


def gestionar_sujeto(request):
    sujetos = Sujeto.objects.all()
    return render(request, 'index_u.html',
                  {'form': SujetoForm(), 'sujetos': sujetos})


def del_sujeto(request, sujeto_id):
    sujeto = get_object_or_404(Sujeto, id=sujeto_id)

    if request.method == 'POST':
        sujeto.delete()
        return redirect('gestionar_sujetos')

    return render(request, 'del_sujeto.html', {'sujeto': sujeto})
