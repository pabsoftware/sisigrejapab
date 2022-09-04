from socket import fromshare
from django import forms
from django.form.widgets import ClearableFileInput

from .models import CustonUserModel


class CardUserForm(forms.ModelForm):
    
    class Meta:
        model = CustonUserModel
        fields = ['first_name', 'last_name',
                  'email', 'cpf', 'username', 'password1']


class Foto_User_Form(forms.ModelForm):
    foto_user = forms.ImageField(widget=ClearableFileInput, required=False)
    class Meta:
        model = CustonUserModel
        fields = ("foto_user",)

