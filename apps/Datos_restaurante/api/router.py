from rest_framework.routers import DefaultRouter
from apps.Datos_restaurante.api.views import ConfiguracionesViewSet

router_datos = DefaultRouter()
router_datos.register(prefix="datos",basename="datos",viewset=ConfiguracionesViewSet)