from django.urls import path
from . import views

app_name = 'festivais'
urlpatterns = [
    path('', views.listFestivais_view, name = 'festivais'),
    path('festival/<str:festival_name>', views.listFestival_view,  name = 'festival'),
    ]
