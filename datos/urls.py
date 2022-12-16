from django.urls import path

from datos.views import crecimiento, crecimientos, socio_economico, socio_economicos, documentacion, documentacions
from usuarios.views import usuarios



urlpatterns = [
    path('crecimiento/',crecimiento,name="crecimiento"),
    path('crecimiento-crear/',crecimientos,name="crecimiento-crear"),
    path('socio-economico/',socio_economico,name="socio-economico"),
    path('socio-economico-crear/',socio_economicos,name="socio-economico-crear"),    
    path('documentacion/',documentacion,name="documentacion"),
    path('documentacion-crear/',documentacions,name="documentacion-crear"),
    #path('programa/',programa,name="programa"),
    #path('programa-beneficiario/<int:pk>/',programa_beneficiarios,name="programa-beneficiarios"),
    
    
]