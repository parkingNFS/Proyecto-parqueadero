from rest_framework import serializers
from .models import *


class rolSerializer(serializers.ModelSerializer):

    class Meta:
        model = rol
        fields = ('__all__')