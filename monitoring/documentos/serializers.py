from rest_framework import serializers
from . import models

class DocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'solicitud', 'nombre', 'descripcion', 'archivo')
        model = models.Documento