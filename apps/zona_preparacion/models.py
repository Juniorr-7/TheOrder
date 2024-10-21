from django.db import models
from apps.pedido.models import Pedido
from apps.productos.models import Producto
from apps.detalles.models import DetallePedido

# Create your models here.
class ZonaPreparacion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=[
        ('En espera', 'En espera'),
        ('En preparación', 'En preparación'),
        ('Terminado', 'Terminado')
    ], default='En preparación')

    def __str__(self):
        return f"Pedido: {self.pedido.nombre_pedido}, Producto: {self.producto.nombre}, Cantidad: {self.cantidad}, Estado: {self.estado}"



