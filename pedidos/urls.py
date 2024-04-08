from django.urls import path, include
from rest_framework import routers
from .views import PedidoView, DetallePedidoView 

router = routers.DefaultRouter()
router.register(r'pedidos', PedidoView, 'pedidos')
router.register(r'detallesPedido', DetallePedidoView, 'detallesPedido')

urlpatterns = [
  path("api/v1/", include(router.urls))
]