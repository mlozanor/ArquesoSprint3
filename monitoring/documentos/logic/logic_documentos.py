from ..models import Documento

def get_documentos():
    queryset = Documento.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_documento(form):
    documento = form.save()
    documento.save()
    return ()