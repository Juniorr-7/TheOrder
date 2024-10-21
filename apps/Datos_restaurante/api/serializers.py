from rest_framework.serializers import ModelSerializer
from apps.Datos_restaurante.models import Configuracion

class ConfiguracionSerializer(ModelSerializer):
    class Meta:
        model = Configuracion
        fields = ['nombre_restaurante', 'logo']