
# pylint: disable=line-too-long
from django.urls import path

from .views import gestionar_paises, del_pais, gestionar_provincias, \
    del_provincia, gestionar_localidades, del_localidad, gestionar_localidad

urlpatterns = [
    path('', gestionar_paises, name='gestionar_paises'),
    path('del_pais/<int:pais_id>/', del_pais, name='del_pais'),
    path('<str:pais_name>/',
         gestionar_provincias, name='gestionar_provincias'),
    path('<str:pais_name>/del_provincia/<int:provincia_id>',
         del_provincia, name='del_provincia'),
    path('<str:pais_name>/<str:provincia_name>/',
         gestionar_localidades, name='gestionar_localidades'),
    path(
        '<str:pais_name>/<str:provincia_name>/del_localidad/<int:localidad_id>', del_localidad, name='del_localidad'),
    path('<str:pais_name>/<str:provincia_name>/<str:localidad_name>',
         gestionar_localidad, name='gestionar_localidad'),
    # ... otras rutas
]
