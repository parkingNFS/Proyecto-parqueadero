from django.db import models

# Create your models here.
class Permisos (models.Model):
    agregar= models.TextField ("Agregar")
    eliminar=models.TextField("Eliminar")
    editar=models.TextField("Editar")
    consultar=models.TextField("Consultar")
    usuario_id=models.TextField("Usuarios_id")
    rol_id=models.IntegerField("Rol_id")

    def __str__(self):
        return f'{self.agregar}'
    
    def __str__(self):
        return f'{self.eliminar}'
    
    def __str__(self):
        return f'{self.editar}'
    
    def __str__(self):
        return f'{self.consultar}'