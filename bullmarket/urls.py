from django.urls import path, include

from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('articulos/', include("articulo_view.urls"), name="articulos"),
    path('clientes/', include("clientes_view.urls"), name="clientes"),
    path('pais/', include("location_view.urls"), name="pais"),
    path('remitos/', include("remito_view.urls"), name="remitos"),
]
