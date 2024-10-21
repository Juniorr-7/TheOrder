from rest_framework.viewsets import ModelViewSet
from apps.productos.models import Producto
from apps.productos.api.serializers import ProductoSerializer

class ProductosModelViewSet(ModelViewSet):
    serializer_class= ProductoSerializer
    queryset = Producto.objects.all()