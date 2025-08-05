from django.db import models

class servicio (models.Model):

    nombre = models.TextField("Nombre")
    usuario_id = models.TextField("Usuario")
    placa_vehiculo = models.TextField("Placa de vehiculo")

