from django import forms
from .models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['nombre', 'descripcion', 'archivo']

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'archivo': 'Archivo'
        }
        