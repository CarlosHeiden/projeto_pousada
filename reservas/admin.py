from django.contrib import admin, messages
from reservas.models import Apartamentos, Reservas


class ReservasAdmin(admin.ModelAdmin):
    list_display = [
        'nome_apartamento',
        'nome_cliente',
        'data_pgto_reserva',
        'data_entrada',
        'data_saida',
        'preco_diaria',
        'vl_pgto_reserva',
        'taxa_limpeza',
        'valor_total_diarias',
        'saldo_a_pagar',
    ]

    list_filter = [
        'nome_apartamento',
        'nome_cliente',
        'data_pgto_reserva',
        'data_entrada',
        'data_saida',
        'preco_diaria',
        'vl_pgto_reserva',
        'taxa_limpeza',
        'valor_total_diarias',
        'saldo_a_pagar',
    ]

    search_fields = [
        'nome_apartamento',
        'nome_cliente',
        'data_pgto_reserva',
        'data_entrada',
        'data_saida',
        'preco_diaria',
        'vl_pgto_reserva',
        'taxa_limpeza',
        'valor_total_diarias',
        'saldo_a_pagar',
    ]


class ApartamentosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'numero_pessoas']

    list_filter = ['nome', 'numero_pessoas']

    search_fields = ['nome', 'numero_pessoas']


admin.site.register(Reservas, ReservasAdmin)
admin.site.register(Apartamentos, ApartamentosAdmin)
