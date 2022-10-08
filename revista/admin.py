from django.contrib import admin

from Apps.home.models import Estudiante
from .models import  Administradores,Articulos, Autorizaciones, Comentarios, Publicaciones, Estududiantes, Usuario

# Register your models here.
admin.site.register(Publicaciones)
admin.site.register(Autorizaciones)
admin.site.register(Articulos)
admin.site.register(Comentarios)

#******************
#add content
admin.site.register(Estududiantes)
admin.site.register(Administradores)

admin.site.register(Usuario)

