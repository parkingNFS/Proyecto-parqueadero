from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import Tipo_de_facturaSerializer

class Tipo_de_facturaViewset(viewsets.ModelViewSet):

    queryset = Tipo_de_factura.objects.all()
    serializer_class = Tipo_de_facturaSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')