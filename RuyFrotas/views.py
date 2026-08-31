from django.shortcuts import render

def index(request):
    return render(request,"RuyFrotas/index.html")

def veiculos(request):
    return render(request,"RuyFrotas/veiculos.html")

def motoristas(request):
    return render(request,"RuyFrotas/motoristas.html")

def rotas(request):
    return render(request,"RuyFrotas/rotas.html")

def solicitacoes(request):
    return render(request,"RuyFrotas/solicitacoes.html")

def manutencoes(request):
    return render(request,"RuyFrotas/manutencoes.html")

def gastos(request):
    return render(request,"RuyFrotas/gastos.html")

