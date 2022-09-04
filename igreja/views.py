
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *

# Create your views here.


def sobreigreja_add(request):
    template_name = 'igreja/sobreigreja_form.html'
    form = SobreIgreja_form(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, template_name, context)

# =============== DOACOES ==========================
def doacoes_add(request):
    template_name = 'igreja/doacoes_form.html'
    form = Doacoes_form(request.POST, request.FILES)
    
    if request.method == "POST":   
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_doacoes')
    
    context = {'form':form}
    return render(request, template_name, context)

def metodo_doacoes(request):
    template_name = 'igreja/metodo_doacoes.html'
    object = Doacoes.objects.all()

    context = {'object': object}
    return render(request, template_name, context)


def list_doacoes(request):
    template_name = 'igreja/doacoes_lista.html'
    object = Doacoes.objects.all()

    context = {'object': object}
    return render(request, template_name, context)

def doacoes_edit(request, id):
    template_name = 'igreja/doacoes_form.html'
    doacoes= get_object_or_404(Doacoes, pk=id)
    
    form = Doacoes_form(instance=doacoes)
    
    if request.method == "POST":  
        form = Doacoes_form(request.POST, request.FILES, instance=doacoes) 
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_doacoes')
    
    context = {'form':form}
    return render(request, template_name, context)
#===================FIM DOACOES ========================

#===================DENOMINACAO ========================
def denominacao_add(request):
    template_name = 'igreja/denominacao_form.html'
    form = denominacao_form(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form} 
    return render(request, template_name, context)


#===================FIM DENOMINACAO ========================

#=================== CONTATO ========================
def contatos_add(request):
    template_name = 'igreja/contato_msg_form.html'
    form = Contatos_msg_form(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form} 
    return render(request, template_name, context)

def list_dmensagens(request):
    template_name = 'igreja/mensagem_list.html'
    object = Contatos_Msg.objects.all()

    context = {'object': object}
    return render(request, template_name, context)


#===================FIM CONTATO ========================
