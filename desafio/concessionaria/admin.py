from django.contrib import admin
from .models import Veiculo, Loja, Cliente

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'ano_fabricacao', 'ano_modelo', 'tipo_veiculo', 'portas', 'motor', 'potencia', 'torque')

admin.site.register(Veiculo, VeiculoAdmin)

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Loja, LojaAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Cliente, ClienteAdmin)
