
from django import forms
from pessoas.models import Pessoas


from pessoas.models import Pessoas, Cargo_Funcao

class Pessoas_form(forms.ModelForm):
    data_nasc = forms.DateField(label='Data de nascimento', required=False,
                widget=forms.DateInput(
                    format='%Y-%m-%d',
                    attrs={
                        'type' : 'date'
                    }
                ),
                input_formats=('%Y-%m-%d',),
                )

    data_batismo = forms.DateField(label='Data de batismo', required=False,
                widget=forms.DateInput(
                    format='%Y-%m-%d',
                    attrs={
                        'type' : 'date',
                        
                    }
                ),
                input_formats=('%Y-%m-%d',),
                )

    telefone = forms.CharField(required=False)
    mae = forms.CharField(required=False)
    pai = forms.CharField(required=False)
    
   

    class Meta:
        model = Pessoas
        #fields = "__all__"
        fields = (
            'active',
            'nome',
            'sexo',
            'rg',
            'cnh',
            'data_nasc',
            'pai',
            'mae',
            'email',
            'telefone',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
            'cep',
            'country',
            'situacao',
            'dizimista',
            'data_batismo',
            'status', 
            'zona',
            'area',
            'congregacao',
            'cargo',
            'funcao',
            'observacao'
            
        )
        
class Cargo_Form(forms.ModelForm):
    class Meta:
        model = Cargo_Funcao
        fields = (
            'cargo',
            'obs',
        )
    
