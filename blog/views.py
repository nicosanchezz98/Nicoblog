from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada, Comentario, Contacto
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    context = RequestContext(request)
    #posts = Entrada.objects.all()

    return render_to_response('home.html', 
                              {'posts':None},
                              context)


def noticias(request):
    context = RequestContext(request)
    #posts = Entrada.objects.all()
    posts = Entrada.objects.filter(published = True)

    return render_to_response('noticias.html', 
                              {'posts':posts},
                              context)


def calculadora(request):
    context = RequestContext(request)
    #posts = Entrada.objects.all()
    
    return render_to_response('calculadora.html', 
                              {'posts':None},
                              context)


def cambio(request):
    context = RequestContext(request)
    #posts = Entrada.objects.all()
    
    return render_to_response('cambio.html', 
                              {'posts':None},
                              context)

def galeria(request):
    context = RequestContext(request)
    #posts = Entrada.objects.all()
    
    return render_to_response('galeria.html', 
                              {'posts':None},
                              context)

def crono(request):
    context = RequestContext(request)
    #posts = Entrada.objects.all()
    
    return render_to_response('crono.html', 
                              {'posts':None},
                              context)

def sorteo(request):
    context = RequestContext(request)
    #posts = Entrada.objects.all()
    
    return render_to_response('sorteo.html', 
                              {'posts':None},
                              context)
def ubicacion(request):
    context = RequestContext(request)
    #posts = Entrada.objects.all()
    
    return render_to_response('ubicacion.html', 
                              {'posts':None},
                              context)



# Create your views here.


from blog.models import Entrada
# Create your views here.

def ver_post(request, id_post):
    context = RequestContext(request)
    mi_post = Entrada.objects.get(id=id_post)
    
    
    if request.method=="POST":
        nick = request.POST["nombre"]
        contenido = request.POST["message"]
        entrada = Entrada.objects.get(id=id_post)
        comentario=Comentario()
        comentario.nick = nick
        comentario.contenido = contenido
        comentario.post = entrada
        comentario.save()
    comentarios = Comentario.objects.filter(post=id_post)  
    
    return render_to_response('post.html', 
                              {'post':mi_post, 'comentarios':comentarios},
                              context)



def ver_comentarios(request, id_post):
    context = RequestContext(request)
    post = Entrada.objects.get(id=id_post)
    
    
    if request.method=="POST":
        nick = request.POST["nombre"]
        contenido = request.POST["message"]
        entrada = Entrada.objects.get(id=id_post)
        comentario=Comentario()
        comentario.nick = nick
        comentario.contenido = contenido
        comentario.post = entrada
        comentario.save()
    comentarios = Comentario.objects.filter(post=id_post)    
    return render_to_response('post.html', 
                              {'post':post,
                              'comentarios':comentarios},
                              context)

def enviar_comentarios(request):
    context = RequestContext(request)
    if request.method=="POST":
        nick = request.POST["nombre"]
        contenido = request.POST["message"]
        entrada = Entrada.objects.get(id=request.POST['id'])
        comentario=Comentario()
        comentario.nick = nick
        comentario.contenido = contenido
        comentario.post = entrada
        comentario.save()
    comentarios = Comentario.objects.filter(post=request.POST['id'])    
    return render_to_response('comentarios.html', 
                              {'comentarios':comentarios},
                              context)







def contact(request):
    context = RequestContext(request)
    enviado = "No se envio"
    if request.method == 'POST':
        enviado="Mensaje enviado"
        nombre= request.POST['nombre']
        mail= request.POST['mail']
        mensaje= request.POST['mensaje']
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.mail = mail
        contacto.mensaje = mensaje
        contacto.save()
        send_mail('Subject here', mensaje, mail, ['nicosanchezz98@gmail.com'], fail_silently=False)
        return render_to_response('home.html', 
                              {'enviado':enviado},
                              context)
    
    
    
    
    
    
    