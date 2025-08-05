from django.db import models

class vehiculo (models.Model):
    
    Placa = models.TextField("Placa")
    usuario_id = models.IntegerField("Usuario")
    fecha_ingreso = models.TextField("Fecha de ingreso")
    


