from django.db import models

class Tiempo (models.Model):
    horas= models.IntegerField("horas", blank=True, null=True)
    minutos= models.IntegerField("minutos", blank=True, null=True)
    contador= models.IntegerField("contador", blank=True, null=True)

    def __str__(self):
        return f'{self.horas}'
    