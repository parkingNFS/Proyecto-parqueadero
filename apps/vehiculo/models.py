from django.db import models

# Create your models here.
class Vehiculo (models.Model):
    placa= models.TextField("Placa", blank=True)
    modelo= models.TextField("modelo", blank=True)
    tipo= models.TextField("tipo", blank=True)
    categoria= models.TextField("categoria", blank=True)
    documentacion= models.TextField("documentacion", blank=True)
   
    def __str__(self):
        return f'{self.placa}'
    