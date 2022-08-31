from django.urls import path, include
from .views import home, popular_select, load_areas, load_congregacoes

urlpatterns = [

    path('', home, name='home'),
    path('select/', popular_select, name='popular_select'),
    path('ajax/load_areas', load_areas, name='ajax_load_areas'),
    path('ajax/load_congregacoes/', load_congregacoes,
         name='ajax_load_congregacoes')


]
