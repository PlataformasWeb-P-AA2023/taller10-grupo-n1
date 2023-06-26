from django.contrib import admin

# Importar las clases del modelo
from ordenamiento.models import Parroquia, Barrio


class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'viviendas', 'num_parques', 'edificios', 'parroquia')
    search_fields = ('nombre', 'parroquia')

admin.site.register(Barrio, BarrioAdmin)
