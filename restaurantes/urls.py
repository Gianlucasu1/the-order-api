from django.urls import path, include
from rest_framework import routers
from restaurantes import views 

router = routers.DefaultRouter()
router.register(r'restaurantes', views.RestauranteView, 'restaurantes')

urlpatterns = [
  path("api/v1/", include(router.urls))
]