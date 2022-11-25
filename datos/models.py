from django.db import models
from usuarios.models import Beneficiario
from django.utils.translation import gettext_lazy as _

# Create your models here.
#AQUI EMPIEZA LA INFORMACION PERSONAL DEL BENEFICIARIO
class Crecimiento(models.Model):
    estatura= models.CharField(max_length=50, verbose_name="Estatura")    
    peso= models.CharField(max_length=50, verbose_name="Peso")
    enfermedad= models.CharField(max_length=50, verbose_name="Enfermedad")
    discapacidad= models.CharField(max_length=50, verbose_name="Discapacidad")
    eps= models.CharField(max_length=50, verbose_name="EPS")   
    tallaCamisa= models.CharField(max_length=50, verbose_name="Talla camisa")
    tallaPantalon= models.CharField(max_length=50, verbose_name="Talla pantalon ")
    tallaCalzado= models.CharField(max_length=50, verbose_name="Talla de calzado")
    beneficiario= models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")



#AQUI EMPIEZA LA INFORMACION SOCIO ECONOMICA
class Socio_Economico(models.Model):
    oficio= models.CharField(max_length=50, verbose_name="A que se dedica el beneficiario?")
    colegio= models.CharField(max_length=50, verbose_name="Colegio")
    grado= models.CharField(max_length=50, verbose_name="Grado")
    ingresos= models.CharField(max_length=50, verbose_name="Ingresos mensuales del nucleo familiar")
    sisben= models.CharField(max_length=50, verbose_name="Categoria sisben")
    estrato= models.CharField(max_length=50, verbose_name="Estrato")

    viviendaPropia=models.BooleanField(default=False,verbose_name="Tiene Vivienda Propia?")
    servicioLuz=models.BooleanField(default=False,verbose_name="Tiene Servicio de Luz?")
    servicioAgua=models.BooleanField(default=False,verbose_name="Tiene Servicio de Agua?")
    servicioGas=models.BooleanField(default=False,verbose_name="Tiene Servicio de Gas?")
    servicioInternet=models.BooleanField(default=False,verbose_name="Tiene Servicio de Internet?")
    beneficiario= models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    estado= models.BooleanField(default=False,verbose_name="Estado")

class Programa(models.Model):
    nombre= models.CharField(max_length=50, verbose_name="Nombre")
    descripcion= models.CharField(max_length=50, verbose_name="Descripción")
    estado= models.BooleanField(default=False,verbose_name="Estado")

    
#AQUI EMPIEZA LOS PROGRAMAS Y ESTADOS DEL BENEFICIARIO
class Programas_Beneficiario(models.Model):
    
    programas=models.ForeignKey(Programa, on_delete=models.CASCADE, verbose_name="Programa")
    fecha=models.DateField(auto_now=True, verbose_name="Fecha de ingreso", help_text="DD/MM/AA")  
    class EstadoUsuario(models.TextChoices):
        ACTIVO='Activo', _("Activo")
        INACTIVO='Inactivo', _("Inactivo")
        RETIRADO='Retirado', _("Retirado")
    estadoUsuario=models.CharField(max_length=20, choices=EstadoUsuario.choices, default=EstadoUsuario.ACTIVO, verbose_name="Estado del Beneficiario")
    class EstadoCarnet(models.TextChoices):
        HABILITADO='Habilitado', _("Habilitado")
        PENDIENTE='Pendiente', _("Pendiente")
        INHABILITADO='Inhabilitado', _("Inhabilitado")
    estadoCarnet=models.CharField(max_length=20, choices=EstadoCarnet.choices, default=EstadoCarnet.PENDIENTE, verbose_name="Estado del carnet")
    beneficiario= models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    
#AQUI EMPIEZA LOS DOCUMENTOS ADJUNTOS
class Documentacion(models.Model):
    documentoAcudiente=models.FileField(upload_to='uploads/',blank=True, null=True)
    registroCivil=models.FileField(upload_to='uploads/',blank=True, null=True)
    foto=models.FileField(upload_to='uploads/',blank=True, null=True)
    formato=models.FileField(upload_to='uploads/',blank=True, null=True)
    autorizacion=models.FileField(upload_to='uploads/',blank=True, null=True)
    tarjetaIdentidad=models.FileField(upload_to='uploads/',blank=True, null=True)
    carnet=models.FileField(upload_to='uploads/',blank=True, null=True)
    factura=models.FileField(upload_to='uploads/',blank=True, null=True)
    beneficiario= models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")





    
