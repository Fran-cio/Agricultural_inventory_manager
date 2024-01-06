from django.shortcuts import render, redirect, get_object_or_404

from .models import Articulo, Unity_cat
from .forms import ArticuloForm
# Create your views here.


def gestionar_articulos(request):
    if request.method == 'POST':
        Articulo.objects.create(
            name=request.POST['name'], unity_id=request.POST['unity_id'])
        return redirect('gestionar_articulos')

    articulos = Articulo.objects.all()
    return render(request, 'index.html',
                  {'form': ArticuloForm(), 'articulos': articulos})


def del_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    if request.method == 'POST':
        articulo.delete()
        return redirect('gestionar_articulos')

    return render(request, 'del_articulo.html', {'articulo': articulo})
