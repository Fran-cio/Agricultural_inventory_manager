from django.urls import path

from .views import agregar_remito

urlpatterns = [
    path('', agregar_remito, name='agregar_remito'),
    # path('del_articulo/<int:articulo_id>/',
    # del_articulo, name='del_articulo'),
    # ... otras rutas
]
