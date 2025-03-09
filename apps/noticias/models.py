from django.db import models
from django.utils import timezone

class Noticia(models.Model):
    title = models.CharField(max_length=200)
    imageurl = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    content = models.TextField()
    publish = models.BooleanField(default=True)
    date = models.DateTimeField()  # Cambiado para almacenar la fecha de la noticia
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title