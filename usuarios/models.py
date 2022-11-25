from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

#DATOS BASICOS DEL BENEFICIARIO
class DatosBasicos(models.Model):
    identificacion=models.CharField(unique=True, max_length=20)
    class TipoDocumento(models.TextChoices):
        TI='T.I.', _("Tarjeta de Identidad")
        RC='R.C.', _("Registro Civil")
        CE='C.E.', _("Cédula de Extranjería")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices, default=TipoDocumento.TI, verbose_name="Tipo de Documento")    
    nombresBeneficario= models.CharField(max_length=50, verbose_name="Nombres")
    apellidosBeneficiario= models.CharField(max_length=50, verbose_name="Apellidos")
    InformacionPersonal=models.ForeignKey("InformacionPersonal",models.DO_NOTHING)
    DatosContactoBeneficiario=models.ForeignKey("DatosContactoBeneficiario",models.DO_NOTHING)
    DatosAcudiente=models.ForeignKey("DatosAcudiente",models.DO_NOTHING)
    DatosPadrino=models.ForeignKey("DatosPadrino",models.DO_NOTHING)
    ReferenciaPersonal=models.ForeignKey("ReferenciaPersonal",models.DO_NOTHING)
    ReferenciaFamiliar=models.ForeignKey("ReferenciaFamiliar",models.DO_NOTHING)
    InformacionSocio=models.ForeignKey("InformacionSocio",models.DO_NOTHING)
    ProgramasEstados=models.ForeignKey("ProgramasEstados",models.DO_NOTHING)
    AdjuntosBeneficiario=models.ForeignKey("AdjuntosBeneficiario",models.DO_NOTHING,blank=True, null=True)
    
    nacionalidad= models.CharField(max_length=50, verbose_name="Nacionalidad")
    tipoSangre= models.CharField(max_length=50, verbose_name="Tipo de sangre")
    class EstadoCivil(models.TextChoices):
        SOLTERO='Soltero', _("Soltero")
        CASADO='Casado', _("Casado")
        UNIONLIBRE='Union Libre', _("Union Libre")
    estadoCivil=models.CharField(max_length=20, choices=EstadoCivil.choices, default=EstadoCivil.SOLTERO, verbose_name="Estado Civil")
    edad= models.CharField(max_length=50, verbose_name="Edad")
    fechaNacimiento=models.DateField(verbose_name="Fecha de nacimiento", help_text="DD/MM/AA")
    lugarNacimiento= models.CharField(max_length=50, verbose_name="Lugar de nacimiento")
    class Genero(models.TextChoices):
        MASCULINO='Masculino', _("Masculino")
        FEMENINO='Femenino', _("Femenino")
    genero=models.CharField(max_length=15, choices=Genero.choices, default=Genero.MASCULINO, verbose_name="Genero")
#AQUI EMPIEZA LA INFORMACION PERSONAL DEL BENEFICIARIO
class InformacionPersonal(models.Model):
    estatura= models.CharField(max_length=50, verbose_name="Estatura")    
    peso= models.CharField(max_length=50, verbose_name="Peso")
    enfermedad= models.CharField(max_length=50, verbose_name="Enfermedad")
    discapacidad= models.CharField(max_length=50, verbose_name="Discapacidad")
    eps= models.CharField(max_length=50, verbose_name="EPS")   
    tallaCamisa= models.CharField(max_length=50, verbose_name="Talla camisa")
    tallaPantalon= models.CharField(max_length=50, verbose_name="Talla pantalon ")
    tallaCalzado= models.CharField(max_length=50, verbose_name="Talla de calzado")
#AQUI EMPIEZA LOS DATOS DE CONTACTO DEL BENEFICIARIO
class DatosContactoBeneficiario(models.Model):
    departamento= models.CharField(max_length=50, verbose_name="Departamento")
    lugarResidencia= models.CharField(max_length=50, verbose_name="Lugar de residencia")
    localidad= models.CharField(max_length=50, verbose_name="Localidad")
    barrio= models.CharField(max_length=50, verbose_name="Barrio")
    direccion= models.CharField(max_length=50, verbose_name="Direccion")
    ubicacion= models.CharField(max_length=50, verbose_name="Ubicacion")
    celular= models.CharField(max_length=50, verbose_name="Celular")
    telefonoSecundario= models.CharField(max_length=50, verbose_name="Telefono secundario")   
    telefonoFijo= models.CharField(max_length=50, verbose_name="Telefono fijo")   
#AQUI EMPIEZA LOS DATOS DEL ACUDIENTE DEL BENEFICIARIO
class DatosAcudiente(models.Model):
    identificacionAcudiente= models.CharField(max_length=50, verbose_name="Documento de identidad")
    nombresAcudiente= models.CharField(max_length=50, verbose_name="Nombres")
    apellidosAcudiente= models.CharField(max_length=50, verbose_name="Apellidos")
    parentescoAcudiente= models.CharField(max_length=50, verbose_name="Parentesco")
    ocupacionAcudiente= models.CharField(max_length=50, verbose_name="Ocupacion")
    telefonoAcudiente= models.CharField(max_length=50, verbose_name="Telefono")
#AQUI EMPIEZA LOS DATOS DEL PADRINO
class DatosPadrino(models.Model): 
    nombresPadrino= models.CharField(max_length=50, verbose_name="Nombres")
    apellidosPadrino= models.CharField(max_length=50, verbose_name="Apellidos")
    identificacionPadrino= models.CharField(max_length=50, verbose_name="Documento de identidad")
    telefonoPadrino= models.CharField(max_length=50, verbose_name="Telefono fijo")
    celularPadrino= models.CharField(max_length=50, verbose_name="Celular")
    correoPadrino= models.CharField(max_length=50, verbose_name="Correo electronico") 
#AQUI EMPIEZA LA REFERENCIA PERSONAL
class ReferenciaPersonal(models.Model):
    nombresPersonal= models.CharField(max_length=50, verbose_name="Nombres")
    apellidosPersonal= models.CharField(max_length=50, verbose_name="Apellidos") 
    identificacionPersonal= models.CharField(max_length=50, verbose_name="Identificacion")
    ocupacionPersonal= models.CharField(max_length=50, verbose_name="Ocupacion")     
    telefonoPersonal= models.CharField(max_length=50, verbose_name="Telefono")
#AQUI EMPIEZA LA REFERENCIA FAMILIAR 
class ReferenciaFamiliar(models.Model):
    nombresFamiliar= models.CharField(max_length=50, verbose_name="Nombres del familiar")
    apellidosFamiliar= models.CharField(max_length=50, verbose_name="Apellidos del familiar")
    identificacionfamiliar= models.CharField(max_length=50, verbose_name="Identificacion")
    ocupacionfamiliar= models.CharField(max_length=50, verbose_name="Ocupacion")
    parentescoFamiliar= models.CharField(max_length=50, verbose_name="Parentesco")
    telefonoFamiliar= models.CharField(max_length=50, verbose_name="Telefono fijo")
#AQUI EMPIEZA LA INFORMACION SOCIO ECONOMICA
class InformacionSocio(models.Model):
    dedica= models.CharField(max_length=50, verbose_name="A que se dedica el beneficiario?")
    colegio= models.CharField(max_length=50, verbose_name="Colegio")
    grado= models.CharField(max_length=50, verbose_name="Grado")
    ingresosMensuales= models.CharField(max_length=50, verbose_name="Ingresos mensuales del nucleo familiar")
    sisben= models.CharField(max_length=50, verbose_name="Categoria sisben")
    estrato= models.CharField(max_length=50, verbose_name="Estrato")
    class ViviendaPropia(models.TextChoices):
        SI='Si', _("Si")
        NO='No', _("No")
    viviendaPropia=models.CharField(max_length=15, choices=ViviendaPropia.choices, default=ViviendaPropia.SI, verbose_name="Vivienda Propia")
    class ServicioPublico(models.TextChoices):
        SI='Si', _("Si")
        NO='No', _("No")
    servicioPublico=models.CharField(max_length=15, choices=ServicioPublico.choices, default=ServicioPublico.SI, verbose_name="Servicios públicos")
    class ServicioInternet(models.TextChoices):
        SI='Si', _("Si")
        NO='No', _("No")
    servicioInternet=models.CharField(max_length=15, choices=ServicioInternet.choices, default=ServicioInternet.SI, verbose_name="Servicio de internet")
#AQUI EMPIEZA LOS PROGRAMAS Y ESTADOS DEL BENEFICIARIO
class ProgramasEstados(models.Model):
    class Programas(models.TextChoices):
        ALIMENTARTE='Alimentarte', _("Alimentarte")
        FORMARTE='Formarte', _("Formarte")
        IMPULSARTE='Impulsarte', _("Impulsarte")
        BIENESTAR='Bienestar', _("Bienestar")
        CUIDARTE='Cuidarte', _("Cuidarte")
    programas=models.CharField(max_length=20, choices=Programas.choices, default=Programas.ALIMENTARTE, verbose_name="Programas")
    fechaInicial=models.DateField(verbose_name="Fecha inicial", help_text="DD/MM/AA")  
    class EstadoUsuario(models.TextChoices):
        ACTIVO='Activo', _("Activo")
        INACTIVO='Inactivo', _("Inactivo")
        RETIRADO='Retirado', _("Retirado")
    estadoUsuario=models.CharField(max_length=20, choices=EstadoUsuario.choices, default=EstadoUsuario.ACTIVO, verbose_name="Estado del beneficiario")
    class EstadoCarnet(models.TextChoices):
        HABILITADO='Habilitado', _("Habilitado")
        PENDIENTE='Pendiente', _("Pendiente")
        INHABILITADO='Inhabilitado', _("Inhabilitado")
    estadoCarnet=models.CharField(max_length=20, choices=EstadoCarnet.choices, default=EstadoCarnet.HABILITADO, verbose_name="Estado del carnet")
#AQUI EMPIEZA LOS DOCUMENTOS ADJUNTOS
class AdjuntosBeneficiario(models.Model):
    documentoAcudiente=models.FileField(upload_to='uploads/',blank=True, null=True)
    registroCivil=models.FileField(upload_to='uploads/',blank=True, null=True)
    fotoBeneficiario=models.FileField(upload_to='uploads/',blank=True, null=True)
    formato=models.FileField(upload_to='uploads/',blank=True, null=True)
    autorizacion=models.FileField(upload_to='uploads/',blank=True, null=True)
    tarjetaIdentidad=models.FileField(upload_to='uploads/',blank=True, null=True)
    carnet=models.FileField(upload_to='uploads/',blank=True, null=True)
    factura=models.FileField(upload_to='uploads/',blank=True, null=True)




    
