from unicodedata import name
from django.urls import path
from cadastros.views import (
   
    
    listar_congregacoes,
    cadastrar_congregacoes,
    editar_congregacoes,
    deletar_congregacoes,
    galeria_congregacoes,
    
    listar_areas,
    cadastrar_areas,
    editar_area,
    deletar_areas,

    listar_zonas,
    cadastrar_zonas, 
    cadastrar_cargo,
    deletar_cargos, 
    editar_cargos, 
    listar_cargo
    
    )

urlpatterns = [

path('lista_cong/', listar_congregacoes, name="listar_congregacoes"),
path('novo_cong/', cadastrar_congregacoes, name = "cadastrar_congregacoes"),
path('editar_cong/<int:id>', editar_congregacoes, name='editar_congregacoes'),
path('delete_cong/<int:id>', deletar_congregacoes, name='deletar_congregacoes'),
path('galeria_cong/', galeria_congregacoes, name='galeria_congregacoes'),

path('lista_area/', listar_areas, name = 'listar_areas'),
path('nova_area/', cadastrar_areas, name='cadastrar_areas'),
path('editar_area/<int:id>', editar_area, name = 'editar_areas' ),
path('deletar_area/<int:id>', deletar_areas, name= 'deletar_areas'),

path('listar_zona/', listar_zonas, name='listar_zonas'),
path('cadastra_zonas/', cadastrar_zonas, name='cadastrar_zonas'),


path('listar_cargo/', listar_cargo, name='listar_cargos'),
path('novo_cargo/', cadastrar_cargo, name='cadastrar_cargos'),
path('editar_cargo/<int:id>', editar_cargos, name='editar_cargos'),
path('deletar_cargo/<int:id>', deletar_cargos, name='deletar_cargos'),

]