from rest_framework import serializers
from .models import *


class vehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = vehiculo
        fields = ('__all__')