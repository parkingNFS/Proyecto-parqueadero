from django.db import models

# Create your models here.
class Usuario(models.Model):

    nombre= models.TextField("nombre", blank= True)
    apellido= models.TextField("apellido", blank= True) 
    password= models.CharField("contraseña", null= True, blank= True)
    correo= models.TextField("correo", blank= True)
    rol_id= models.IntegerField("rol", null= True)

    def __str__(self):
        return f'{self.nombre}'

    

    
