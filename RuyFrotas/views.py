from django.shortcuts import render, get_object_or_404
from .models import Motorista, Veiculo, Rota, Solicitacao, Manutencao,Gasto, Viagem

def index(request):
    return render(request,"RuyFrotas/index.html")

def veiculos(request):
    context = {
        "veiculos": Veiculo.objects.all(),
    }
    return render(request,"RuyFrotas/veiculos.html", context)

def ver_veiculos(request, id_veiculo):
    context = {
        "veiculo": get_object_or_404(Veiculo, id=id_veiculo),
    }
    return render(request, "RuyFrotas/veiculo_ver.html", context)

def motoristas(request):

    context = {
            "motoristas": Motorista.objects.all(),
        }
    return render(request,"RuyFrotas/motoristas.html", context)


def ver_motoristas(request, id_motorista):
    context = {
        "motorista": get_object_or_404(Motorista, id=id_motorista),
    }
    return render(request, "RuyFrotas/motorista_ver.html", context)

def rotas(request):
    context = {
            "rotas": Rota.objects.all(),
        }
    return render(request,"RuyFrotas/rotas.html",context)

def ver_rotas(request, id_rotas):
    context = {
        "rota": get_object_or_404(Rota, id=id_rotas),
    }
    return render(request, "RuyFrotas/rota_ver.html", context)

def solicitacoes(request):
    context = {
            "solicitacoes": Solicitacao.objects.all(),
        }
    return render(request,"RuyFrotas/solicitacoes.html",context)

def ver_solicitacao(request, id_solicitacao):
    context = {
        "solicitacao": get_object_or_404(Solicitacao, id=id_solicitacao),
    }
    return render(request, "RuyFrotas/solicitacao_ver.html", context)

def manutencoes(request):
    context = {
            "manutencoes": Manutencao.objects.all(),
        }
    return render(request,"RuyFrotas/manutencoes.html",context)

def ver_manutencoes(request, id_manutencao):
    context = {
        "rota": get_object_or_404(Manutencao, id=id_manutencao),
    }
    return render(request, "RuyFrotas/manutencao_ver.html", context)

def gastos(request):
    context = {
            "gastos": Gasto.objects.all(),
        }
    return render(request,"RuyFrotas/gastos.html",context)

def ver_gastos(request, id_gastos):
    context = {
        "rota": get_object_or_404(Gasto, id=id_gastos),
    }
    return render(request, "RuyFrotas/gasto_ver.html", context)
