from socket import fromshare
from django import forms

from .models import CustonUserModel

class CardUserForm(forms.ModelForm):
    
    class Meta:
        model = CustonUserModel
        fields = ['first_name', 'last_name', 'email', 'cpf', 'username', 'password1']
