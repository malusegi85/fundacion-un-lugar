"""general URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, include, re_path

from general.views import inicio, contenido, pagina404, pagina500, reload, ayuda, politica
from general import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio , name="inicio"),
    path('contenido', contenido , name="contenido"),
    path('pagina404', pagina404 , name="pagina404"),
    path('pagina500', pagina500 , name="pagina500"),
    path('ayuda', ayuda , name="ayuda"),
    path('reload', reload , name="reload"),
    path('politica', politica , name="politica"),
    path('usuarios/',include("usuarios.urls")),  
    path('datos/',include("datos.urls")),  

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT,
    })
]