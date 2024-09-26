from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(default="Sem descrição")
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    tempo_preparo = models.PositiveIntegerField(
        # Para pratos que precisam de preparo
        help_text="Tempo de preparo em minutos", null=True, blank=True)
    categoria = models.CharField(
        max_length=50,
        choices=[('prato', 'Prato'), ('bebida', 'Bebida'),
                 ('sobremesa', 'Sobremesa')],
        default='prato'  # Definindo o valor padrão como "prato"
    )

    def __str__(self):
        return f'{self.nome} - R${self.preco}'


class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pendente')
    data_agendamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Pedido de {self.cliente} - {self.produto.nome}'


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.nome
