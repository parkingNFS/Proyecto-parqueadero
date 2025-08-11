from rest_framework import serializers
from .models import *


class TiempodeparqueoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tiempodeparqueo
        fields = ('__all__')