from django.contrib import admin
from .models import *
# from .models import Proyecto
# from .models import Recurso
# from .models import Tecnologia
# from .models import Usuario
# from .models import UsuarioTecnologia
# from .models import ProyectoTecnologia

admin.site.register(Proyecto)
admin.site.register(Recurso)
admin.site.register(Tecnologia)
admin.site.register(Usuario)
admin.site.register(UsuarioTecnologia)
admin.site.register(ProyectoTecnologia)
