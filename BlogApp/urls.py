from django.urls import path
from . import views

app_name = 'artigos'
urlpatterns = [
    path('', views.listArtigos_view, name = 'artigos'),
    path('usuarios', views.listUsuarios_view, name = 'usuarios'),
    path('meusArtigos/', views.listMeusArtigos_view, name = 'meusArtigos'),
    path('usuario/<int:usuario_id>', views.listUsuario_view, name = 'usuario'),
    path('artigo/<str:artigo_name>', views.listArtigo_view, name = 'artigo'),
    path('criarArtigo/novo', views.novo_artigo_view, name = 'novo_artigo'),
    path('criarComentario/novo/<str:artigo_name>' , views.novo_comentario_view, name = 'novo_comentario'),
    path('editarArtigo/<str:artigo_name>', views.edita_artigo_view, name = 'edita_artigo'),
    path('editarComentario/<str:artigo_name>/<int:id>/', views.edita_comentario_view, name = 'edita_comentario'),
    path('editarUsuario', views.edita_usuario_view, name = 'edita_usuario'),
    path('adicionarInfoUsuario', views.novo_InformacaoUser_view, name = 'novo_usuario'),
    path('apagarArtigo/<str:artigo_name>', views.apaga_artigo_view, name = 'apaga_artigo'),
    path('apagarComentario/<str:artigo_name>/<int:id>/', views.apaga_comentario_view, name = 'apaga_comentario'),
    ]
