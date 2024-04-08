from rest_framework import viewsets
from .models import Pedido, DetallePedido
from .serializer import PedidoSerializer, DetallePedidoSerializer

class PedidoView(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoView(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
