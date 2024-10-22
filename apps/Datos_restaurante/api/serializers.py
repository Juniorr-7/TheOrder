from rest_framework.serializers import ModelSerializer
from apps.Datos_restaurante.models import Configuraciones

class ConfiguracionesSerializer(ModelSerializer):
    class Meta:
        model = Configuraciones
        fields = ['nombre_restaurante', 'logo']