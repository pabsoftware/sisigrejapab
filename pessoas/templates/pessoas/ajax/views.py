from multiprocessing import context
from re import template
from urllib import request
from django.shortcuts import get_object_or_404
from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from pessoas.forms import Pessoas_form, Cargo_Form
from pessoas.models import Cargo_Funcao, Pessoas
from core.filters import Pessoas_filters
from core.views import popular_select, load_areas, load_congregacoes
from congregacoes.models import Zonas


# Create your views here.
#---------------------------PESSOAS----------------------
# Lista pessoas cadastradas
def listar_pessoas(request):
    template_name = 'pessoas/pessoas_list.html'
    
    zonas_select = Zonas.objects.all().order_by('zona')
    areas_select = []
    congregacoes_select = []
    
    context = {
       }

    pesquisa_nome = request.GET.get('nome_input', None)
    pesq_cargo = request.GET.get('cargo_input', None)
    
    
    if (pesquisa_nome or pesq_cargo):
        object_list = Pessoas.objects.all().filter(primeiro_nome__contains=pesquisa_nome)
        print('pesquisa passando')
    else:
        print('nada encontrado')
        object_list = Pessoas.objects.all()
        
    
    
  

   # form = Pessoas_form
    context = {
        'object_list': object_list,
        'zonas_select': zonas_select, 
        'areas_select': areas_select, 
        'congregacoes_select': congregacoes_select}
    return render(request, template_name, context)

#Filter Lista pessoas cadastradas
def pessoas_list(request):
    template_name = 'pessoas/pessoas_filter_lista.html'
    object_list = Pessoas.objects.all()
    pessoa_list = Pessoas_filters(request.GET, queryset=object_list)
  

   # form = Pessoas_form
    context = {'object_list': object_list, 'filter': pessoa_list}
    return render(request, template_name, context)


#Cria novo cadastro
def pessoas_cad(request):
    template_name = 'pessoas/pessoa_form.html'
    form = Pessoas_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    
    context = {'form' : form}
    return render(request, template_name, context)



#Editar pessoas
def editar_pessoas(request, id):
    template_name ='pessoas/pessoa_form.html'
    pessoa = Pessoas.objects.get(pk=id)
    form = Pessoas_form(request.POST or None, instance=pessoa)

    if request.method =='POST':
        
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    context = {'form': form}
    return render(request, template_name, context)



#deleta pessoas
def deleta_pessoas(request, id):
    pessoas =get_object_or_404(Pessoas, pk=id)
    if request.method == 'POST':
        pessoas.delete()
        return redirect('listar_pessoas')
    context = {
        "object":pessoas
    }
    return render(request, 'pessoas/confirm_delete.html', context)

def pessoas_detalhes(request, id):
    template_name = 'pessoas/pessoas_detalhes.html'
    pessoa  = get_object_or_404(Pessoas, pk=id)
    context = {'object':pessoa}
    return render(request,template_name, context)


#-------------------CARGOS------------------------------
# Lista cargo e funcoes cadastradas
def listar_cargo(request):
    template_name = 'pessoas/cargo/cargo_lista.html'
    
    pesquisa = request.GET.get('nome_input', None)
    if pesquisa:
        object_list = Cargo_Funcao.objects.all().filter(cargo=pesquisa)
        print('pesquisa passando')
    else:
        print('nada encontrado')
        object_list = Cargo_Funcao.objects.all()
        
    
    context = {'object_list': object_list}
    return render(request, template_name, context)


#Cria novo cadastro funcao
def cadastrar_cargo(request):
    template_name = 'pessoas/cargo/cargo_form.html'
    form = Cargo_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_cargos')
    
    context = {'form' : form}
    return render(request, template_name, context)


#Editar cargo
def editar_cargos(request, id):
    template_name ='pessoas/cargo/cargo_form.html'
    pessoa = Cargo_Funcao.objects.get(pk=id)
    form = Cargo_Form(request.POST or None, instance=pessoa)

    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('listar_cargos')
        
    context = {'form': form}
    return render(request, template_name, context)


#deleta cargos
def deletar_cargos(request, id):
    pessoas =get_object_or_404(Cargo_Funcao, pk=id)
    
    if request.method == 'POST':
        pessoas.delete()
        return redirect('listar_cargos')
    
    context = {
        "object":pessoas
    }
    return render(request, 'pessoas/cargo/confirm_delete.html', context)

