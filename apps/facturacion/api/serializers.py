from rest_framework.serializers import ModelSerializer
from apps.facturacion.models import Facturacion

class FacturacionSerializer(ModelSerializer):
    class Meta:
        model = Facturacion
        fields = ['restaurante','pedido', 'detalle', 'total_a_pagar']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        detalles = instance.pedido.detalles.all()
        detalle_rep = [{
            'producto': detalle.producto.nombre,
            'precio': detalle.producto.precio,
            'cantidad': detalle.cantidad
        } for detalle in detalles]
        representation['pedido'] = instance.pedido.nombre_pedido
        representation['detalle'] = detalle_rep
        total_a_pagar = sum(detalle.producto.precio * detalle.cantidad for detalle in detalles)
        representation['total_a_pagar'] = total_a_pagar

        return representation