from django.urls import path

from .views import gestionar_sujetos, del_sujeto, gestionar_sujeto

urlpatterns = [
    path('', gestionar_sujetos, name='gestionar_sujetos'),
    path('del_sujeto/<int:sujeto_id>/', del_sujeto, name='del_sujeto'),
    path('<int:cuit>', gestionar_sujeto, name='gestionar_sujeto')
    # ... otras rutas
]
