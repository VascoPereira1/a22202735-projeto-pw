from django.shortcuts import render
import requests

def obter_lista_locais():

    url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        return dados.get('data', [])
    except requests.RequestException as e:
        print(f"Erro ao acessar a API do IPMA: {e}")
        return None


def obter_id_local(cidade):

    locais = obter_lista_locais()
    if locais is None:
        return None

    for local in locais:
        if local['local'].lower() == cidade.lower():
            return local['globalIdLocal']

    return None

def obter_descricao_tempo ():

    url = "https://api.ipma.pt/open-data/weather-type-classe.json"
    response = requests.get(url)

    if response.status_code == 200:
        dic_dados = response.json()

    return dic_dados



def listPortfolio_view(request):

    globalIdLocal = obter_id_local("Lisboa")
    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{globalIdLocal}.json"
    response = requests.get(url)

    if response.status_code == 200:
        dic_dados = response.json()


    return render(request, 'listPortfolio.html', {'dados': dic_dados, 'descricao_tempo' : obter_descricao_tempo ()})

def listCV_view (request):

    return render(request, 'listCV.html', {})


def listCadeira_view(request):

    return render(request, 'listCadeira.html', {})
