from django.shortcuts import get_object_or_404
from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from pessoas.forms import Pessoas_form
from pessoas.models import Cargo_Funcao, Pessoas
from cadastros.models import Zonas
from usuarios.models import CustonUserModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


# Create your views here.
def home(request):
    template_name = 'core/index.html'
    return render(request, template_name)


def pesquisar_pelo_nome(request):
    template_name = 'pessoas/pessoas_filter_lista.html'
    nome = request.GET.get('nome_input', None)
    object_list = Pessoas.objects.all().filter(nome=nome)
    print('não econtrama', nome)

    context = {
        'object_list': object_list
    }
    return render(request, template_name, context)
# ---------------------------PESSOAS----------------------
# Lista pessoas cadastradas


@login_required
def listar_pessoas(request):

    template_name = 'pessoas/pessoas_list.html'

    cargos_select = Cargo_Funcao.objects.all().order_by('cargo')
    zonas_select = Zonas.objects.all().order_by('zona')
    areas_select = []
    congregacoes_select = []

    object_list = Pessoas.objects.all()

    context = {
        'cargos_select': cargos_select,
        'object_list': object_list,
        'zonas_select': zonas_select,
        'areas_select': areas_select,
        'congregacoes_select': congregacoes_select}
    return render(request, template_name, context)

# pesquisar pessoas cadastradas


def pesquisar_pessoas(request):
    template_name = 'pessoas/pessoas_filter_lista.html'

    zonas_select = Zonas.objects.all().order_by('zona')
    areas_select = []
    congregacoes_select = []

    pesquisa_nome = request.GET.get('pesquisa_nome', None)
    cargo_id = request.GET.get('cargo_id', None)
    zona_id = request.GET.get('zona_id', None)
    area_id = request.GET.get('area_id', None)
    congregacao_id = request.GET.get('congregacao_id', None)
    print(zona_id)
    object_list = Pessoas.objects.all()

    if pesquisa_nome:
        object_list = Pessoas.objects.all().filter(
            nome__contains=pesquisa_nome).order_by('nome')

    if zona_id:
        object_list = Pessoas.objects.all().filter(zona_id=zona_id).order_by('nome')

    if cargo_id:
        object_list = Pessoas.objects.all().filter(cargo_id=cargo_id).order_by('nome')

    if zona_id and area_id:
        object_list = Pessoas.objects.all().filter(
            zona_id=zona_id, area_id=area_id).order_by('nome')

    if zona_id and area_id and congregacao_id:
        object_list = Pessoas.objects.all().filter(zona_id=zona_id, area_id=area_id,
                                                   congregacao_id=congregacao_id).order_by('nome')

    if cargo_id and zona_id:
        object_list = Pessoas.objects.all().filter(
            zona_id=zona_id, cargo_id=cargo_id).order_by('nome')

    if cargo_id and zona_id and area_id:
        object_list = Pessoas.objects.all().filter(zona_id=zona_id, area_id=area_id,
                                                   cargo_id=cargo_id).order_by('nome')

    if zona_id and area_id and congregacao_id and cargo_id:
        object_list = Pessoas.objects.all().filter(zona_id=zona_id, area_id=area_id,
                                                   congregacao_id=congregacao_id, cargo_id=cargo_id).order_by('nome')

    if zona_id and area_id and congregacao_id and cargo_id and pesquisa_nome:
        object_list = Pessoas.objects.all().filter(zona_id=zona_id, area_id=area_id, congregacao_id=congregacao_id,
                                                   cargo_id=cargo_id, nome__contains=pesquisa_nome).order_by('nome')

    context = {
        'object_list': object_list,
        'zonas_select': zonas_select,
        'areas_select': areas_select,
        'congregacoes_select': congregacoes_select}
    return render(request, template_name, context)


# Cria novo cadastro
@login_required
def pessoas_cad(request):
    template_name = 'pessoas/pessoa_form.html'
    form = Pessoas_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')

    context = {'form': form}
    return render(request, template_name, context)


# Editar pessoas
@login_required
def editar_pessoas(request, id):
    template_name = 'pessoas/pessoa_form.html'
    pessoa = Pessoas.objects.get(pk=id)
    form = Pessoas_form(request.POST or None, request.FILES, instance=pessoa)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    context = {'form': form}
    return render(request, template_name, context)

# Editar perfil pessoas


@login_required
def editar_perfil_pessoas(request):
    template_name = 'pessoas/pessoa_form.html'
    u = request.user

    situacao = request.POST.get('situacao')
    print(situacao)
    pessoa = get_object_or_404(Pessoas, usuario=request.user.id)
    form = Pessoas_form(instance=pessoa)

    if request.method == 'POST':
        form = Pessoas_form(request.POST or None, request.FILES, instance=pessoa)

        if form.is_valid():
            form.save()
            if situacao == 'Membro':
                group = get_object_or_404(Group, name='Membros')
                u.groups.add(group)

            return redirect('perfil_detalhes')
    context = {'form': form}
    return render(request, template_name, context)


# deleta pessoas
@login_required
def deleta_pessoas(request, id):
    pessoas = get_object_or_404(Pessoas, pk=id)
    if request.method == 'POST':
        pessoas.delete()
        return redirect('listar_pessoas')
    context = {
        "object": pessoas
    }
    return render(request, 'pessoas/confirm_delete.html', context)


@login_required
def pessoas_detalhes(request, id):
    template_name = 'pessoas/pessoas_detalhes.html'
    # pega id do usuario
    u = request.user
    print(u.id)
    pessoa = get_object_or_404(Pessoas, pk=id)
    context = {'object': pessoa}
    return render(request, template_name, context)


@login_required
def pessoas_detalhes_perfil(request):
    template_name = 'pessoas/pessoas_detalhes.html'
    # pega id do usuario

    pessoa = get_object_or_404(Pessoas, usuario=request.user.id)

    context = {'object': pessoa}
    return render(request, template_name, context)
