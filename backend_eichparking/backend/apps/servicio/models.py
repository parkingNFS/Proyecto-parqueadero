from django.db import models

class servicio (models.Model):

    usuario_id = models.TextField("Usuario")
    placa_automovil = models.TextField("Placa de vehiculo")

