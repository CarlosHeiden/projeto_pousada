from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Apartamentos, Reservas
from .forms import FormMiniCalendario, FormConsultarReservas, FormEditarReserva


def fazer_reserva(request):
    apts = []
    aptos = Apartamentos.objects.all()
    for i in range(len(aptos)):
        apts.append(i)
    if request.method == 'POST':
        form = FormMiniCalendario(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['nome_cliente']
            apartamento = form.cleaned_data['nome_apartamento']
            dia_pgto_reserva = form.cleaned_data['data_pgto_reserva']
            entrada = form.cleaned_data['data_entrada']
            saida = form.cleaned_data['data_saida']
            preco = form.cleaned_data['preco_diaria']
            vl_pgto_reserva = form.cleaned_data['vl_pgto_reserva']
            limpeza = form.cleaned_data['taxa_limpeza']

            # Registros onde a reserva está ativa na data_verificacao
            reservas_ativas = Reservas.objects.filter(
                nome_apartamento=apartamento,
                data_entrada__lte=saida,
                data_saida__gte=entrada,
            )

            if reservas_ativas:
                messages.error(
                    request,
                    '***Já existem reservas para este apartamento neste intervalo.***',
                )
                # print(reservas_encontradas)
                print(reservas_ativas)
                return redirect('fazer_reservas')

            else:
                reservas = Reservas(
                    nome_cliente=cliente,
                    nome_apartamento=apartamento,
                    data_pgto_reserva=dia_pgto_reserva,
                    data_entrada=entrada,
                    data_saida=saida,
                    preco_diaria=preco,
                    vl_pgto_reserva=vl_pgto_reserva,
                    taxa_limpeza=limpeza,
                )
                reservas.save()
                messages.success(
                    request,
                    f'Reserva do cliente *{cliente}* cadastrada com sucesso!!',
                )
                return redirect('fazer_reservas')

        else:
            redirect('fazer_reservas')

    else:
        form = FormMiniCalendario()

    context = {'form': form, 'apts': apts}
    return render(request, 'fazer_reserva.html', context)


def exibir_reservas(request):
    apartamentos = Apartamentos.objects.all()
    reservas_por_apartamento = {}

    for apartamento in apartamentos:
        reservas = Reservas.objects.filter(
            nome_apartamento=apartamento
        ).order_by('data_entrada')
        reservas_por_apartamento[apartamento] = reservas

    return render(
        request,
        'exibir_reservas.html',
        {'reservas_por_apartamento': reservas_por_apartamento},
    )


# ...


def consultar_datas_para_reserva(request):
    apts = []
    aptos = Apartamentos.objects.all()
    for i in range(len(aptos)):
        apts.append(i)
    if request.method == 'POST':
        form = FormConsultarReservas(request.POST)
        if form.is_valid():
            apartamento = form.cleaned_data['nome_apartamento']
            entrada = form.cleaned_data['data_entrada']
            saida = form.cleaned_data['data_saida']

            entrada_str = entrada.strftime('%d/%m/%Y')
            saida_str = saida.strftime('%d/%m/%Y')

            # Filtro or apartamento e verifica se datas para reservas ativas
            reservas_ativas = Reservas.objects.filter(
                nome_apartamento=apartamento,
                data_entrada__lte=saida,
                data_saida__gte=entrada,
            )

            if reservas_ativas:
                messages.error(
                    request,
                    f"***Já existem reservas para o apartamento '{apartamento}' nestas datas/ data entrada = {entrada_str},  data saida = {saida_str} ***",
                )
                print(reservas_ativas)
                context = {
                    'form': form,
                    'apts': apts,
                    'reservas_ativas': reservas_ativas,
                }
                return render(request, 'consultar_reservas.html', context)

            else:
                messages.success(
                    request,
                    f"***Não existem reservas para o apartamento '{apartamento}' nestas datas/ data entrada = {entrada_str},  data saida = {saida_str} ***",
                )
                return redirect('consultar_reservas')

        else:
            redirect('consultar_reservas')

    else:
        form = FormConsultarReservas()

    context = {'form': form, 'apts': apts}
    return render(request, 'consultar_reservas.html', context)


def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reservas, id=reserva_id)
    if request.method == 'POST':
        form = FormEditarReserva(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('exibir_reservas')
    else:
        form = FormEditarReserva(instance=reserva)
    return render(request, 'editar_reserva.html', {'form': form})


def excluir_reserva(request, reserva_id):
    reserva = get_object_or_404(Reservas, id=reserva_id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('exibir_reservas')
    return render(request, 'excluir_reserva.html', {'reserva': reserva})
