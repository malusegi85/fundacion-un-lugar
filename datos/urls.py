from django.urls import path

from datos.views import crecimiento,crecimiento_crear,socio_economico,socio_economico_crear
from usuarios.views import usuarios



urlpatterns = [
    path('crecimiento/<int:pk>/',crecimiento_crear,name="crecimientos-c"),
    path('crecimientos/',crecimiento,name="crecimientos"),

    path('socio-economico/<int:pk>/',socio_economico_crear,name="socio-economicos-c"),
    path('socio-economicos/',socio_economico,name="socio-economicos"),

    # path('programa/',programa,name="programa"),
    # path('programa-beneficiario/<int:pk>/',programa_beneficiarios,name="programa-beneficiarios"),
    # path('documentacion/<int:pk>/',documentacion,name="documentacion"),
    
]