from django.contrib import admin
from django.urls import path, include
from concessionaria.views import VeiculoViewSet, LojaViewSet, ClienteViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register('veiculos',VeiculoViewSet, basename='Veiculo')
router.register('lojas',LojaViewSet, basename='Loja')
router.register('clientes',ClienteViewSet, basename='Cliente')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    ]