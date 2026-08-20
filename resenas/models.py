from django.db import models

class Resena(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    calificacion = models.PositiveIntegerField(
        choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')],
        default=5,
        verbose_name="Calificación"
    )
    comentario = models.TextField(verbose_name="Comentario")
    foto = models.ImageField(
        upload_to='resenas/',
        blank=True,
        null=True,
        verbose_name="Foto de tus uñas"
    )
    aprobada = models.BooleanField(default=False, verbose_name="Aprobada")
    creada_en = models.DateTimeField(auto_now_add=True, verbose_name="Creada el")
    
    def __str__(self):
        return f"{self.nombre} - {self.calificacion}⭐"
    
    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        ordering = ['-creada_en']