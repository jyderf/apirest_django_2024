from django.contrib import admin
from .models import Persona
from .models import Proyecto
from .models import Estado_Tarea
from .models import Tarea


admin.site.register(Persona)
admin.site.register(Proyecto)
admin.site.register(Estado_Tarea)
admin.site.register(Tarea)
