from django.contrib import admin
from .models import Cita, Horario

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora', 'servicio', 'estado')
    list_filter = ('estado', 'fecha', 'servicio')
    search_fields = ('nombre', 'telefono', 'instagram')
    date_hierarchy = 'fecha'
    readonly_fields = ('creada_en',)
    
    fieldsets = (
        ('Datos de la clienta', {
            'fields': ('nombre', 'telefono', 'instagram')
        }),
        ('Servicio y diseño', {
            'fields': ('servicio', 'diseno')
        }),
        ('Fecha y hora', {
            'fields': ('fecha', 'hora')
        }),
        ('Estado', {
            'fields': ('estado', 'notas')
        }),
        ('Información del sistema', {
            'fields': ('creada_en',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('get_dia_display', 'apertura', 'cierre', 'activo')
    list_filter = ('activo',)