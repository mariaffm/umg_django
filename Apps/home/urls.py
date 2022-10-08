"""PaginaWeb URL Configuration

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
from PaginaWeb.revista.views import CrearEstudianteView
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from Apps.home import views
from revista.views import CrearArticulosView, principalView
from .views import CrearAdministradorView, CrearPublicacionView, HomeView, ListadoView, StudentsView, AdministratorView, CrearArticulosView, CrearEstudianteView,CrearPublicacionView
from .views import CrearAutorizacionesView, CrearComentariosView, RegistroView, LoginView
app_name ='home'

urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
    path('listado/', ListadoView.as_view(), name='listadoapp'),
    path('students/', StudentsView.as_view(), name='studentsapp'),
    path('administrator/', AdministratorView.as_view(), name='administratorapp'),
    path('principal/', principalView.as_view(), name='principalapp'),
    path('crearArticulo/', CrearArticulosView.as_view(), name='crearArticulo'),
    path('crearEstudiante/',CrearEstudianteView.as_view(), name='crearEstudiante'),
    path('crearAdministrador/',CrearAdministradorView.as_view(), name='crearAdministrador'),
    path('crearPublicacion/', CrearPublicacionView.as_view(), name='crearPublicacion'),
    path('crearAutorizaciones/',CrearAutorizacionesView.as_view(), name= 'crearAutorizaciones'),
    path('crearComentarios/',CrearComentariosView.as_view(), name= 'crearComentarios'),
    path('registro/',RegistroView.as_view(), name= 'registro'),
     path('login/',LoginView.as_view(), name= 'login')
    
]