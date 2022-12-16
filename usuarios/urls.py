from django.urls import path

from usuarios.views import beneficiario, usuarios, acudiente, acudientes, padrino, padrinos, referencia, referencias



urlpatterns = [
    path('beneficiario/',beneficiario,name="beneficiario"),
    path('beneficiario-crear/',usuarios,name="beneficiario-crear"),
    path('acudiente/',acudiente,name="acudiente"),
    path('acudiente-crear/',acudientes,name="acudiente-crear"),
    path('padrino/',padrino,name="padrino"),
    path('padrino-crear/',padrinos,name="padrino-crear"),
    path('referencia/',referencia,name="referencia"),
    path('referencia-crear/',referencias,name="referencia-crear"),
    # path('padrino-beneficiario/<int:pk_pad>',padrino_beneficiario,name="padrinos"),
    
]
    
