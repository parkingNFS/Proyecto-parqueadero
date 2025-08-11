from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UsuariosSerializer

class UsuariosViewset(viewsets.ModelViewSet):

    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')