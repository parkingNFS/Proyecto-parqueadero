from django.db import models

# Create your models here.
class Tipo_de_factura (models.Model):
    tipo_de_factura= models.TextField("Tipo_de_factura")
    medio_de_pago= models.TextField("Medios_de_pago")

    def __str__(self):
        return f'{self.tipo_de_factura}'
    
    def __str__(self):
        return f'{self.medio_de_pago}'