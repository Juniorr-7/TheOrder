from rest_framework.routers import DefaultRouter
from apps.facturacion.api.views import FacturacionModelViewset

router_facturacion = DefaultRouter()
router_facturacion.register(prefix="facturacion",basename="facturacion",viewset=FacturacionModelViewset)