from rest_framework import serializers
from .models import *


class servicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = servicio
        fields = ('__all__')