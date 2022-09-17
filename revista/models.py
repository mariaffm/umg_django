from django.db import models

# Create your models here.
class Publicaciones(models.Model):
      nombre =models.CharField(blank = True,max_length=100, verbose_name = 'Nombre')
      apellido =models.CharField(blank = True,max_length=100, verbose_name = 'Apellido') 
      tipoNoticia =models.CharField(blank = True,max_length=100, verbose_name = 'Tipo_Noticia') 
      creacion =models.DateTimeField(auto_now_add=True)
      

def __str__(self):
        return '%s %s' % (self.nombre, self.tipoNoticia )

class Meta:
      ordering = ['nombre']
      verbose_name = 'Publicacion'
      verbose_name_plural = 'Publicaciones' 



class Autorizaciones(models.Model):
      nombre =models.CharField(blank = True,max_length=100, verbose_name = 'Nombre')
      apellido =models.CharField(blank = True,max_length=100, verbose_name = 'Apellido') 
      comentario =models.CharField(blank = True,max_length=100, verbose_name = 'Comentario') 
      Publicaciones = models.ManyToManyField(Publicaciones)
      creacion =models.DateTimeField(auto_now_add=True)
      

def __str__(self):
        return '%s'% (self.nombre)

class Meta:
      ordering = ['nombre']
      verbose_name = 'Autorizacion'
      verbose_name_plural = 'Autorizaciones' 



class Articulos(models.Model):
      tipo_Articulo=(
        ('G', 'Grafica'),
        ('D', 'Divulgativa'),
        ('I', 'Informativa'),   
        ('E', 'Educativa'),
      )
      
      titulo =models.CharField(blank = True,max_length=100, verbose_name = 'titulo')
      fecha_creacion =models.DateField(verbose_name = 'Fecha') 
      descripcion =models.CharField(blank = True,max_length=100, verbose_name = 'Descripcion') 
      tipo = models.CharField(
        max_length=1,
        choices = tipo_Articulo,
        default = 'E',
      )
      publicaciones = models.ForeignKey(Publicaciones,on_delete =models.CASCADE)
      creacion =models.DateTimeField(auto_now_add=True)
      

def __str__(self):
        return '%s'% (self.nombre)



class Comentarios(models.Model):
      descripcion =models.CharField(blank = True,max_length=100, verbose_name = 'Descripcion')
      Articulos = models.ManyToManyField(Articulos)
      creacion =models.DateTimeField(auto_now_add=True)
      

def __str__(self):
        return '%s'% (self.nombre)
