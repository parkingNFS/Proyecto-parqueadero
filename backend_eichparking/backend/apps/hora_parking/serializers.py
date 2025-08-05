from rest_framework import serializers
from .models import *


class hora_parkingSerializer(serializers.ModelSerializer):

    class Meta:
        model = hora_parking
        fields = ('__all__')