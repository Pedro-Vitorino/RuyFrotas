from django.contrib import admin
from .models import Motorista, Veiculo, Rota, Solicitacao, Manutencao,Gasto, Viagem

admin.site.register(Motorista)
admin.site.register(Veiculo)
admin.site.register(Rota)
admin.site.register(Solicitacao)
admin.site.register(Manutencao)
admin.site.register(Gasto)
admin.site.register(Viagem)
