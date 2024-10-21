from django.db import models

# Create your models here.
class Configuracion(models.Model):
    nombre_restaurante = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.nombre_restaurante