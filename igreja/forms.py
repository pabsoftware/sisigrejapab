from dataclasses import fields
from .models import *
from django import forms


class Doacoes_add(forms.ModelForm):
    class Meta:
        model=Doacoes
        fields = '__all__'


class denominacao_add(forms.ModelForm):
    class Meta:
        model = Denominacao
        fields = ('nome',)
        

class SobreIgreja(forms.ModelForm):
    class Meta:
        model = SobreIgreja
        fields = '__all__'