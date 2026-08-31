from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("veiculos/", views.veiculos, name="veiculos"),
    path("motoristas/", views.motoristas, name="motoristas"),
    path("rotas", views.rotas, name="rotas"),
    path("solicitacoes", views.solicitacoes, name="solicitacoes"),
    path("manutencoes/", views.manutencoes, name="manutencoes"),
    path("gastos/", views.gastos, name="gastos"),
]