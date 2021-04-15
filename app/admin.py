from django.contrib import admin
from .models import *

admin.site.register(Proyecto)
admin.site.register(Recurso)
admin.site.register(Tecnologia)
admin.site.register(Usuario)

admin.site.register(UsuarioTecnologia)
admin.site.register(ProyectoTecnologia)
