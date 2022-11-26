from django.shortcuts import render,redirect
from datos.forms import CrecimientoForm,Socio_EconomicoForm
from datos.models import Crecimiento,Socio_Economico
from usuarios.models import Beneficiario
# Create your views here.


def crecimiento(request):
    titulo="Crecimientos"
    crecimientos=Crecimiento.objects.all()
    context={
        'titulo':titulo,
        'crecimientos':crecimientos
    }
    return render(request, 'datos/crecimiento.html')
    
def crecimiento_crear(request,pk):
    beneficiario= Beneficiario.objects.get(id=pk)
    titulo=f"Crecimiento de {beneficiario.nombres} {beneficiario.apellidos}"
    if request.method=='POST':
        form= CrecimientoForm(reques.POST)
        if form.is_valid():
            aux=form.save(commit=false)
            aux.beneficiario=beneficiario
            aux.save()
            return redirect('crecimientos')
        else:
            form= CrecimientoForm(request.POST)
    else:
            form= CrecimientoForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request, 'datos/crear.html',context)

    
def socio_economico(request):
    titulo="Datos socio-economicos"
    socio_economicos=Socio_Economico.objects.all()
    context={
        'titulo':titulo,
        'socio_economicos':socio_economicos
    }
    return render(request, 'datos/socio_economicos.html')
    
def socio_economico_crear(request,pk):
    beneficiario= Beneficiario.objects.get(id=pk)
    titulo=f"Datos Socio-economicos de {beneficiario.nombres} {beneficiario.apellidos}"
    if request.method=='POST':
        form= Socio_EconomicoForm(reques.POST)
        if form.is_valid():
            aux=form.save(commit=false)
            aux.beneficiario=beneficiario
            aux.save()
            return redirect('socio-economicos')
        else:
            form= Socio_EconomicoForm(request.POST)
    else:
            form= Socio_EconomicoForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request, 'datos/crear.html',context)

