from rest_framework import serializers
from concessionaria import models

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veiculo
        fields = ['id', 'nome','preco', 'ano_fabricacao', 'ano_modelo', 'tipo_veiculo', 'portas', 'motor', 'potencia', 'torque']

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Loja
        fields = ['nome', 'endereco', 'telefone', 'cnpj']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = ['nome', 'endereco', 'telefone', 'cpf']







