from django.contrib import admin
from .models import FormaUña, ColorUña, DisenoPersonalizado

@admin.register(FormaUña)
class FormaUñaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(ColorUña)
class ColorUñaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_color')

@admin.register(DisenoPersonalizado)
class DisenoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_extra')