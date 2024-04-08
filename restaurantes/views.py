from rest_framework import viewsets
from .serializer import RestauranteSerializer
from .models import Restaurante
# Create your views here.


class RestauranteView(viewsets.ModelViewSet):
  serializer_class = RestauranteSerializer
  queryset = Restaurante.objects.all()