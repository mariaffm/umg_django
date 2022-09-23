from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from Apps.forms import ArticuloForm


#********************

from django.urls import reverse_lazy

#**************************

# Create your views here.

class principalView(TemplateView):
    template_name='principal.html'


#*********************************
#*********************************
class CrearArticulosView(CreateView):
  template_name: 'crearArticulo.html'
  form_class: ArticuloForm
  success_url = reverse_lazy('home:homeapp')


#*********************