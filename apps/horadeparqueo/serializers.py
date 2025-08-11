from rest_framework import serializers
from .models import Horadeparqueo


class HoradeparqueoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horadeparqueo
        fields = ('__all__')