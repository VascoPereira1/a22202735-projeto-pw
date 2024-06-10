from django.urls import path
from . import views


urlpatterns = [
    path('', views.listPortfolio_view, name = 'portfolio'),
    path('Programação Web/', views.listCadeira_view, name = 'cadeira'),
    path('Vasco Pereira/', views.listCV_view, name = 'Vasco Pereira'),
    ]
