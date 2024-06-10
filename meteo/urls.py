from django.urls import path
from . import views

urlpatterns = [
    path('previsao/<str:cidade>/', views.previsao_meteorologica, name='previsao_meteorologica'),
    path('previsao5dias/<str:cidade>/', views.previsao_meteorologica2, name = 'previsao_meteorologica5dias'),
    path('cidades', views.list_cidades, name = 'cidades'),
]