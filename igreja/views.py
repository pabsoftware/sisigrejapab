
from django.shortcuts import render, redirect

from .models import Denominacao, Doacoes, SobreIgreja

# Create your views here.


def sobreigreja_add(request):
    template_name = 'igreja/sobreigreja_form.html'
    form = SobreIgreja(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, template_name, context)


def doacoes_add(request):
    template_name = 'igreja/doacoes_form.html'
    form = Doacoes(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, template_name, context)


def denominacao_add(request):
    template_name = 'igreja/denominacao_form.html'
    form = Denominacao(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, template_name, context)
