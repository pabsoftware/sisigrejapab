
from django.shortcuts import render, redirect

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


def doacoes_add(request):
    template_name = 'igreja/doacoes_form.html'
    form = Doacoes_form(request.POST, request.FILES)
    
    if request.method == "POST":   
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, template_name, context)


def denominacao_add(request):
    template_name = 'igreja/denominacao_form.html'
    form = denominacao_form(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form} 
    return render(request, template_name, context)
