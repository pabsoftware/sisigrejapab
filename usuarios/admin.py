from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import CustonUserModel


# Register your models here.
class CustonUserAdmin(UserAdmin):
    model = CustonUserModel

    list_display = ['first_name', 'email', 'cpf']
    list_display_links = ['email', 'cpf']
    



admin.site.register(CustonUserModel, CustonUserAdmin)
