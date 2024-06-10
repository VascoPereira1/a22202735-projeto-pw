import zipfile
import os

def descomprimir_arquivo_zip(caminho_zip, pasta_destino):
    """
    Descomprime o arquivo ZIP para a pasta de destino.

    :param caminho_zip: Caminho do arquivo ZIP.
    :param pasta_destino: Pasta onde os arquivos serão extraídos.
    """
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)
    print(f"Arquivos extraídos para {pasta_destino}")

# Exemplo de uso
if __name__ == "__main__":
    caminho_zip = 'meteo/static/meteo/icons_ipma_weather.zip'  # Substitua pelo caminho do seu arquivo ZIP
    pasta_destino = 'meteo/static/meteo/'  # Substitua pelo caminho do diretório de destino
    descomprimir_arquivo_zip(caminho_zip, pasta_destino)
