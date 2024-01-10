from django.urls import path

from .views import gestionar_remito, del_remito

urlpatterns = [
    path('', gestionar_remito, name='gestionar_remito'),
    path('del_remito/<int:remito_id>', del_remito, name='del_remito'),
    # path('del_articulo/<int:articulo_id>/',
    # del_articulo, name='del_articulo'),
    # ... otras rutas
]
