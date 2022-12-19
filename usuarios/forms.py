from django.forms import ModelForm, widgets
from usuarios.models import Beneficiario,Acudiente,Padrino_Beneficiario,Padrino,Referencia
from django.utils.translation import gettext_lazy as _


class BeneficiarioForm(ModelForm):
    class Meta:
        model=Beneficiario
        exclude=['estado']
        widgets={
            'fechaNacimiento': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d')
        }


class AcudienteForm(ModelForm):
    class Meta:
        model=Acudiente
        exclude=['estado']

class PadrinoForm(ModelForm):
    class Meta:
        model=Padrino
        exclude=['estado']

class Padrino_BeneficiarioForm(ModelForm):
    class Meta:
        model=Padrino_Beneficiario
        exclude=['padrino','estado']
        
class ReferenciaForm(ModelForm):
    class Meta:
        model=Referencia
        exclude=['estado']


# PARA EDITAR OBJETOS

class BeneficiarioEditarForm(ModelForm):
    class Meta:
        model=Beneficiario
        exclude=['documento','beneficiario','fechaNacimiento']

class AcudienteEditarForm(ModelForm):
    class Meta:
        model=Acudiente
        exclude=['documento','beneficiario']

class PadrinoEditarForm(ModelForm):
    class Meta:
        model=Padrino
        exclude=['documento']
class Padrino_BeneficiarioForm(ModelForm):
    class Meta:
        model=Padrino_Beneficiario
        exclude=['padrino']
class ReferenciaEditarForm(ModelForm):
    class Meta:
        model=Referencia
        exclude=['documento','beneficiario']

"""comentario"""