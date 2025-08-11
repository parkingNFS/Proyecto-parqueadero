from rest_framework import serializers
from .models import *


class PermisosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permisos
        fields = ('__all__')