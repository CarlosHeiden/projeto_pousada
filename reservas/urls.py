from django.urls import path
from . import views


urlpatterns = [
    path('fazer_reservas/', views.fazer_reserva, name='fazer_reservas'),
    path('exibir_reservas/', views.exibir_reservas, name='exibir_reservas'),
    path(
        'consultar_reservas/',
        views.consultar_datas_para_reserva,
        name='consultar_reservas',
    ),
    path(
        'reserva/<int:reserva_id>/editar/',
        views.editar_reserva,
        name='editar_reserva',
    ),
    path(
        'reserva/<int:reserva_id>/excluir/',
        views.excluir_reserva,
        name='excluir_reserva',
    ),
]
