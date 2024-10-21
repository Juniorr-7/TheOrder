from rest_framework.viewsets import ModelViewSet
from apps.Datos_restaurante.models import Configuracion
from apps.Datos_restaurante.api.serializers import ConfiguracionSerializer

class ConfiguracionViewSet(ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer
