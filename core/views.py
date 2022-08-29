from django.shortcuts import render
from cadastros.models import Zonas, Areas, Congregacoes

# Create your views here.

def home(request):
    template_name = 'core/home.html'
    return render(request, template_name)


def popular_select(request):
    template_name = 'core/selects.html'
    zonas_select = Zonas.objects.all().order_by('zona')
    areas_select = []
    congregacoes_select = []
    
    context = {
        'zonas_select': zonas_select, 
        'areas_select': areas_select, 
        'congregacoes_select': congregacoes_select}
    return render(request, template_name, context)


def load_areas(request):
    template_name = 'core/fetch/areas_ajax.html'
    zona_id = request.GET.get('zona_id')
    areas =  Areas.objects.filter(zona_id=zona_id).all()
    context = {'areas_slect': areas}
    return render(request, template_name, context)


def load_congregacoes(request):
    template_name = 'core/fetch/congregacoes_ajax.html'
    area_id = request.GET.get('area_id')
    congregacoes =  Congregacoes.objects.filter(area_id=area_id).all()
    context = {'congregacoes_slect': congregacoes}
    return render(request, template_name, context)
