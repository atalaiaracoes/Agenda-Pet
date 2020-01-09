from django.db import models


class Servico(models.Model):

    codigo = models.IntegerField(null=True, blank=True)
    servico = models.CharField('Descrição do Serviço', max_length=200)
    tipo = models.CharField('Tipo do Pet', max_length=10)
    tamanho = models.CharField('Tamanho do Pet', max_length=10)
    valor = models.DecimalField('Valor do Serviço', max_digits=10, decimal_places=2, null=True, blank=True)
    ativo = models.BooleanField(null=True, blank=True)
    observacao = models.TextField('Observação', blank=True, null=True)
    cadastro = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.produto

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['servico']