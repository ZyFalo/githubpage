from django.db import models

class Partido(models.Model):
    fecha = models.CharField(max_length=50)
    equipo_local = models.CharField(max_length=100)
    equipo_visitante = models.CharField(max_length=100)
    resultado_local = models.IntegerField(null=True, blank=True)
    resultado_visitante = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=50)
    imagen_local = models.URLField()
    imagen_visitante = models.URLField()

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha}"