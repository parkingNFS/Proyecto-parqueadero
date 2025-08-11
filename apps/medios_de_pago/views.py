from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import Medios_de_pagoSerializer

class Medios_de_pagoViewset(viewsets.ModelViewSet):

    queryset = Medios_de_pago.objects.all()
    serializer_class = Medios_de_pagoSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')