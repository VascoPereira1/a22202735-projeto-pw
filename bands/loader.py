from bands.models import *
import json

Band.objects.all().delete()
Album.objects.all().delete()
Music.objects.all().delete()

with open('bands/json/bands.json') as f :
    bands = json.load(f)

    for band1 in bands:
        Band.objects.create(
            name = band1['name'],
            country = band1['country'],
            yearCreated = band1['yearCreated']
            )

with open('bands/json/albunsAndMusics.json') as f :
    data = json.load(f)


    for album_data in data:
        Album.objects.create(
            name = album_data['name'],
            band = Band.objects.get(name = album_data['band']),
            anoLancamento = album_data['anoLancamento']
            )

        for music_data in album_data['musics']:
            Music.objects.create(
                url = music_data['url'],
                name = music_data['name'],
                duration = music_data['duration'],
                album = Album.objects.get(name = album_data['name'])
                )




