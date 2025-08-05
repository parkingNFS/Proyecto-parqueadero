from django.db import models

class usuario(models.Model):
    nombre = models.TextField("Nombre")
    apellido = models.TextField("Apellido")
    

    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'   
