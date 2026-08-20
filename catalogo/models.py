from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.PositiveIntegerField(
        help_text="Duración aproximada en minutos"
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Diseno(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=100, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    imagen = models.ImageField(
        upload_to="disenos/",
        blank=True,
        null=True
    )

    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="disenos"
    )

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre