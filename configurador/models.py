from django.db import models

class FormaUña(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='formas/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class ColorUña(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_color = models.CharField(max_length=7, help_text="Código hexadecimal ej: #FFB6C1")
    
    def __str__(self):
        return self.nombre

class DisenoPersonalizado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio_extra = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    imagen = models.ImageField(upload_to='disenos_personalizados/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre