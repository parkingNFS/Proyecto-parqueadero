from django.db import models

class vehiculo (models.Model):
    Placa = models.TextField("Placa")
    matricula_vehiculo = models.TextField("Matricula y vehiculo")
    usuario_id = models.IntegerField("Usuario")
    fecha_ingreso = models.TextField("Fecha de ingreso")
    Servicio_id = models.IntegerField("Servicio")


