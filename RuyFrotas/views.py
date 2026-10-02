from django.shortcuts import render, get_object_or_404,redirect
from .models import Motorista, Veiculo, Rota, Solicitacao, Manutencao,Gasto, Viagem
from django.contrib import messages
from .forms import FormsGasto, FormsManutencao, FormsMotorista, FormsRota, FormsSolicitacao, FormsUsuario, FormsVeiculo, FormsViagem,  MotoristaFormSet, FormsMotoristaAdmin, FormsMinhaConta, FormsAlterarSenha

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from .models import Usuario
from django.db import transaction



@login_required
def index(request):
    return render(request,"RuyFrotas/index.html")


## USUÁRIOS
@login_required
def minha_conta(request):

    usuario = request.user

    if request.method == 'POST':

        form = FormsMinhaConta(
            request.POST,
            instance=usuario
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Dados da conta atualizados com sucesso!'
            )

            return redirect('minha_conta')

    else:

        form = FormsMinhaConta(
            instance=usuario
        )

    return render(
        request,
        'RuyFrotas/minha_conta.html',
        {
            'form': form,
        }
    )
@login_required
def alterar_senha(request):

    if request.method == 'POST':

        form = FormsAlterarSenha(
            request.user,
            request.POST
        )

        if form.is_valid():

            usuario = form.save()

            login(
                request,
                usuario
            )

            messages.success(
                request,
                'Senha alterada com sucesso!'
            )

            return redirect('minha_conta')

    else:

        form = FormsAlterarSenha(
            request.user
        )

    return render(
        request,
        'RuyFrotas/alterar_senha.html',
        {
            'form': form,
        }
    )

## CADASTRO ADMIN
@login_required
def cadastrar_administrador(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            return render(request, 'RuyFrotas/cadastro_administrador.html', {
                'erro': 'As senhas não coincidem.'
            })

        if Usuario.objects.filter(username=username).exists():
            return render(request, 'RuyFrotas/cadastro_administrador.html', {
                'erro': 'Esse usuário já existe.'
            })

        usuario = Usuario.objects.create_user(
            username=username,
            email=email,
            password=password,
            tipo='ADMIN'
        )

        return redirect('login')

    return render(request, 'RuyFrotas/cadastro_administrador.html')

## CADASTRO 
@login_required
@transaction.atomic
def cadastrar_motorista(request):

    if request.method == 'POST':

        usuario_form = FormsUsuario(request.POST)

        motorista_formset = MotoristaFormSet(
            request.POST,
            request.FILES
        )

        if (
            usuario_form.is_valid()
            and motorista_formset.is_valid()
        ):
            usuario = usuario_form.save()

            motorista_formset.instance = usuario
            motorista_formset.save()

            messages.success(
                request,
                'Motorista cadastrado com sucesso!'
            )

            return redirect('motoristas')

    else:

        usuario_form = FormsUsuario()
        motorista_formset = MotoristaFormSet()

    return render(
        request,
        'RuyFrotas/cadastro_motorista.html',
        {
            'usuario_form': usuario_form,
            'motorista_formset': motorista_formset,
            'edicao': False,
        }
    )

## LOGIN E LOGOUT

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('index')

        return render(request, 'RuyFrotas/login.html', {
            'erro': 'Usuário ou senha inválidos.'
        })

    return render(request, 'RuyFrotas/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('login')

## VEÍCULOS
@login_required
def veiculos(request):
    context = {
        "veiculos": Veiculo.objects.all(),
    }
    return render(request,"RuyFrotas/veiculos.html", context)

@login_required
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

@login_required
def ver_veiculos(request, id_veiculo):
    context = {
        "veiculo": get_object_or_404(Veiculo, id=id_veiculo),
    }
    return render(request, "RuyFrotas/veiculo_ver.html", context)

@login_required
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


@login_required
def remover_veiculos(request, id_veiculo):
    if request.method == "POST":
        veiculo = get_object_or_404(Veiculo, id=id_veiculo)
        veiculo.delete()
        messages.success(request, 'Veículo removido com sucesso!')
        return redirect("veiculos")
    else:
        return render(request, "RuyFrotas/veiculo_remover.html")


## MOTORISTAS

@login_required
def motoristas(request):

    context = {
            "motoristas": Motorista.objects.all(),
        }
    return render(request,"RuyFrotas/motoristas.html", context)    


@login_required
@transaction.atomic
def editar_motoristas(request, id_motorista):

    motorista = get_object_or_404(
        Motorista,
        id=id_motorista
    )

    if request.method == 'POST':

        form = FormsMotoristaAdmin(
            request.POST,
            request.FILES,
            instance=motorista
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Motorista editado com sucesso!'
            )

            return redirect('motoristas')

    else:

        form = FormsMotoristaAdmin(
            instance=motorista
        )

    return render(
        request,
        'RuyFrotas/motorista_editar.html',
        {
            'form': form,
            'motorista': motorista,
        }
    )


@login_required
@transaction.atomic
def remover_motoristas(request, id_motorista):

    motorista = get_object_or_404(
        Motorista,
        id=id_motorista
    )

    usuario = motorista.usuario

    motorista.delete()
    usuario.delete()

    messages.success(
        request,
        'Motorista e conta removidos com sucesso!'
    )

    return redirect('motoristas')

@login_required
def ver_motoristas(request, id_motorista):
    context = {
        "motorista": get_object_or_404(Motorista, id=id_motorista),
    }
    return render(request, "RuyFrotas/motorista_ver.html", context)


## ROTAS
@login_required
def rotas(request):
    context = {
            "rotas": Rota.objects.all(),
        }
    return render(request,"RuyFrotas/rotas.html",context)

@login_required
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

@login_required
def ver_rotas(request, id_rotas):
    context = {
        "rota": get_object_or_404(Rota, id=id_rotas),
    }
    return render(request, "RuyFrotas/rota_ver.html", context)

@login_required
def remover_rotas(request, id_rotas):
    if request.method == "POST":
        rotas = get_object_or_404(Rota, id=id_rotas)
        rotas.delete()
        messages.success(request, 'Rota removida com sucesso!')
        return redirect("rotas")
    else:
        return render(request, "RuyFrotas/rotas_remover.html")


@login_required
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
@login_required
def solicitacoes(request):
    context = {
            "solicitacoes": Solicitacao.objects.all(),
        }
    return render(request,"RuyFrotas/solicitacoes.html",context)

@login_required
def alternar_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)

    solicitacao.atendida = not solicitacao.atendida
    solicitacao.save()

    return redirect('solicitacoes')

@login_required
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

@login_required
def ver_solicitacao(request, id_solicitacao):
    context = {
        "solicitacao": get_object_or_404(Solicitacao, id=id_solicitacao),
    }
    return render(request, "RuyFrotas/solicitacao_ver.html", context)

@login_required
def remover_solicitacao(request, id_solicitacao):
    if request.method == "POST":
        solicitacao = get_object_or_404(Solicitacao, id=id_solicitacao)
        solicitacao.delete()
        messages.success(request, 'Solicitação removida com sucesso!')
        return redirect("solicitacoes")
    else:
        return render(request, "RuyFrotas/solicitacao_remover.html")


@login_required
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
@login_required
def manutencoes(request):
    context = {
            "manutencoes": Manutencao.objects.all(),
        }
    return render(request,"RuyFrotas/manutencoes.html",context)

@login_required
def alternar_manutencao(request, id):
    manutencao = get_object_or_404(Manutencao, id=id)

    manutencao.atendida = not manutencao.atendida
    manutencao.save()

    return redirect('manutencoes')

@login_required
def nova_manutencao(request):
    if request.method == "POST":
        form = FormsManutencao(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manutenção cadastrada com sucesso!')
            return redirect('manutencoes')
    else:
        form = FormsManutencao()

    context = {
        "form": form,
    }
    return render(request,"RuyFrotas/manutencao_editar.html", context)

    
@login_required
def ver_manutencoes(request, id_manutencao):
    context = {
        "manutencao": get_object_or_404(Manutencao, id=id_manutencao),
    }
    return render(request, "RuyFrotas/manutencao_ver.html", context)

@login_required
def remover_manutencoes(request, id_manutencao):
    if request.method == "POST":
        manutencao = get_object_or_404(Manutencao, id=id_manutencao)
        manutencao.delete()
        messages.success(request, 'Manutenção removida com sucesso!')
        return redirect('manutencoes')
    else:
        return render(request, "RuyFrotas/manutencao_remover.html")


@login_required
def editar_manutencao(request, id_manutencao):
    manutencao = get_object_or_404(Manutencao, id=id_manutencao)
    if request.method == "POST":
        form = FormsManutencao(request.POST, request.FILES, instance=manutencao)

        if form.is_valid():
            form.save()
            messages.success(request, 'Manutenção editada com sucesso!')
            return redirect('manutencoes')
            
    else:
        form = FormsManutencao(instance= manutencao)

    context = {
        "form": form,
    }
    return render(request, "RuyFrotas/manutencao_editar.html", context)

## GASTOS
@login_required
def gastos(request):
    context = {
            "gastos": Gasto.objects.all(),
        }
    return render(request,"RuyFrotas/gastos.html",context)

@login_required
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

@login_required
def ver_gastos(request, id_gastos):
    context = {
        "gastos": get_object_or_404(Gasto, id=id_gastos),
    }
    return render(request, "RuyFrotas/gasto_ver.html", context)

@login_required
def remover_gastos(request, id_gastos):
    if request.method == "POST":
        gastos = get_object_or_404(Gasto, id=id_gastos)
        gastos.delete()
        messages.success(request, 'Gasto removido com sucesso!')
        return redirect("gastos")
    else:
        return render(request, "RuyFrotas/gasto_remover.html")


@login_required
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