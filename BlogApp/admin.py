from django.contrib import admin
from .models import artigos
from .models import comentarioRating
from .models import infoAdicionalUser



admin.site.register(artigos)
admin.site.register(comentarioRating)
admin.site.register(infoAdicionalUser)
