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
    ## Views de Veículo
    path("veiculos/<int:id_veiculo>/", views.ver_veiculos, name="detalhe_veiculo"),
    path("veiculos/<int:id_veiculo>/", views.editar_veiculos, name="editar_veiculo"),
    path("veiculos/<int:id_veiculo>/", views.remover_veiculos, name="remover_veiculo"),
    ## Views de Motoristas
    path("motoristas/<int:id_motorista>/", views.ver_motoristas, name="detalhe_motorista"),
    path("motoristas/<int:id_motorista>/", views.editar_motoristas, name="editar_motorista"),
    path("motoristas/<int:id_motorista>/", views.remover_motoristas, name="remover_motorista"),
    ## Views de Rotas
    path("rotas/<int:id_rotas>/", views.ver_rotas, name="detalhe_rota"),
    path("rotas/<int:id_rotas>/", views.editar_rotas, name="editar_rota"),
    path("rotas/<int:id_rotas>/", views.remover_rotas, name="remover_rota"),
    ## Views de Solicitações
    path("solicitacoes/<int:id_solicitacao>/", views.ver_solicitacao, name="detalhe_solicitacao"),
    path("solicitacoes/<int:id_solicitacao>/", views.editar_solicitacao, name="editar_solicitacao"),
    path("solicitacoes/<int:id_solicitacao>/", views.remover_solicitacao, name="remover_solicitacao"),
    ## Views de Manutenções
    path("manutencoes/<int:id_manutencao>/", views.ver_manutencoes, name="detalhe_manutencao"),
    path("manutencoes/<int:id_manutencao>/", views.editar_manutencoes, name="editar_manutencao"),
    path("manutencoes/<int:id_manutencao>/", views.remover_manutencoes, name="remover_manutencao"),
    ## Views de Gastos
    path("gastos/<int:id_gastos>/", views.ver_gastos, name="detalhe_gasto"),
    path("gastos/<int:id_gastos>/", views.editar_gastos, name="editar_gasto"),
    path("gastos/<int:id_gastos>/", views.remover_gastos, name="remover_gasto"),
]