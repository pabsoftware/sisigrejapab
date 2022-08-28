from django.contrib import admin
from pessoas.models import Pessoas

# Register your models here.

class PessoasAdimn(admin.ModelAdmin):
    model = Pessoas
    list_display= ['nome', 'cpf','congregacao', 'situacao','status']
    search_fields = ['nome',"foreinkeyfield__congregacao"]

admin.site.register(Pessoas, PessoasAdimn)
