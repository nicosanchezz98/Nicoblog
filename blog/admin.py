from django.contrib import admin
from blog.models import Entrada, Categoria, Contacto, Comentario
# Register your models here.
admin.site.register(Entrada)
admin.site.register(Categoria)
admin.site.register(Contacto)
admin.site.register(Comentario)