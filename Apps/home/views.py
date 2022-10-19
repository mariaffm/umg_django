from io import UnsupportedOperation
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from revista.models import Usuario, Estududiantes, Administradores,Publicaciones, Autorizaciones, Articulos, Comentarios
from revista.forms import ArticuloForm, EstudianteForm, AdministradorForm,PublicacionesForm, AutorizacionesForm, ComentariosForm, RegistroForm
from django.urls import reverse_lazy
from .models import Estudiante

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
  success_url = reverse_lazy('home:listadoart')

class CrearEstudianteView(CreateView):
    template_name= 'crearEstudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('home:listadoest')

class CrearAdministradorView(CreateView):
    template_name= 'crearAdministrador.html'
    form_class = AdministradorForm
    success_url = reverse_lazy('home:listadoadm')

class CrearPublicacionView(CreateView):
    template_name= 'crearPublicacion.html'
    form_class= PublicacionesForm
    success_url = reverse_lazy('home:listadopubl')

class CrearAutorizacionesView(CreateView):
    template_name= 'crearAutorizaciones.html'
    form_class = AutorizacionesForm
    success_url = reverse_lazy('home:listadoaut')

class CrearComentariosView(CreateView):
    template_name= 'crearComentarios.html'
    form_class = ComentariosForm
    success_url = reverse_lazy('home:listadocom')

class RegistroView(CreateView):
    model= Usuario 
    form_class = RegistroForm
    success_url = reverse_lazy('home:homeapp')

class LoginView(LoginView):
    template_name = 'login.html'

class ListarEstudianteView (ListView):
    template_name = 'listarEstudiantes.html'
    model = Estududiantes

    def get_query(self):
        return Estudiante.objects.all()

class ListarAdministradoresView (ListView):
    template_name = 'listarAdministradores.html'
    model = Administradores

    def get_query(self):
        return Administradores.objects.all()

class ListarPublicacionesView (ListView):
    template_name = 'listadoPublicaciones.html'
    model = Publicaciones

    def get_query(self):
        return Publicaciones.objects.all()

class ListarAutorizacionesView (ListView):
    template_name = 'listadoAutorizaciones.html'
    model = Autorizaciones

    def get_query(self):
        return Autorizaciones.objects.all()

class ListarArticulosView (ListView):
    template_name = 'listadoArticulos.html'
    model = Articulos

    def get_query(self):
        return Articulos.objects.all()

class ListarComentariosView (ListView):
    template_name = 'listadoComentarios.html'
    model = Comentarios

    def get_query(self):
        return Comentarios.objects.all()
