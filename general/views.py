from django.shortcuts import render

def inicio(request):
    return render(request, "login.html")

def contenido(request):
    return render(request, "contenido.html")