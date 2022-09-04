
from django.db import models
from cadastros.models import Areas, Congregacoes, Zonas, Cargo_Funcao
from usuarios.models import CustonUserModel
from core.models import (
    Active,
    Address,
    Document,
    TimeStampedModel,
    UuidModel,
    Situaco_na_igreja,


)


# Create your models here.


class Pessoas(UuidModel, Situaco_na_igreja, Document, Address, Active, TimeStampedModel):
    SEXO_CHOICES = (
        ("Masculino", "Masculino"),
        ("Feminino", "Feminino")
    )

    ESCOLARIDADE_CHOICES = (
        ("Analfabeto", "Analfabeto"),
        ("Até 5º ano", "Até 5º ano"),
        ("5º ano complte", "5º ano completo"),
        ("Fundamental Completo", "Fundamental Completo"),
        ("Médio Incompleto", "Médio Incompleto"),
        ("Médio Completo", "Médio Completo"),
        ("Superior Incompleto", "Superior Incompleto"),
        ("Superior Completo", "Superior Completo"),
        ("Mestrado", "Mestrado"),
        ("Doutorado", "Doutorado"),
        ("Ignorado", "Ignorado")

    )

    STATUS_CHOICES = (
        ("Em comunhão", "Em comunhão"),
        ("Disciplinado", "Disciplinado"),
        ("Afastado", "Afastado"),
        ("Desviado", "Desviado"),
        ("Observação", "Observacao")

    )
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, null=True)
    nome = models.CharField(max_length=200, blank=False, null=True)
    data_nasc = models.DateField(
        null=True, blank=False, auto_now=False, auto_now_add=False)
    sexo = models.CharField(
        max_length=20, choices=SEXO_CHOICES, blank=True, null=True)
    pai = models.CharField(max_length=200, blank=True, null=True)
    mae = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    cargo = models.ForeignKey(
        Cargo_Funcao, on_delete=models.CASCADE, related_name='cargo_atual', null=True)
    funcao = models.ForeignKey(Cargo_Funcao, on_delete=models.CASCADE,
                               related_name='funcao_que_exerce', blank=True, null=True)
    zona = models.ForeignKey(Zonas, on_delete=models.CASCADE, null=True)
    area = models.ForeignKey(Areas, on_delete=models.CASCADE, null=True)
    congregacao = models.ForeignKey(
        Congregacoes, on_delete=models.CASCADE, null=True)
    dizimista = models.BooleanField(blank=True, null=True)
    nivel_escolaridade = models.CharField(
        max_length=60, choices=ESCOLARIDADE_CHOICES, blank=True, null=True)
    usuario = models.OneToOneField(CustonUserModel, on_delete=models.CASCADE)
    foto = models.FileField(upload_to="img/usuarios/", null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoas'

    def __str__(self):
        return self.nome
