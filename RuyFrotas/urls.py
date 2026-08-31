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
    path("veiculos/<int:id_veiculo>/", views.ver_veiculos, name="detalhe_veiculo"),
    path("motoristas/<int:id_motorista>/", views.ver_motoristas, name="detalhe_motorista"),
    path("rotas/<int:id_rotas>/", views.ver_rotas, name="detalhe_rota"),
    path("solicitacoes/<int:id_solicitacao>/", views.ver_solicitacao, name="detalhe_solicitacao"),
    path("manutencoes/<int:id_manutencao>/", views.ver_manutencoes, name="detalhe_manutencao"),
    path("gastos/<int:id_gastos>/", views.ver_gastos, name="detalhe_gasto"),
]