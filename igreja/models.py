
from multiprocessing.dummy import active_children
from django.db import models
from pessoas.models import Pessoas
from core.models import Active, Address
# Create your models here.


class denominacao(Active, Address):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'denominacao'
        db_table = 'denominacao'

    def __str__(self):
        return self.titulo_sobre


class SobreIgreja():

    ASSUNTO_CHOICES = (
        ("Nossa visão", "Nossa visão"),
        ("Em que cremos", "Em que cremos"),
        ("Hstória", "História"),
        ("outro", "outro")

    )
    assunto = models.CharField(max_length=100, choices=ASSUNTO_CHOICES)
    titulo_sobre = models.CharField(max_length=120, blank=True, null=True)
    sub_titulo_sobre = models.CharField(max_length=120, blank=True, null=True)
    sobre = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'SobreIgreja'
        db_table = 'SobreIgreja'

    def __str__(self):
        return self.titulo_sobre
