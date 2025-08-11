from rest_framework import serializers
from .models import *


class Tipo_de_facturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipo_de_factura
        fields = ('__all__')