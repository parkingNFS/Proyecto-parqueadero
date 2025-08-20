from django.db import models

# Create your models here.
class Medios_de_pago (models.Model):
    medios_de_pago= models.TextField  ("Medios_de_pago")
    tiempo_parqueo_id= models.IntegerField ("Tiempo de parqueo")

    def _str_(self):
        return f'{Medios_de_pago}'