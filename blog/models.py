# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Entrada(models.Model):
    class Meta:
        verbose_name = "Mi Entrada"
        verbose_name_plural = "Todas mis entradas"
        ordering=['-fecha']
    
    titulo = models.CharField(u'Título', max_length=100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    resumen= models.CharField(u'Resumen',max_length=512)
    contenido = models.TextField(u'Contenido')
    published = models.BooleanField(u'Publicado?', default=True)
    autor = models.ForeignKey(User)
    categoria = models.ManyToManyField('Categoria')
    
    def __str__(self):
        return self.titulo
    
    
class Categoria(models.Model):
    nombre = models.CharField(u'Título de la Categoría', max_length=100)
    descripcion = models.CharField(u'Descripción de la Categoría', max_length=256)
    
    
    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    nombre = models.CharField(u'Nombre', max_length=100)
    celu = models.CharField(u'Telefono', max_length=100)
    mail = models.CharField(u'Mail', max_length=100)
    mensaje = models.TextField(u'Mensaje')
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    
    
    
class Comentario(models.Model):
    post = models.ForeignKey(Entrada)
    nick = models.CharField("publicado por:", max_length=50)
    contenido = models.TextField("Ahi lo anoto", max_length=500)
    fecha = models.DateTimeField("Fecha", auto_now_add=True)
        
    def __str__(self):
        return self.nick