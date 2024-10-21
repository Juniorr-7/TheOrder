from rest_framework.viewsets import ModelViewSet
from apps.zona_preparacion.models import ZonaPreparacion
from apps.zona_preparacion.api.serializers import ZonaPreparacionSerializer

class zonaPreparacionModelViewSet(ModelViewSet):
    serializer_class= ZonaPreparacionSerializer
    queryset = ZonaPreparacion.objects.all()