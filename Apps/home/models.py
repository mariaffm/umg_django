from django.db import models

# Create your models here.

#CREATE CLASS PER TABLE
class Estudiante(models.Model):
   nombre =models.CharField(max_length=100)
   apellido =models.CharField(max_length=100) 
   creacion =models.DateTimeField(auto_now_add=True)
   
   def __str__(self) :
      return '%s' (self.nombre)


   class Publicaciones(models.Model):
      id =models.IntegerField
      nombre =models.CharField(max_length=100)
      apellido =models.CharField(max_length=100) 
      tipoNoticia =models.CharField(max_length=100) 
      descripcion =models.CharField(max_length=100) 
      creacion =models.DateTimeField(auto_now_add=True)
      

   def __str__(self) :
      return '%s' (self.nombre)

   class Meta:
      ordering = ['nombre']
      verbose_name = 'Publicacion'
      verbose_name_plural = 'Publicaciones'

   class Autorizaciones(models.Model):
      id =models.IntegerField
      nombre =models.CharField(max_length=100)
      apellido =models.CharField(max_length=100)
      creacion =models.DateTimeField(auto_now_add=True)
      

   def __str__(self) :
      return '%s' (self.nombre)

   class Meta:
      ordering = ['nombre']
      verbose_name = 'Publicacion'
      verbose_name_plural = 'Publicaciones'