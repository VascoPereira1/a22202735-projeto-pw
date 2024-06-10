from django import forms
from .models import Band, Album, Music

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = '__all__'