from rest_framework.serializers import ModelSerializer
from apps.zona_preparacion.models import ZonaPreparacion

class ZonaPreparacionSerializer(ModelSerializer):
    class Meta:
        model = ZonaPreparacion
        fields = ['pedido', 'producto', 'cantidad', 'estado']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['pedido'] = instance.pedido.nombre_pedido
        representation['producto'] = instance.producto.nombre
        return representation