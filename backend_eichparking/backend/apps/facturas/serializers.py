from rest_framework import serializers
from .models import *


class FacturasSerializer(serializers.ModelSerializer):

    class Meta:
        model = facturas
        fields = ('__all__')