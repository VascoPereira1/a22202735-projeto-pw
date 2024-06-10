from django.contrib import admin
from .models import Festival, Localizacao, Banda



class BandAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'ano')



admin.site.register(Banda, BandAdmin)
admin.site.register(Localizacao, LocalizacaoAdmin)
admin.site.register(Festival, FestivalAdmin)