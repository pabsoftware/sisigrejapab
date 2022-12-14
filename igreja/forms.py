from dataclasses import fields
import email
from .models import *
from django import forms
from django.forms.widgets import ClearableFileInput


class Doacoes_form(forms.ModelForm):
    foto = forms.ImageField(widget=ClearableFileInput, required=False)

    class Meta:
        model = Doacoes
        fields = (
            'descricao',
            'tipo_conta',
            'banco',
            'titular',
            'agencia',
            'conta',
            'variacao',
            'variacao',
            'chave_pix',
            'foto',


        )


class denominacao_form(forms.ModelForm):
    class Meta:
        model = Denominacao
        fields = ('nome',)


class SobreIgreja_form(forms.ModelForm):
    class Meta:
        model = SobreIgreja
        fields = '__all__'


class Contatos_msg_form(forms.ModelForm):
    msg = forms.Textarea()

    class Meta:
        model = Contatos_Msg
        fields = ('mensagem', 'nome', 'email',)
