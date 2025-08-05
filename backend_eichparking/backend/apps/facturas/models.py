from django.db import models

class facturas (models.Model):

    vehiculo_id = models.IntegerField("Vehiculo")
    total_pagar = models.IntegerField("Total a pagar")