from django.db import models
from core.models import Address, UuidModel, Active, TimeStampedModel
# Create your models here.


class Cargo_Funcao(UuidModel):
    cargo = models.CharField(max_length=200,)
    obs = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'cargo_funcao'

    def __str__(self):
        return self.cargo


class Zonas(UuidModel):
    zona = models.CharField(max_length=200)
    zona_obs = models.TextField(blank=True)

    class Meta:
        db_table = 'zonas'

    def __str__(self):
        return self.zona


class Areas(UuidModel):
    area = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=200, blank=True, null=True)
    descricao = models.TextField(blank=True)
    zona = models.ForeignKey(Zonas, on_delete=models.CASCADE)

    class Meta:
        db_table = 'areas'
        ordering = ('area',)

    def __str__(self):
        return self.area


class Congregacoes(UuidModel, Address, Active, TimeStampedModel):
    nome = models.CharField(
        max_length=200, help_text='Informe o nome da congregação')
    dirigente = models.CharField(
        max_length=200, help_text='Informe o nome do dirigente da congregação')
    observacao = models.TextField(blank=True)
    zona = models.ForeignKey(Zonas, on_delete=models.CASCADE)
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)

    class Meta:
        db_table = 'congregacoes'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
