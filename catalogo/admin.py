from django.contrib import admin
from .models import Servicio, Diseno


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'precio',
        'duracion',
        'activo',
    )
    list_filter = ('activo',)
    search_fields = ('nombre',)


@admin.register(Diseno)
class DisenoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'categoria',
        'precio',
        'servicio',
        'activo',
    )
    list_filter = ('categoria', 'activo')
    search_fields = ('nombre', 'categoria')