from rest_framework import serializers
from .models import *


class TiempoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tiempo
        fields = ('__all__')