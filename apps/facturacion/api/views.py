from rest_framework.viewsets import ModelViewSet
from apps.facturacion.models import Facturacion
from apps.facturacion.api.serializers import FacturacionSerializer

class FacturacionModelViewset(ModelViewSet):
    serializer_class= FacturacionSerializer
    queryset = Facturacion.objects.all()