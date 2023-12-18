from django.urls import path
from . import views


urlpatterns = [
    path('verificar_reservas/', views.verificar_reservas, name='verificar_reservas'),
    path('exibir_reservas', views.exibir_reservas, name= 'exibir_reservas')
]