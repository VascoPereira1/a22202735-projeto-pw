from django.urls import path
from . import views

app_name = 'bands'
urlpatterns = [
    path('homePage', views.homePage_view, name = 'homePage'),
    path('', views.listBands_view, name = 'bandas'),
    path('banda/<str:band_name>', views.listAlbums_view, name = 'banda'),
    path('album/<str:album_name>', views.listMusics_view, name = 'album'),
    path('musica/<str:music_name>', views.musica_view, name = 'musica'),
    path('criarBanda/nova', views.nova_banda_view, name = 'nova_banda'),
    path('criarAlbum/novo/<str:band_name>', views.novo_album_view, name = 'novo_album'),
    path('criarMusica/nova/<str:album_name>', views.nova_musica_view, name = 'nova_musica'),
    path('editarBanda/<str:band_name>', views.edita_banda_view, name = 'edita_banda'),
    path('editarAlbum/<str:album_name>', views.edita_album_view, name = 'edita_album'),
    path('editarMusica/<str:musica_name>', views.edita_musica_view, name = 'edita_musica'),
    path('apagarBanda/<str:band_name>', views.apaga_banda_view, name = 'apaga_banda'),
    path('apagarAlbum/<str:album_name>', views.apaga_album_view, name = 'apaga_album'),
    path('apagarMusica/<str:musica_name>', views.apaga_musica_view, name = 'apaga_musica')
    ]


