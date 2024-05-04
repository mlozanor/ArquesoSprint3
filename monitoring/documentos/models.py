from django.db import models
from solicitudes.models import Solicitud

class Documento(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '%s - %s' % (self.solicitud, self.nombre)    

# Create your models here.
