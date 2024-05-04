from documentos.models import Documento
from ..models import Alarm

def getAlarms():
    queryset = Alarm.objects.all().order_by('-dateTime')
    return (queryset)

def get_documentos_by_solicitud(solicitud):
    queryset = Documento.objects.filter(solicitud=solicitud).order_by('-dateTime')[:10]
    return (queryset)

def create_alarm(solicitud, documento, limitExceeded):
    alarm = Alarm()
    alarm.solicitud = solicitud
    alarm.documento = documento
    alarm.limitExceeded = limitExceeded
    alarm.save()
    return alarm

