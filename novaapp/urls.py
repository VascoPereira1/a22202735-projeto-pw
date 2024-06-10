# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('menu/pikachu/', views.pikachu_view, name='pikachu'),
    path('menu/charmander/', views.charmander_view, name='charmander'),
    path('menu/', views.menu_view, name = 'menu'),
]