from django.urls import path

from .views import gestionar_remito, del_remito, \
    gestionar_transacciones, del_transaccion

urlpatterns = [
    path('', gestionar_remito, name='gestionar_remito'),
    path('del_remito/<int:remito_id>', del_remito, name='del_remito'),
    path('<int:nro_remito>', gestionar_transacciones,
         name='gestionar_transacciones'),
    path('<int:nro_remito>/del_transaccion/<int:transaccion_id>',
         del_transaccion, name='del_transaccion'),
    # path('del_articulo/<int:articulo_id>/',
    # del_articulo, name='del_articulo'),
    # ... otras rutas
]
