from django import forms
from .models import Apartamentos, Reservas


class FormApt(forms.ModelForm):
    class Meta:
        model = Apartamentos
        fields = '__all__'


class DateInput(forms.DateInput):
    # insere mini calendario nos campos de data
    input_type = 'date'


class FormMiniCalendario(forms.ModelForm):
    # campos para gerar formulario de cadastro de reserva
    nome_apartamento = forms.ModelChoiceField(
<<<<<<< HEAD
        queryset=Apartamentos.objects.all().order_by('nome')
=======
        queryset=Apartamentos.objects.all()
>>>>>>> 7e4f72a17fa080c3f621ebb2eba4e76fb9577b7c
    )
    data_pgto_reserva = forms.DateField(widget=DateInput())
    data_entrada = forms.DateField(widget=DateInput())
    data_saida = forms.DateField(widget=DateInput())

    class Meta:
        model = Reservas
        fields = [
            'nome_cliente',
            'nome_apartamento',
            'data_pgto_reserva',
            'data_entrada',
            'data_saida',
            'preco_diaria',
            'vl_pgto_reserva',
            'taxa_limpeza',
        ]


class FormConsultarReservas(forms.ModelForm):
    # formulário para consulta de reservas por apartamento e período
    nome_apartamento = forms.ModelChoiceField(
<<<<<<< HEAD
        queryset=Apartamentos.objects.all().order_by('nome')
=======
        queryset=Apartamentos.objects.all()
>>>>>>> 7e4f72a17fa080c3f621ebb2eba4e76fb9577b7c
    )
    data_entrada = forms.DateField(widget=DateInput())
    data_saida = forms.DateField(widget=DateInput())

    class Meta:
        model = Reservas
        fields = ['nome_apartamento', 'data_entrada', 'data_saida']


class FormEditarReserva(forms.ModelForm):
    # campos para gerar formulario para editar reserva
    nome_apartamento = forms.ModelChoiceField(
<<<<<<< HEAD
        queryset=Apartamentos.objects.all().order_by('nome')
=======
        queryset=Apartamentos.objects.all()
>>>>>>> 7e4f72a17fa080c3f621ebb2eba4e76fb9577b7c
    )
    data_pgto_reserva = forms.DateField()
    data_entrada = forms.DateField()
    data_saida = forms.DateField()

    class Meta:
        model = Reservas
        fields = [
            'nome_cliente',
            'nome_apartamento',
            'data_pgto_reserva',
            'data_entrada',
            'data_saida',
            'preco_diaria',
            'vl_pgto_reserva',
            'taxa_limpeza',
        ]
