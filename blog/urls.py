from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       url(r'^calculadora/$', 'blog.views.calculadora', name='calculadora'),
                       url(r'^cambio/$', 'blog.views.cambio', name='cambio'),
                       url(r'^contact/$', 'blog.views.contact', name='contact'),
                       url(r'^galeria/$', 'blog.views.galeria', name='galeria'),
                       url(r'^crono/$', 'blog.views.crono', name='crono'),
                       url(r'^sorteo/$', 'blog.views.sorteo', name='sorteo'),
                       url(r'^noticias/$', 'blog.views.noticias', name='noticias'),
                       url(r'^ubicacion/$', 'blog.views.ubicacion', name='ubicacion'),
                       url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'blog.views.ver_post', name='vermipost'),
                       url(r'^contactame/$', 'blog.views.contact', name='contactame'), 
                       url(r'^enviar_comentarios/$', 'blog.views.enviar_comentarios', name='enviar_comentarios'),
)
                      
                      


