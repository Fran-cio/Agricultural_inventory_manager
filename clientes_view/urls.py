from django.urls import path

from .views import gestionar_sujeto, del_sujeto

urlpatterns = [
    path('', gestionar_sujeto, name='gestionar_sujetos'),
    path('del_sujeto/<int:sujeto_id>/', del_sujeto, name='del_sujeto'),
    # ... otras rutas
]
