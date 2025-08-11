from django.db import models

class Tiempodeparqueo (models.Model):
    precio= models.IntegerField("Precio")

    def __str__(self):
        return f'{self.precio}'