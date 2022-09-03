
from xml.dom.minidom import Document
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import denominacao_add, doacoes_add, sobreigreja_add

urlpatterns = [

    path('sobrenos/', sobreigreja_add, name="sobreigreja"),
    path('doacoes/', doacoes_add, name="doacoes"),
    path('denominacao/', denominacao_add, name="denominacao"),
] 

urlpatterns += static(settings.MEDIA_URL,
Document_root = settings.MEDIA_ROOT,)