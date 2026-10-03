from django.db import models


class Ocorrencia(models.Model):
    CATEGORIAS = [
        ('Eletrica', 'Elétrica'),
        ('Hidraulica', 'Hidráulica'),
        ('Mobiliario', 'Mobiliário'),
        ('Limpeza', 'Limpeza'),
        ('Equipamento', 'Equipamento'),
        ('Outro', 'Outro'),
    ]

    PRIORIDADES = [
        ('Baixa', 'Baixa'),
        ('Media', 'Média'),
        ('Alta', 'Alta'),
    ]

    STATUS = [
        ('Pendente', 'Pendente'),
        ('Em analise', 'Em análise'),
        ('Resolvido', 'Resolvido'),
    ]

    local = models.CharField(max_length=100)

    categoria = models.CharField(
        max_length=30,
        choices=CATEGORIAS
    )

    descricao = models.TextField()

    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pendente'
    )

    foto = models.ImageField(
        upload_to='ocorrencias/',
        blank=True,
        null=True
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.local} - {self.categoria}"