from rest_framework.viewsets import ModelViewSet
from apps.Datos_restaurante.models import Configuraciones
from apps.Datos_restaurante.api.serializers import ConfiguracionesSerializer

class ConfiguracionesViewSet(ModelViewSet):
    queryset = Configuraciones.objects.all()
    serializer_class = ConfiguracionesSerializer
