from rest_framework.viewsets import ModelViewSet
from apps.pedido.models import Pedido
from apps.pedido.api.serializers import PedidoSerializer

class PedidoModelViewset(ModelViewSet):
    serializer_class= PedidoSerializer
    queryset = Pedido.objects.all()