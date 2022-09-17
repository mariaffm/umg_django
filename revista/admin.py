from django.contrib import admin
from .models import Articulos, Autorizaciones, Comentarios, Publicaciones

# Register your models here.
admin.site.register(Publicaciones)
admin.site.register(Autorizaciones)
admin.site.register(Articulos)
admin.site.register(Comentarios)