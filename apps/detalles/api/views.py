from rest_framework.viewsets import ModelViewSet
from apps.detalles.models import DetallePedido
from apps.detalles.api.serializers import DetallePedidoSerializer

class DetallesModelViewset(ModelViewSet):
    serializer_class= DetallePedidoSerializer
    queryset = DetallePedido.objects.all()

    