from rest_framework.routers import DefaultRouter
from apps.pedido.api.views import PedidoModelViewset

router_pedido = DefaultRouter()
router_pedido.register(prefix="pedidos",basename="pedidos",viewset=PedidoModelViewset)