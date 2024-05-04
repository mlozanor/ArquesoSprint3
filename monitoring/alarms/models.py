from django.db import models
from solicitudes.models import Solicitud

class Alarm(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    value = models.FloatField(null=True, blank=True, default=None)
    limitExceeded = models.FloatField(null=True, blank=True, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"solicitud": %s, "documento": %s, "limitExceeded": %s, "dateTime": %s}' % (self.solicitud, self.documento, self.limitExceeded, self.dateTime)
    
    def toJson(self):
        alarm = {
            'solicitud': self.solicitud,
            'documento': self.documento,
            'limitExceeded': self.limitExceeded,
            'dateTime': self.dateTime
        }
        return alarm