from django.shortcuts import render
from usuarios.forms import BeneficiarioForm, AcudienteForm, PadrinoForm, ReferenciaForm
from usuarios.models import Beneficiario, Acudiente, Padrino, Referencia
# Create your views here.

def beneficiario(request):
    beneficiarios= Beneficiario.objects.all()
    context={
        'beneficiarios':beneficiarios
    }
    return render(request, "usuarios/beneficiario.html", context)


def usuarios(request):
    if request.method == 'POST':
        form=BeneficiarioForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("el beneficiario no se guardo")
    else:
        form=BeneficiarioForm()
    context={
        'form':form
    }
    return render(request, "usuarios/beneficiario-crear.html", context)

def acudiente(request):
    acudientes= Acudiente.objects.all()
    context={
        'acudientes':acudientes
    }
    return render(request, "usuarios/acudiente.html", context)

def acudientes(request):
    if request.method == 'POST':
        form=AcudienteForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("el acudiente no se guardo")
    else:
        form=AcudienteForm()
    context={
        'form':form
    }
    return render(request, "usuarios/acudiente-crear.html", context)

def padrino(request):
    padrinos= Padrino.objects.all()
    context={
        'padrinos':padrinos
    }
    return render(request, "usuarios/padrino.html", context)

def padrinos(request):
    if request.method == 'POST':
        form=PadrinoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("el padrino no se guardo")
    else:
        form=PadrinoForm()
    context={
        'form':form
    }
    return render(request, "usuarios/padrino-crear.html", context)


def referencia(request):
    referencias= Referencia.objects.all()
    context={
        'referencias':referencias
    }
    return render(request, "usuarios/referencia.html", context)

def referencias(request):
    if request.method == 'POST':
        form=ReferenciaForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("la referencia no se guardo")
    else:
        form=ReferenciaForm()
    context={
        'form':form
    }
    return render(request, "usuarios/referencia-crear.html", context)



