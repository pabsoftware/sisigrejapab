
from django.urls import path

from .views import sobreigreja

urlpatterns = [

    path('sobrenos/', sobreigreja, name="sobreigreja"),
]