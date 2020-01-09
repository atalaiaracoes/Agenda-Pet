from django.db import models



class Tutor(models.Model):

    tutor = models.CharField('Nome do Tutor', max_length=200)
    cpf = models.CharField('CPF', max_length=11, blank=True, null=True)
    tel_principal = models.CharField('Telefone Principal', max_length=20)
    tel_alternativo = models.CharField('Telefone Alternativo', max_length=20)
    email = models.CharField('E-mail', max_length=80)
    cont_alternativo = models.CharField('Contato Alternativo', max_length=200)
    tel_contato = models.CharField('Telefone do Contato', max_length=20)
    observacao = models.TextField('Observação', blank=True, null=True)
    cadastro = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.tutor

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'
        ordering = ['tutor']


class Pet(models.Model):

    pet = models.CharField('Nome do Pet', max_length=200)
    tipo = models.CharField('Tipo do Pet', max_length=20)
    raca = models.CharField('Raça do Pet', max_length=20)
    tamanho = models.CharField('Tamanho do Pet', max_length=20, null=True)
    cor = models.CharField('Cor do Pet', max_length=20)
    dt_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    tutor = models.CharField('Nome do Tutor', max_length=200)
    pet_alergico = models.BooleanField(null=True, blank=True)
    pet_cardiaco = models.BooleanField(null=True, blank=True)
    observacao = models.TextField('Observação', blank=True, null=True)
    cadastro = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.pet

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'
        ordering = ['tutor', 'pet']


class Raca(models.Model):

    raca = models.CharField('Raça do Pet', max_length=100)
    tipo = models.CharField('Tipo do Pet', max_length=20)
    porte = models.CharField('Porte do Pet', max_length=20, null=True)

    def __str__(self):
        return self.raca

    class Meta:
        verbose_name = 'Raça'
        verbose_name_plural = 'Raças'
        ordering = ['raca', 'porte']