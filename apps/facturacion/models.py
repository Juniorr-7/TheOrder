from django.db import models
from apps.pedido.models import Pedido
from apps.detalles.models import DetallePedido
from apps.Datos_restaurante.models import Configuracion

# Create your models here.
class Facturacion(models.Model):
    restaurante = models.ForeignKey(Configuracion, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    detalle = models.ForeignKey(DetallePedido, on_delete=models.SET_NULL, null=True)
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_total(self):
        total = 0
        detalles = DetallePedido.objects.filter(pedido=self.pedido)
        for detalle in detalles:
            total += detalle.producto.precio * detalle.cantidad
        return total

    def save(self, *args, **kwargs):
        self.total_a_pagar = self.calcular_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Facturación para el pedido {self.pedido.nombre_pedido}: {self.total_a_pagar}"