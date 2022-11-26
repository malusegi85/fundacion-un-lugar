from django.forms import ModelForm, widgets
from datos.models import Crecimiento,Socio_Economico,Programa,Programas_Beneficiario,Documentacion


class CrecimientoForm(ModelForm):
    class Meta:
        model=Crecimiento
        exclude=['beneficiario']

class Socio_EconomicoForm(ModelForm):
    class Meta:
        model=Socio_Economico
        exclude=['estado','beneficiario']

class ProgramaForm(ModelForm):
    class Meta:
        model=Programa
        exclude=['estado']       

class Programas_BeneficiarioForm(ModelForm):
    class Meta:
        model=Programas_Beneficiario
        exclude=['estadoUsuario','estadoCarnet','beneficiario']

class DocumentacionForm(ModelForm):
    class Meta:
        model=Documentacion
        exclude=['beneficiario']



class Socio_EconomicoEditarForm(ModelForm):
    class Meta:
        model=Socio_Economico
        exclude=['beneficiario']

class ProgramaEditarForm(ModelForm):
    class Meta:
        model=Programa
        fields='__all__'      

class Programas_BeneficiarioEditarForm(ModelForm):
    class Meta:
        model=Programas_Beneficiario
        exclude=['beneficiario']

