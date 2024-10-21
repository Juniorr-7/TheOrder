from rest_framework.serializers import ModelSerializer
from apps.detalles.models import DetallePedido

class DetallePedidoSerializer(ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ['pedido', 'producto', 'cantidad', 'observaciones']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['pedido'] = instance.pedido.nombre_pedido if instance.pedido else "Pedido no asignado"
        representation['producto'] = instance.producto.nombre if instance.producto else "Producto no asignado"
        
        return representation