from django.db import models

# Create your models here.
class Horadeparqueo (models.Model):
    precio= models.IntegerField ("Precio")

    def __str__(self):
        return f'{self.precio}'

  