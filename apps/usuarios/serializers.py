from rest_framework import serializers
from .models import *


class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('__all__')