from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

#DATOS BASICOS DEL BENEFICIARIO
class Beneficiario(models.Model):
    documento=models.CharField(unique=True, max_length=20,verbose_name="Número de Documento")
    class TipoDocumento(models.TextChoices):
        TI='T.I.', _("Tarjeta de Identidad")
        RC='R.C.', _("Registro Civil")
        CE='C.E.', _("Cédula de Extranjería")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices, default=TipoDocumento.TI, verbose_name="Tipo de Documento")    
    nombres= models.CharField(max_length=50, verbose_name="Nombres")
    apellidos= models.CharField(max_length=50, verbose_name="Apellidos")
    extranjero= models.BooleanField(default=False,verbose_name="Es extranjero?")
    class TipoSangre(models.TextChoices):
        AP='A+', _("A+")    
        AN='A-', _("A-")
        BP='B+', _("B+")
        BN='B-', _("B-")
        ABP='AB+', _("AB+")
        ABN='AB-', _("AB-")
        OP='O+', _("O+")
        ON='O-', _("O-")
    tipoSangre=models.CharField(max_length=5, choices=TipoSangre.choices, verbose_name="Tipo de Documento") 
    class Genero(models.TextChoices):
        MASCULINO='Masculino', _("Masculino")
        FEMENINO='Femenino', _("Femenino")
    genero=models.CharField(max_length=15, choices=Genero.choices, verbose_name="Género")   
    fechaNacimiento=models.DateField(verbose_name="Fecha de nacimiento", help_text="DD/MM/AA")
    lugarNacimiento= models.CharField(max_length=50, verbose_name="Lugar de Nacimiento")

    localidad= models.CharField(max_length=50, verbose_name="Localidad")
    barrio= models.CharField(max_length=50, verbose_name="Barrio")
    direccion= models.CharField(max_length=50, verbose_name="Dirección")
    telefono= models.CharField(max_length=50, verbose_name="Teléfono")
    telefonoSecundario= models.CharField(max_length=50,blank=True,null=True, verbose_name="Teléfono secundario")   
    estado= models.BooleanField(default=False,verbose_name="Estado")
    
#AQUI EMPIEZA LOS DATOS DEL ACUDIENTE DEL BENEFICIARIO
class Acudiente(models.Model):
    documento=models.CharField(unique=True, max_length=20,verbose_name="Número de Documento")
    class TipoDocumento(models.TextChoices):
        TI='T.I.', _("Tarjeta de Identidad")
        RC='R.C.', _("Registro Civil")
        CE='C.E.', _("Cédula de Extranjería")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices, default=TipoDocumento.TI, verbose_name="Tipo de Documento")    
    nombres= models.CharField(max_length=50, verbose_name="Nombres")
    apellidos= models.CharField(max_length=50, verbose_name="Apellidos")
    parentesco= models.CharField(max_length=50, verbose_name="Parentesco")
    ocupacion= models.CharField(max_length=50, verbose_name="Ocupación")
    telefono= models.CharField(max_length=50, verbose_name="Teléfono")
    beneficiario= models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    estado= models.BooleanField(default=False,verbose_name="Estado")

#AQUI EMPIEZA LOS DATOS DEL PADRINO
class Padrino(models.Model): 
    documento=models.CharField(unique=True, max_length=20,verbose_name="Número de Documento")
    class TipoDocumento(models.TextChoices):
        TI='T.I.', _("Tarjeta de Identidad")
        RC='R.C.', _("Registro Civil")
        CE='C.E.', _("Cédula de Extranjería")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices, default=TipoDocumento.TI, verbose_name="Tipo de Documento")    
    nombres= models.CharField(max_length=50, verbose_name="Nombres")
    apellidos= models.CharField(max_length=50, verbose_name="Apellidos")
    telefono= models.CharField(max_length=50, verbose_name="Teléfono")
    correo= models.EmailField(max_length=50, verbose_name="Correo electrónico") 
    estado= models.BooleanField(default=False,verbose_name="Estado")
class Padrino_Beneficiario(models.Model):
    beneficiario= models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    padrino= models.ForeignKey(Padrino, on_delete=models.CASCADE, verbose_name="Padrino")
    estado= models.BooleanField(default=False,verbose_name="Estado")

#AQUI EMPIEZA LA REFERENCIA PERSONAL
class Referencia(models.Model):
    documento=models.CharField(unique=True, max_length=20,verbose_name="Número de Documento")
    class TipoDocumento(models.TextChoices):
        TI='T.I.', _("Tarjeta de Identidad")
        RC='R.C.', _("Registro Civil")
        CE='C.E.', _("Cédula de Extranjería")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices, default=TipoDocumento.TI, verbose_name="Tipo de Documento")    
    nombres= models.CharField(max_length=50, verbose_name="Nombres")
    apellidos= models.CharField(max_length=50, verbose_name="Apellidos")
    ocupacion= models.CharField(max_length=50, verbose_name="Ocupación")
    relacion= models.CharField(max_length=50, verbose_name="Relación")
    telefono= models.CharField(max_length=50, verbose_name="Teléfono")
    class TipoReferencia(models.TextChoices):
        PER='T.I.', _("Personal")
        FAM='R.C.', _("Familiar")
    tipoReferencia=models.CharField(max_length=5, choices=TipoReferencia.choices, verbose_name="Tipo de Referencia")
    beneficiario= models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    estado= models.BooleanField(default=False,verbose_name="Estado")

