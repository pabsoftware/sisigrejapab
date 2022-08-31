from enum import unique
from django.db import models

from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCPFField
# Create your models here.


class CustonUserModel(AbstractUser):
    cpf = BRCPFField('CPF', unique=True, blank=False, null=False)
    email = models.EmailField(max_length=120, blank=False, null=False)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email']

    class Meta():
        db_table = 'usuarios'
