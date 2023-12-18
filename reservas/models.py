from django.db import models
from calendar import HTMLCalendar
from itertools import groupby
from datetime import timedelta

# Create your models here.
class Apartamentos(models.Model):
    nome = models.CharField(max_length=100)
    numero_pessoas = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nome} - {self.numero_pessoas}'
    
   
class Reservas(models.Model):
    nome_cliente = models.CharField(max_length=100)
    nome_apartamento = models.ForeignKey(Apartamentos, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    data_entrada = models.DateField()
    data_saida = models.DateField()
    preco_diaria = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    taxa_limpeza = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
 
    
    def __str__(self) -> str:
        return f'{self.nome_cliente} - {self.nome_apartamento} - {self.data_reserva} - {self.data_entrada} - {self.data_saida} - {self.preco_diaria} - {self.nome_cliente}'
    


class ReservaCalendar(HTMLCalendar):
    def __init__(self, reservas):
        super().__init__()
        self.reservas = self.group_by_day(reservas)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if day in self.reservas:
                cssclass += " reserva"
                body = []
                for reserva in self.reservas[day]:
                    body.append(f"<p>Entrada: {reserva.data_entrada}<br>Saída: {reserva.data_saida}</p>")
                return self.day_cell(cssclass, f"<span class='day-number'>{day}</span> {''.join(body)}")
            return self.day_cell(cssclass, f"<span class='day-number'>{day}</span>")
        return self.day_cell("noday", "&nbsp;")

    def formatmonth(self, year, month, withyear=True):
        self.year, self.month = year, month
        return super().formatmonth(year, month, withyear)

    def group_by_day(self, reservas):
        field = lambda reserva: reserva.data_reserva.day
        return {day: list(items) for day, items in  groupby(reservas, field)}

    def day_cell(self, cssclass, body):
        return f"<td class='{cssclass}'>{body}</td>"

