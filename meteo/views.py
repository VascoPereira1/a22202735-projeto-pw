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


def previsao_meteorologica(request, cidade):

    globalIdLocal = obter_id_local(cidade)


    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{globalIdLocal}.json"
    response = requests.get(url)


    if response.status_code == 200:
        dic_dados = response.json()


    return render(request, 'previsaoCidade.html', {'dados': dic_dados, 'descricao_tempo' : obter_descricao_tempo (), 'cidade' : cidade })

def previsao_meteorologica2(request, cidade):

    globalIdLocal = obter_id_local(cidade)


    url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{globalIdLocal}.json"
    response = requests.get(url)


    if response.status_code == 200:
        dic_dados = response.json()


    return render(request, 'previsaoCidade5dias.html', {'dados': dic_dados, 'descricao_tempo' : obter_descricao_tempo (), 'cidade' : cidade })

def list_cidades(request):

    url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(url)

    if response.status_code == 200:
        dic_dados = response.json()

    return render(request, 'listCidades.html', {'cidades': dic_dados})







