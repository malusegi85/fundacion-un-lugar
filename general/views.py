from django.shortcuts import render

def inicio(request):
    return render(request, "login.html")

def contenido(request):
    return render(request, "contenido.html")

def pagina404(request):
    return render(request, "pagina404.html")

def pagina500(request):
    return render(request, "pagina500.html")

def reload(request):
    return render(request, "reload.html")

def ayuda(request):
    return render(request, "ayuda.html")

def politica(request):
    return render(request, "politica.html")