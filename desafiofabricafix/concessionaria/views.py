from rest_framework import viewsets
from concessionaria import serializers
from concessionaria import models

class VeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VeiculoSerializer
    queryset = models.Veiculo.objects.all()

class LojaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LojaSerializer
    queryset = models.Loja.objects.all()

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()






