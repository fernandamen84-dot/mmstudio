from django.contrib import admin
from .models import Resena

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'calificacion', 'comentario_corto', 'aprobada', 'creada_en')
    list_filter = ('aprobada', 'calificacion')
    search_fields = ('nombre', 'comentario')
    list_editable = ('aprobada',)
    readonly_fields = ('creada_en',)
    
    def comentario_corto(self, obj):
        return obj.comentario[:50] + '...' if len(obj.comentario) > 50 else obj.comentario
    comentario_corto.short_description = 'Comentario'