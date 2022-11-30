from django.contrib import admin

from usuarios.models import Beneficiario,Acudiente,Padrino,Referencia

# Register your models here.
admin.site.register(Beneficiario)
admin.site.register(Acudiente)
admin.site.register(Padrino)
admin.site.register(Referencia)

