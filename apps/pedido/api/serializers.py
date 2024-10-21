from rest_framework.serializers import ModelSerializer
from apps.pedido.models import Pedido
from apps.detalles.api.serializers import DetallePedidoSerializer

class PedidoSerializer(ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['nombre_pedido', 'para_llevar', 'estado', 'detalles']