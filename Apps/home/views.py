from io import UnsupportedOperation
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
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

    def get_queryset(self):
        vNombre =self.request.GET.get('nombre')
        if(vNombre):
            return Estududiantes.objects.filter(nombre__icontains=vNombre)
        else:
            return Estududiantes.objects.all()


class ListarAdministradoresView (ListView):
    template_name = 'listarAdministradores.html'
    model = Administradores

    def get_queryset(self):
        vCargo = self.request.GET.get('cargo')
        if(vCargo):
            return Administradores.objects.filter(cargo__icontains = vCargo)
        else:
            return Administradores.objects.all()

class ListarPublicacionesView (ListView):
    template_name = 'listadoPublicaciones.html'
    model = Publicaciones

    def get_queryset(self):
        vTipo = self.request.GET.get('tipoNoticia')
        if(vTipo):
            return Publicaciones.objects.filter(tipoNoticia__icontains =vTipo)
        else:
            return Publicaciones.objects.all()

class ListarAutorizacionesView (ListView):
    template_name = 'listadoAutorizaciones.html'
    model = Autorizaciones

    def get_queryset(self):
        vNombre =self.request.GET.get('nombre')
        if(vNombre):
            return Autorizaciones.objects.filter(nombre__icontains =vNombre)
        else:  
            return Autorizaciones.objects.all()

class ListarArticulosView (ListView):
    template_name = 'listadoArticulos.html'
    model = Articulos

    def get_queryset(self):
        vTitulo = self.request.GET.get('titulo')
        if(vTitulo):
            return Articulos.objects.filter(titulo__icontains=vTitulo)
        else:
            return Articulos.objects.all()

class ListarComentariosView (ListView):
    template_name = 'listadoComentarios.html'
    model = Comentarios

    def get_queryset(self):
        vDes= self.request.GET.get('descripcion')
        if(vDes):
            return Comentarios.objects.filter(descripcion__icontains=vDes)
        else:
            return Comentarios.objects.all()

class EditarEstudianteView(UpdateView):
    template_name= 'editarestudiante.html'
    model = Estududiantes
    form_class = EstudianteForm
    success_url = reverse_lazy('home:listadoest')

class EditarAdministradorView(UpdateView):
    template_name= 'editaradministrador.html'
    model = Administradores
    form_class = AdministradorForm
    success_url = reverse_lazy('home:listadoadm')

class EditarAdministradorView(UpdateView):
    template_name= 'editaradministrador.html'
    model = Administradores
    form_class = AdministradorForm
    success_url = reverse_lazy('home:listadoadm')

class EditarArticulosView(UpdateView):
  template_name= 'editarArticulo.html'
  model= Articulos
  form_class= ArticuloForm
  success_url = reverse_lazy('home:listadoart')

class EditarPublicacionView(UpdateView):
    template_name= 'editarPublicacion.html'
    model=Publicaciones
    form_class= PublicacionesForm
    success_url = reverse_lazy('home:listadopubl')

class EditarAutorizacionesView(UpdateView):
    template_name= 'editarAutorizaciones.html'
    model=Autorizaciones
    form_class = AutorizacionesForm
    success_url = reverse_lazy('home:listadoaut')

class EditarComentariosView(UpdateView):
    template_name= 'editarComentarios.html'
    model= Comentarios
    form_class = ComentariosForm
    success_url = reverse_lazy('home:listadocom')
