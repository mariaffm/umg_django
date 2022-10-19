from dataclasses import field
from pyexpat import model
from unittest.util import _MAX_LENGTH
from  django import forms
from pkg_resources import require 
from .models import Administradores, Articulos, Autorizaciones, Comentarios, Publicaciones
from .models import Estududiantes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ArticuloForm(forms.ModelForm):
    class Meta:
        model= Articulos
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model= Estududiantes
        fields = '__all__'  

class AdministradorForm(forms.ModelForm):
    class Meta:
        model= Administradores
        fields ='__all__'


class PublicacionesForm(forms.ModelForm):
    class Meta:
        model= Publicaciones
        fields= '__all__'

class AutorizacionesForm(forms.ModelForm):
    class Meta:
        model = Autorizaciones
        fields = '__all__'
    
class ComentariosForm(forms.ModelForm):
    class Meta:
        model= Comentarios
        fields = '__all__'

class RegistroForm(UserCreationForm):
    first_name =forms.CharField(max_length=140, required=True)
    last_name =forms.CharField(max_length=140, required =False)
    email =forms.EmailField(required =True)

    class Meta:
        model =User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
        