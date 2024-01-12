from django.urls import path

from .views import gestionar_articulos, del_articulo, gestionar_articulo

urlpatterns = [
    path('', gestionar_articulos, name='gestionar_articulos'),
    path('del_articulo/<int:articulo_id>',
         del_articulo, name='del_articulo'),
    path('<str:articulo_name>', gestionar_articulo, name='gestionar_articulo')
    # ... otras rutas
]
