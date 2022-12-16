from django.forms import ModelForm, widgets
from datos.models import Crecimiento,Socio_Economico,Programas_Beneficiario,Documentacion


class CrecimientoForm(ModelForm):
    class Meta:
        model=Crecimiento
        exclude=['beneficiario']

class Socio_EconomicoForm(ModelForm):
    class Meta:
        model=Socio_Economico
        exclude=['estado','beneficiario']
  

class Programas_BeneficiarioForm(ModelForm):
    class Meta:
        model=Programas_Beneficiario
        exclude=['estadoUsuario','estadoCarnet','beneficiario']

class DocumentacionForm(ModelForm):
    class Meta:
        model=Documentacion
        exclude=['beneficiario']

# PARA EDITAR OBJETOS

class CrecimientoEditarForm(ModelForm):
    class Meta:
        model=Crecimiento
        exclude=['beneficiario']

class Socio_EconomicoEditarForm(ModelForm):
    class Meta:
        model=Socio_Economico
        exclude=['beneficiario']
    

class Programas_BeneficiarioEditarForm(ModelForm):
    class Meta:
        model=Programas_Beneficiario
        exclude=['beneficiario']

