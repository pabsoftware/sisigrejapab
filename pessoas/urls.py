from os import name
from django import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pessoas.views import (
    home,
    listar_pessoas,
    deleta_pessoas,
    editar_pessoas,
    pesquisar_pelo_nome,
    pesquisar_pessoas,
    pessoas_cad,
    pessoas_detalhes,
    pessoas_detalhes_perfil,
    editar_perfil_pessoas
)
urlpatterns = [
    path('', home, name='home'),
    path('listar', listar_pessoas, name='listar_pessoas'),
    path('pesquisar/', pesquisar_pessoas, name='pesquisar_pessoas'),
    path('novo/', pessoas_cad, name='cadastrar_pessoas'),
    path('delete/<int:id>', deleta_pessoas, name='deleta_pessoas'),
    path('editar/<int:id>', editar_pessoas, name='editar_pessoas'),
    path('detalhes/<int:id>', pessoas_detalhes, name='pessoa_detalhes'),
    path('pesquisa_nome/', pesquisar_pelo_nome, name='pesq_nome'),
    path('perfil_detalhes/', pessoas_detalhes_perfil, name='perfil_detalhes'),
    path('editar_perfil/', editar_perfil_pessoas, name='editar_perfil_pessoa'),

]
urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT,)
