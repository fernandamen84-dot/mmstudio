from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Servicio, Diseno

class Cita(models.Model):
    ESTADOS = [
        ('pendiente', '⏳ Pendiente'),
        ('confirmada', '✅ Confirmada'),
        ('completada', '💅 Completada'),
        ('cancelada', '❌ Cancelada'),
    ]
    
    # Datos de la clienta
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    instagram = models.CharField(max_length=50, blank=True, verbose_name="Instagram")
    
    # Servicio y diseño
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name="Servicio")
    diseno = models.ForeignKey(Diseno, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Diseño")
    
    # Fecha y hora
    fecha = models.DateField(verbose_name="Fecha")
    hora = models.TimeField(verbose_name="Hora")
    
    # Estado
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente', verbose_name="Estado")
    
    # Notas adicionales
    notas = models.TextField(blank=True, verbose_name="Notas adicionales")
    
    # Fecha de creación
    creada_en = models.DateTimeField(auto_now_add=True, verbose_name="Creada el")
    
    def __str__(self):
        return f"{self.nombre} - {self.fecha} {self.hora}"
    
    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ['-fecha', '-hora']

class Horario(models.Model):
    DIAS = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    
    dia = models.CharField(max_length=20, choices=DIAS, unique=True, verbose_name="Día")
    apertura = models.TimeField(verbose_name="Hora de apertura")
    cierre = models.TimeField(verbose_name="Hora de cierre")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    def __str__(self):
        return f"{self.get_dia_display()}: {self.apertura} - {self.cierre}"
    
    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"
        ordering = ['id']