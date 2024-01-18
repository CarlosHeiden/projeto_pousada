from django.db import models


class Apartamentos(models.Model):
    nome = models.CharField(max_length=100)
    numero_pessoas = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nome} - {self.numero_pessoas}'


from django.db import models


class Reservas(models.Model):
    nome_cliente = models.CharField(max_length=100)
    nome_apartamento = models.ForeignKey(
        Apartamentos, on_delete=models.CASCADE
    )
    data_pgto_reserva = models.DateField()
    data_entrada = models.DateField()
    data_saida = models.DateField()
    preco_diaria = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    vl_pgto_reserva = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    taxa_limpeza = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    valor_total_diarias = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    saldo_a_pagar = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    def calcular_valor_total_diarias(self):
        # Calcula o valor total com base na lógica fornecida
        dias_reserva = (self.data_saida - self.data_entrada).days
        self.valor_total_diarias = dias_reserva * self.preco_diaria

    def calcular_saldo_a_pagar(self):
        # Calcular saldo a pagar
        self.saldo_a_pagar = (
            self.taxa_limpeza + self.valor_total_diarias
        ) - self.vl_pgto_reserva

    def save(self, *args, **kwargs):
        # Antes de salvar, chama o método para calcular o valor total_diarias e calcular_saldo_a_pagar
        self.calcular_valor_total_diarias()
        self.calcular_saldo_a_pagar()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.nome_cliente} - {self.nome_apartamento} - {self.data_pgto_reserva} - {self.data_entrada} - {self.data_saida} - {self.preco_diaria} - {self.vl_pgto_reserva} - {self.taxa_limpeza} - {self.valor_total_diarias} - {self.saldo_a_pagar}'
