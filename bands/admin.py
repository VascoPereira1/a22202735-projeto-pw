from django.contrib import admin
from .models import Band
from .models import Album
from .models import Music

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country' , 'yearCreated',)
    search_fields = ('name', 'yearCreated',)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ( 'name' , 'band', 'anoLancamento',)
    search_fields = ('name', 'band', 'anoLancamento',)

class MusicAdmin(admin.ModelAdmin):
    list_display = ('url', 'name' , 'album', 'duration',)
    search_fields = ('url', 'name' , 'album', 'duration',)




admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Music, MusicAdmin)