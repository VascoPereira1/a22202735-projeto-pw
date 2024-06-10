from django.shortcuts import render
from .models import Localizacao, Banda, Festival


def listFestivais_view (request):
    context = {
        'localizacoes' : Localizacao.objects.all(),
        'festivais' : Festival.objects.all(),
    }
    return render(request, 'listFestivais.html', context)



def listFestival_view(request, festival_name):
    context = {
        'festival' : Festival.objects.get(nome = festival_name),
        'bandas' : Banda.objects.all(),
    }
    return render(request, 'listFestival.html', context)