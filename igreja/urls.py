
from xml.dom.minidom import Document
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import contatos_add, denominacao_add, doacoes_add, sobreigreja_add, metodo_doacoes, list_doacoes, doacoes_edit, list_dmensagens

urlpatterns = [

    path('sobrenos/', sobreigreja_add, name="sobreigreja"),
    path('add_doacoes/', doacoes_add, name="add_doacoes"),
    path('denominacao/', denominacao_add, name="denominacao"),
    path('doacoes/', metodo_doacoes, name="meto_doacoes"),
    path('list_doacoes/', list_doacoes, name="list_doacoes"),
    path('edit_doacoes/<int:id>', doacoes_edit, name="edit_doacoes"),
    path('conato/', contatos_add, name="contato_msg"),
    path('mensagens/', list_dmensagens, name="mensagens"),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT,)
