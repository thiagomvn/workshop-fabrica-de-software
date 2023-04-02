from django.db import models


class Veiculo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    ano_fabricacao = models.IntegerField()
    ano_modelo = models.IntegerField()
    tipo_veiculo = models.CharField(max_length=20)
    portas = models.IntegerField()
    motor = models.CharField(max_length=80)
    potencia = models.CharField(max_length=10)
    torque = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Loja(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome