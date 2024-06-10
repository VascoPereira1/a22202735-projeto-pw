from django.db import models
from django.contrib.auth.models import User

class infoAdicionalUser(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'infoAdicionalUser')
    imagem = models.ImageField(upload_to='app/fotos', null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    dataNascimento = models.DateTimeField(auto_now = False, auto_now_add = False,null=True, blank=True)
    interesses = models.TextField()
    profissao = models.TextField()




class artigos(models.Model):
    autor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'artigos')
    titulo = models.CharField(max_length = 100)
    corpoDoArtigo = models.CharField(max_length = 1000)
    imagem = models.ImageField(upload_to='app/fotos', null=True, blank=True)
    horaPublicacao = models.DateTimeField(auto_now = False, auto_now_add = False)
    categoria = models.TextField(null = True, blank = True)
    introducao = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.titulo

class comentarioRating(models.Model):
    artigo = models.ForeignKey(artigos, on_delete = models.CASCADE, related_name = 'comentariosRatings')
    autor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comentariosRatings')
    comentario = models.CharField(max_length = 1000)
    rating = models.IntegerField()
    horaComentario =  models.DateTimeField(auto_now = False, auto_now_add = False)

