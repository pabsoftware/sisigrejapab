from django.shortcuts import render
from cadastros.models import Areas, Congregacoes, Zonas, Cargo_Funcao
from cadastros.forms import Area_form, Congregacoes_form, Zona_Form, Cargo_Form
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required 

# Create your views here.
#--------------------------CONGREGACOES-----------------------------------
#lista congregacoes
@login_required
def listar_congregacoes(request):
    template_name  = 'cadastros/cong/congregacoes_lista.html'
    object_list = Congregacoes.objects.all().order_by('nome')

    context = {'object': object_list}
    return render(request, template_name, context)


#Cadastro de congregacoes
@login_required
def cadastrar_congregacoes(request):
    template_name = 'cadastros/cong/congregacoes_form.html'
    form = Congregacoes_form(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_congregacoes')

    context = {'form': form}
    return render(request, template_name, context)


#deletar congregacoes
@login_required
def deletar_congregacoes(request, id):
    congregacoes = get_object_or_404(Congregacoes, pk=id)
    
    if request.method == 'POST':
        congregacoes.delete()
        return redirect('listar_congregacoes')
    
    context ={'object':congregacoes}
    return render(request, 'cadastros/cong/cong_confirm_delete.html', context)


#editar congregacoes
@login_required
def editar_congregacoes(request, id):
    template_name = 'cadastros/cong/congregacoes_form.html'
    congregacoes = get_object_or_404(Congregacoes, pk=id) 
    form = Congregacoes_form(request.POST or None, instance=congregacoes)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_congregacoes')
    context = {'form': form}
    return render(request, template_name, context)

def galeria_congregacoes(request):
    template_name = 'cadastros/cong/galeria_cong.html'
    object_list = Congregacoes.objects.all().order_by('nome')
    context = {'object_list' : object_list}
    return render(request, template_name, context)
         
    
#--------------------------AREAS-----------------------------------
#lista areas
@login_required
def listar_areas(request):
    template_name = 'cadastros/area/area_lista.html'
    object_list = Areas.objects.all().order_by('area')

    context = {'object': object_list}
    return render(request, template_name, context)


#Cadastro de areas
@login_required
def cadastrar_areas(request):
    template_name = 'cadastros/area/area_form.html'
    form = Area_form(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_areas')

    context = {'form': form}
    return render(request, template_name, context)


#editar areas
@login_required
def editar_area(request, id):
    template_name = 'cadastros/area/area_form.html'
    area = get_object_or_404(Areas, pk=id)
    form = Area_form(request.POST or None, instance=area)
    
    if request.method == 'POST':
        form.save()
        return redirect('listar_areas')
    
    context = {'form': form}
    return render(request, template_name, context)


#deletar areas
@login_required
def deletar_areas(request, id):
    area = get_object_or_404(Areas, pk=id)
       
    if request.method == 'POST':
        area.delete()
        return redirect('listar_areas')
    
    context = {'object': area}
    return render(request, 'cadastros/area/area_confirm_delete.html', context)


#--------------------------ZONAS-----------------------------------
#Listar zonas
@login_required
def listar_zonas(request):
    template_name = 'cadastros/zona/zona_lista.html'
    zonas = Zonas.objects.all().order_by('zona')
    
    context = {'object': zonas}
    return render(request, template_name, context)


#cadastrar zonas
@login_required
def cadastrar_zonas(request):
    template_name = 'cadastros/zona/zona_form.html'
    form = Zona_Form(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_zonas')

    context = {'form': form}
    return render(request, template_name, context)


#-------------------CARGOS------------------------------
# Lista cargo e funcoes cadastradas
@login_required
def listar_cargo(request):
    template_name = 'cadastros/cargo/cargo_lista.html'
    
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
@login_required
def cadastrar_cargo(request):
    template_name = 'cadastros/cargo/cargo_form.html'
    form = Cargo_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_cargos')
    
    context = {'form' : form}
    return render(request, template_name, context)


#Editar cargo
@login_required
def editar_cargos(request, id):
    template_name ='cadastros/cargo/cargo_form.html'
    pessoa = Cargo_Funcao.objects.get(pk=id)
    form = Cargo_Form(request.POST or None, instance=pessoa)

    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('listar_cargos')
        
    context = {'form': form}
    return render(request, template_name, context)


#deleta cargos
@login_required
def deletar_cargos(request, id):
    pessoas =get_object_or_404(Cargo_Funcao, pk=id)
    
    if request.method == 'POST':
        pessoas.delete()
        return redirect('listar_cargos')
    
    context = {
        "object":pessoas
    }
    return render(request, 'cadastros/cargo/confirm_delete.html', context)


