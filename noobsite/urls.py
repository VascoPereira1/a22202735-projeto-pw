from django.urls import path
from . import views  #importamos views para poder usar as funcoes

urlpatterns = [
    path('index/', views.index_view),
    path('benfica/', views.function_benfica),
    path('sporting/', views.function_sporting),
    path('porto/', views.function_porto),
    ]