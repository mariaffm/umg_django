from django.shortcuts import render
from django.views.generic import TemplateView
from revista.views import CrearArticulosView

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class ListadoView(TemplateView):
    template_name='listado.html'

class StudentsView(TemplateView):
    template_name='students.html'
    
class AdministratorView(TemplateView):
    template_name='administrator.html'

class CrearArticulosView(TemplateView):
    template_name='crearArticulo.html'
    
    

