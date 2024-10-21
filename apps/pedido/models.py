from django.db import models

class Pedido(models.Model):
        nombre_pedido = models.CharField(max_length=100)
        para_llevar = models.CharField(max_length=20, choices=[
                ('Si', 'Si'),
                ('No', 'No')
        ], default='No')
        estado = models.CharField(max_length=20, choices=[
                ('Pendiente', 'Pendiente'),
                ('En preparación', 'En preparación'),
                ('Terminado', 'Terminado')
        ], default='Pendiente')

        def __str__(self):
                return self.nombre_pedido

