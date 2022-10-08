from io import UnsupportedOperation
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from revista.models import Usuario

from revista.forms import ArticuloForm, EstudianteForm, AdministradorForm,PublicacionesForm, AutorizacionesForm, ComentariosForm, RegistroForm
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView


#INICIALIZAR LOS VIEWS
# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class ListadoView(TemplateView):
    template_name='listado.html'

class StudentsView(TemplateView):
    template_name='students.html'
    
class AdministratorView(TemplateView):
    template_name='administrator.html'

class CrearArticulosView(CreateView):
  template_name= 'crearArticulo.html'
  form_class= ArticuloForm
  success_url = reverse_lazy('home:homeapp')

class CrearEstudianteView(CreateView):
    template_name= 'crearEstudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('home:studentsapp')

class CrearAdministradorView(CreateView):
    template_name= 'crearAdministrador.html'
    form_class = AdministradorForm
    success_url = reverse_lazy('home:studentsapp')

class CrearPublicacionView(CreateView):
    template_name= 'crearPublicacion.html'
    form_class= PublicacionesForm
    success_url = reverse_lazy('home:homeapp')

class CrearAutorizacionesView(CreateView):
    template_name= 'crearAutorizaciones.html'
    form_class = AutorizacionesForm
    success_url = reverse_lazy('home:homeapp')

class CrearComentariosView(CreateView):
    template_name= 'crearComentarios.html'
    form_class = ComentariosForm
    success_url = reverse_lazy('home:homeapp')

class RegistroView(CreateView):
    model= Usuario 
    form_class = RegistroForm
    success_url = reverse_lazy('home:homeapp')

class LoginView(LoginView):
    template_name = 'login.html'
