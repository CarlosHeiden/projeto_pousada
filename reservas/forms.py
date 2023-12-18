from django import forms
from .models import Apartamentos, Reservas


class FormApt(forms.ModelForm):
    class Meta:
        model = Apartamentos
        fields = '__all__'

class FormReservas(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'

        