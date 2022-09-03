
from django.urls import path

from .views import denominacao_add, doacoes_add, sobreigreja_add

urlpatterns = [

    path('sobrenos/', sobreigreja_add, name="sobreigreja"),
    path('doacoes/', doacoes_add, name="doacoes"),
    path('denominacao/', denominacao_add, name="denominacao"),
]