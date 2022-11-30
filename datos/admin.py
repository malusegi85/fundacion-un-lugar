from django.contrib import admin

from datos.models import Crecimiento,Socio_Economico,Programa,Documentacion

# Register your models here.
admin.site.register(Crecimiento)
admin.site.register(Socio_Economico)
admin.site.register(Programa)
admin.site.register(Documentacion)


