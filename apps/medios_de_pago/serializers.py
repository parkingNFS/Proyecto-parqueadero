from rest_framework import serializers
from .models import Medios_de_pago


class Medios_de_pagoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medios_de_pago
        fields = ('__all__')