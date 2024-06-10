from django.contrib import admin
from django.urls import path, include


urlpatterns = [path('admin/', admin.site.urls), path('', include('portfolio.urls')), path('noobsite/', include('noobsite.urls')), path('pwsite/', include('pwsite.urls')), path('novaapp/', include('novaapp.urls')), path('AppBandas/', include('bands.urls')), path('BlogApp/', include('BlogApp.urls')),path('AppCurso/',include('curso.urls')),path('AppFestivais/', include('festivais.urls')), path('Autenticacao/', include('Autenticacao.urls')), path('meteo/', include('meteo.urls')), ]
