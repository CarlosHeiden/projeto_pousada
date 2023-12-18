from datetime import datetime, date, timedelta
from django.db.models import Q

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Apartamentos, Reservas
from .forms import FormApt, FormReservas


def verificar_reservas(request):
    apts = []
    aptos = Apartamentos.objects.all()
    for i in range(len(aptos)):
        apts.append(i)
    if request.method == 'POST':
        form = FormReservas(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['nome_cliente']
            apartamento = form.cleaned_data['nome_apartamento']
            entrada = form.cleaned_data['data_entrada']
            saida = form.cleaned_data['data_saida']
            preco = form.cleaned_data['preco_diaria']
            limpeza = form.cleaned_data['taxa_limpeza']
            total = form.cleaned_data['valor_total']
            dia_reserva = form.cleaned_data['data_reserva']

            if Reservas.objects.filter(nome_apartamento=apartamento, data_entrada__range=(entrada, saida)).exists():
                messages.error(request, f'O apartamento {apartamento} já tem reserva neste período de tempo.')
                return redirect('verificar_reservas')

            else:
                reservas = Reservas(
                    nome_cliente= cliente,
                    nome_apartamento = apartamento,
                    data_reserva = dia_reserva,
                    data_entrada = entrada,
                    data_saida = saida,
                    preco_diaria = preco,
                    taxa_limpeza = limpeza,
                    valor_total = total
                )
                reservas.save()
                messages.success(request, f'Reserva da cliente *{cliente}* cadastrada com sucesso!!')
                return redirect('verificar_reservas')
                
        else:
            redirect('verificar_reservas')

    else:
        form = FormReservas()
        periodo = (date.today(), date.today() + timedelta(days=1))
        reservas_no_periodo = Reservas.objects.filter(nome_apartamento=aptos[0], data_entrada__range=periodo)
        if reservas_no_periodo:
            messages.error(request, f'Já existe uma reserva neste período para o apartamento {aptos[0]}.')

    context = {'form': form, 'apts': apts}
    return render(request, "verificar_reservas.html", context)



import calendar
from django.shortcuts import render
from .models import Reservas, Apartamentos

def exibir_reservas(request):
    apartamentos = Apartamentos.objects.all()
    reservas_por_apartamento = {}

    for apartamento in apartamentos:
        reservas = Reservas.objects.filter(nome_apartamento=apartamento)
        reservas_por_apartamento[apartamento] = reservas

    return render(request, 'exibir_reservas.html', {'reservas_por_apartamento': reservas_por_apartamento})
