from django.shortcuts import render, get_object_or_404,redirect
from .models import Motorista, Veiculo, Rota, Solicitacao, Manutencao,Gasto, Viagem
from django.contrib import messages
from .forms import FormsGasto, FormsManutencao, FormsMotorista, FormsRota, FormsSolicitacao, FormsUsuario, FormsVeiculo, FormsViagem
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request,"RuyFrotas/index.html")

## VEÍCULOS
def veiculos(request):
    context = {
        "veiculos": Veiculo.objects.all(),
    }
    return render(request,"RuyFrotas/veiculos.html", context)


def novo_veiculo(request):
    if request.method == "POST":
        form = FormsVeiculo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado com sucesso!')
            return redirect("veiculos")
    else:
        form = FormsVeiculo()

    context = {
        "form": form,
    }
    return render(request,"RuyFrotas/veiculo_editar.html", context)


def ver_veiculos(request, id_veiculo):
    context = {
        "veiculo": get_object_or_404(Veiculo, id=id_veiculo),
    }
    return render(request, "RuyFrotas/veiculo_ver.html", context)

def editar_veiculos(request, id_veiculo):
    veiculo = get_object_or_404(Veiculo, id=id_veiculo)
    if request.method == "POST":
        form = FormsVeiculo(request.POST, request.FILES, instance=veiculo)

        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo editado com sucesso!')
            return redirect("veiculos")
            
    else:
        form = FormsVeiculo(instance= veiculo)

    context = {
        "form": form,
    }
    return render(request, "RuyFrotas/veiculo_editar.html", context)


def remover_veiculos(request, id_veiculo):
    if request.method == "POST":
        veiculo = get_object_or_404(Veiculo, id=id_veiculo)
        veiculo.delete()
        messages.success(request, 'Veículo removido com sucesso!')
        return redirect("veiculos")
    else:
        return render(request, "RuyFrotas/veiculo_remover.html")


## MOTORISTAS
def motoristas(request):

    context = {
            "motoristas": Motorista.objects.all(),
        }
    return render(request,"RuyFrotas/motoristas.html", context)


def novo_motorista(request):
    if request.method == "POST":
        form = FormsMotorista(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Motorista cadastrado com sucesso!')
            return redirect("motoristas")
    else:
        form = FormsMotorista()

    context = {
        "form": form,
    }
    return render(request,"RuyFrotas/motorista_editar.html", context)

    

def editar_motoristas(request, id_motorista):
    motorista = get_object_or_404(Motorista, id=id_motorista)
    if request.method == "POST":
        form = FormsMotorista(request.POST, request.FILES, instance=motorista)

        if form.is_valid():
            form.save()
            messages.success(request, 'Motorista editado com sucesso!')
            return redirect("motoristas")
            
    else:
        form = FormsMotorista(instance= motorista)

    context = {
        "form": form,
    }
    return render(request, "RuyFrotas/motorista_editar.html", context)


def remover_motoristas(request, id_motorista):
    if request.method == "POST":
        motorista = get_object_or_404(Motorista, id=id_motorista)
        motorista.delete()
        messages.success(request, 'Motorista removido com sucesso!')
        return redirect("motoristas")
    else:
        return render(request, "RuyFrotas/motorista_remover.html")



def ver_motoristas(request, id_motorista):
    context = {
        "motorista": get_object_or_404(Motorista, id=id_motorista),
    }
    return render(request, "RuyFrotas/motorista_ver.html", context)

## ROTAS
def rotas(request):
    context = {
            "rotas": Rota.objects.all(),
        }
    return render(request,"RuyFrotas/rotas.html",context)


def nova_rota(request):
    if request.method == "POST":
        form = FormsRota(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rota cadastrada com sucesso!')
            return redirect("rotas")
    else:
        form = FormsRota()

    context = {
        "form": form,
    }
    return render(request,"RuyFrotas/rotas_editar.html", context)

    
def ver_rotas(request, id_rotas):
    context = {
        "rota": get_object_or_404(Rota, id=id_rotas),
    }
    return render(request, "RuyFrotas/rota_ver.html", context)

def remover_rotas(request, id_rotas):
    if request.method == "POST":
        rotas = get_object_or_404(Rota, id=id_rotas)
        rotas.delete()
        messages.success(request, 'Rota removida com sucesso!')
        return redirect("rotas")
    else:
        return render(request, "RuyFrotas/rotas_remover.html")



def editar_rotas(request, id_rotas):
    rota = get_object_or_404(Rota, id=id_rotas)
    if request.method == "POST":
        form = FormsRota(request.POST, request.FILES, instance=rota)

        if form.is_valid():
            form.save()
            messages.success(request, 'Rota editada com sucesso!')
            return redirect("rotas")
            
    else:
        form = FormsRota(instance= rota)

    context = {
        "form": form,
    }
    return render(request, "RuyFrotas/rotas_editar.html", context)

## SOLICITAÇÕES
def solicitacoes(request):
    context = {
            "solicitacoes": Solicitacao.objects.all(),
        }
    return render(request,"RuyFrotas/solicitacoes.html",context)

def alternar_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)

    solicitacao.atendida = not solicitacao.atendida
    solicitacao.save()

    return redirect('solicitacoes')


def nova_solicitacao(request):
    if request.method == "POST":
        form = FormsSolicitacao(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitação cadastrada com sucesso!')
            return redirect("solicitacoes")
    else:
        form = FormsSolicitacao()

    context = {
        "form": form,
    }
    return render(request,"RuyFrotas/solicitacao_editar.html", context)

    
def ver_solicitacao(request, id_solicitacao):
    context = {
        "solicitacao": get_object_or_404(Solicitacao, id=id_solicitacao),
    }
    return render(request, "RuyFrotas/solicitacao_ver.html", context)

def remover_solicitacao(request, id_solicitacao):
    if request.method == "POST":
        solicitacao = get_object_or_404(Solicitacao, id=id_solicitacao)
        solicitacao.delete()
        messages.success(request, 'Solicitação removida com sucesso!')
        return redirect("solicitacoes")
    else:
        return render(request, "RuyFrotas/solicitacao_remover.html")



def editar_solicitacao(request, id_solicitacao):
    solicitacao = get_object_or_404(Solicitacao, id=id_solicitacao)
    if request.method == "POST":
        form = FormsSolicitacao(request.POST, request.FILES, instance=solicitacao)

        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitação editada com sucesso!')
            return redirect("solicitacoes")
            
    else:
        form = FormsSolicitacao(instance= solicitacao)

    context = {
        "form": form,
    }
    return render(request, "RuyFrotas/solicitacao_editar.html", context)

## MANUTENÇÕES
def manutencoes(request):
    context = {
            "manutencoes": Manutencao.objects.all(),
        }
    return render(request,"RuyFrotas/manutencoes.html",context)

def alternar_manutencao(request, id):
    manutencao = get_object_or_404(Manutencao, id=id)

    manutencao.atendida = not manutencao.atendida
    manutencao.save()

    return redirect('manutencao')

def nova_manutencao(request):
    if request.method == "POST":
        form = FormsManutencao(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manutenção cadastrada com sucesso!')
            return redirect("manutencao")
    else:
        form = FormsManutencao()

    context = {
        "form": form,
    }
    return render(request,"RuyFrotas/manutencao_editar.html", context)

    
    
def ver_manutencoes(request, id_manutencao):
    context = {
        "manutencao": get_object_or_404(Manutencao, id=id_manutencao),
    }
    return render(request, "RuyFrotas/manutencao_ver.html", context)

def remover_manutencoes(request, id_manutencao):
    if request.method == "POST":
        manutencao = get_object_or_404(Manutencao, id=id_manutencao)
        manutencao.delete()
        messages.success(request, 'Manutenção removida com sucesso!')
        return redirect("manutencao")
    else:
        return render(request, "RuyFrotas/manutencao_remover.html")



def editar_manutencao(request, id_manutencao):
    manutencao = get_object_or_404(Manutencao, id=id_manutencao)
    if request.method == "POST":
        form = FormsManutencao(request.POST, request.FILES, instance=manutencao)

        if form.is_valid():
            form.save()
            messages.success(request, 'Manutenção editada com sucesso!')
            return redirect("manutencao")
            
    else:
        form = FormsManutencao(instance= manutencao)

    context = {
        "form": form,
    }
    return render(request, "RuyFrotas/manutencao_editar.html", context)

## GASTOS
def gastos(request):
    context = {
            "gastos": Gasto.objects.all(),
        }
    return render(request,"RuyFrotas/gastos.html",context)


def novo_gasto(request):
    if request.method == "POST":
        form = FormsGasto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gasto cadastrado com sucesso!')
            return redirect("gastos")
    else:
        form = FormsGasto()

    context = {
        "form": form,
    }
    return render(request,"RuyFrotas/gasto_editar.html",context)

    
def ver_gastos(request, id_gastos):
    context = {
        "gastos": get_object_or_404(Gasto, id=id_gastos),
    }
    return render(request, "RuyFrotas/gasto_ver.html", context)

def remover_gastos(request, id_gastos):
    if request.method == "POST":
        gastos = get_object_or_404(Gasto, id=id_gastos)
        gastos.delete()
        messages.success(request, 'Gasto removido com sucesso!')
        return redirect("gastos")
    else:
        return render(request, "RuyFrotas/gasto_remover.html")



def editar_gastos(request, id_gastos):
    gasto = get_object_or_404(Gasto, id=id_gastos)
    if request.method == "POST":
        form = FormsGasto(request.POST, request.FILES, instance=gasto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Gastos editados com sucesso!')
            return redirect("gastos")
            
    else:
        form = FormsGasto(instance= gasto)

    context = {
        "form": form,
    }
    return render(request, "RuyFrotas/gasto_editar.html", context)