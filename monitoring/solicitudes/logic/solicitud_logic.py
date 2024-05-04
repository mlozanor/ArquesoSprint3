from ..models import Solicitud

def getSolicitudes():
    queryset = Solicitud.objects.all()
    return (queryset)

def getSolicitudById(id):
    queryset = Solicitud.objects.get(id=id)
    return (queryset)

def createSolicitud(form):
    documento = form.save()
    documento.save()
    return ()