from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    renderer_classes = [JSONRenderer]