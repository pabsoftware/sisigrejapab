from django import forms
from .models import Cargo_Funcao, Congregacoes, Areas, Zonas


class Cargo_Form(forms.ModelForm):
    class Meta:
        model = Cargo_Funcao
        fields = (
            'cargo',
            'obs',
        )


class Congregacoes_form(forms.ModelForm):
    class Meta:
        model = Congregacoes
        fields = (
            'nome',
            'zona',
            'area',
            'dirigente',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
            'cep',
            'country',
            'observacao',
        )


class Area_form(forms.ModelForm):
    class Meta:
        model = Areas
        fields = (
            'area',
            'zona',
            'responsavel',
            'descricao',
        )


class Zona_Form(forms.ModelForm):
    class Meta:
        model = Zonas
        fields = (
            'zona',
            'zona_obs',
        )
