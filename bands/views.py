from django.shortcuts import render ,redirect
from .forms import BandForm, AlbumForm, MusicForm
from .models import Music, Album, Band
from django.contrib.auth.decorators import login_required

@login_required
def nova_banda_view(request):
    form = BandForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bands:bandas')
    context = {'form': form}

    return render(request, 'novaBanda.html', context)


@login_required
def edita_banda_view(request,  band_name):
    banda = Band.objects.get(name = band_name)

    if request.POST:
        form = BandForm(request.POST or None, request.FILES, instance = banda)
        if form.is_valid():
            form.save()
            return redirect('bands:banda' , banda)
    else:
        form = BandForm(instance = banda)  # cria formulário com dados da instância autor

    context = {'form': form, 'banda':banda}
    return render(request, 'editaBanda.html', context)


@login_required
def apaga_banda_view(request, band_name):
    banda = Band.objects.get(name = band_name)
    banda.delete()
    return redirect('bands:bandas')



@login_required
def novo_album_view(request, band_name):
    banda = Band.objects.get(name = band_name)

    form = AlbumForm(request.POST or None, request.FILES)

    bandaNome = band_name
    if form.is_valid():
        form.save()
        return redirect('bands:banda' , bandaNome)
    context = {'form': form, 'banda' : banda}

    return render(request, 'novoAlbum.html', context)


@login_required
def edita_album_view(request,  album_name):
    album = Album.objects.get(name = album_name)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bands:album', album)
    else:
        form = AlbumForm(instance=album)  # cria formulário com dados da instância autor

    context = {'form': form, 'album':album}
    return render(request, 'editaAlbum.html', context)



@login_required
def apaga_album_view(request, album_name):
     album = Album.objects.get(name = album_name)
     album.delete()
     return redirect('bands:banda' , album.band)


@login_required
def nova_musica_view(request, album_name):
    form = MusicForm(request.POST or None, request.FILES)
    album = album_name
    if form.is_valid():
        form.save()
        return redirect('bands:album', album)
    context = {'form': form}

    return render(request, 'novaMusica.html',context)


@login_required
def edita_musica_view(request,  musica_name):
    musica = Music.objects.get(name = musica_name)

    if request.POST:
        form = MusicForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bands:musica', musica)
    else:
        form = MusicForm(instance=musica)  # cria formulário com dados da instância autor

    context = {'form': form, 'musica':musica}
    return render(request, 'editaMusica.html', context)


@login_required
def apaga_musica_view(request, musica_name):
    musica = Music.objects.get(name = musica_name)
    musica.delete()
    return redirect('bands:album', musica.album )


def musica_view(request, music_name):
    context = {
        'music' : Music.objects.get(name = music_name),
    }
    return render(request, 'music.html', context)


def listMusics_view(request, album_name):
    context = {
        'musics' : Music.objects.filter(album__name = album_name),
        'album' : Album.objects.get(name = album_name),
    }
    return render(request, 'album.html', context)


def listAlbums_view(request, band_name):
    context = {
        'albuns' : Album.objects.filter(band__name = band_name),
        'band' : Band.objects.get(name = band_name),
    }
    return render(request, 'band.html', context)

def homePage_view(request):
    context = {}
    return render(request, 'homePage.html',context)

def listBands_view(request):
    context = {
        'bands' : Band.objects.all(),
    }
    return render(request, 'listBands.html', context)





