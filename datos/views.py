from django.shortcuts import render,redirect
from datos.forms import CrecimientoForm,Socio_EconomicoForm,DocumentacionForm
from datos.models import Crecimiento,Socio_Economico,Programa,Documentacion
from usuarios.models import Beneficiario
# Create your views here.


def crecimiento(request):
    crecimientos=Crecimiento.objects.all()
    context={
        'crecimientos':crecimientos
    }
    return render(request, "datos/crecimiento.html", context)
    
def crecimientos(request):
    if request.method == 'POST':
        form=CrecimientoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("el crecimiento no se guardo")
    else:
        form=CrecimientoForm()
    context={
        'form':form
    }
    return render(request, "datos/crecimiento-crear.html", context)

def socio_economico(request):
    socio_economicos=Socio_Economico.objects.all()
    context={
        'socio_economicos':socio_economicos
    }
    return render(request, 'datos/socio-economico.html', context)
    
def socio_economicos(request):    
    if request.method=='POST':
        form=Socio_EconomicoForm(request.POST)
        if form.is_valid():
            form.save()           
        else:
            print("el socio_economico no se guardo")
    else:
        form= Socio_EconomicoForm()
    context={        
        'form':form
    }
    return render(request, 'datos/socio-economico-crear.html', context)

def programa(request):
    programas=Programa.objects.all()
    context={        
        'programas':programas
    }
    return render(request, 'datos/programas.html',context)

def documentacion(request):
    documentacions=Documentacion.objects.all()
    context={
        'documentacions':documentacions
    }
    return render(request, "datos/documentacion.html", context)

def documentacions(request):
    if request.method == 'POST':
        form=DocumentacionForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("el documento no se guardo")
    else:
        form=DocumentacionForm()
    context={
        'form':form
    }
    return render(request, "datos/documentacion-crear.html", context)

