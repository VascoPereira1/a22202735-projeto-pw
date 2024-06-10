from django.db import models



class Localizacao (models.Model):
    nome = models.CharField(max_length = 100)

class Banda (models.Model):
    nome = models.CharField(max_length = 100)


class Festival (models.Model):
    nome = models.CharField(max_length = 100)
    imagem = models.ImageField(upload_to='app/fotos', null=True, blank=True)
    ano = models.IntegerField()
    localizacao = models.ForeignKey(Localizacao, on_delete = models.CASCADE, related_name = "Festivais")
    banda = models.ManyToManyField(Banda, related_name = 'Festivais')








