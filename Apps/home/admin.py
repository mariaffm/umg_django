from django.contrib import admin
from .models import Estudiante
from .models import  Publicaciones
from .models import  Autorizaciones


# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Publicaciones)
admin.site.register(Autorizaciones)
