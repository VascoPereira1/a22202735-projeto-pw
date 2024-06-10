from django.db import models

class Band (models.Model):
    name = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    yearCreated = models.IntegerField()
    biografia = models.TextField(default=' ', null=True, blank=True)
    imagem = models.ImageField(upload_to='app/fotos', null=True, blank=True)

    def __str__(self):
        return self.name



class Album (models.Model):
    name = models.CharField(max_length = 100)
    band  = models.ForeignKey(Band, on_delete = models.CASCADE)
    anoLancamento = models.IntegerField()
    imagemAlbum = models.ImageField(upload_to='app/fotos', null=True, blank=True)

    def __str__(self):
        return self.name


class Music(models.Model):
    url = models.URLField(max_length = 200)
    name = models.CharField(max_length = 100)
    duration = models.CharField(max_length = 10, default = ' ')
    album = models.ForeignKey(Album, on_delete = models.CASCADE, related_name = 'musics')
    letra = models.TextField(default=' ', null=True, blank=True)

    def __str__(self):
        return self.name