from django.db import models


class Departamento (models.Model):
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome

class AreaCientifica (models.Model):
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome

class Disciplina (models.Model):
    nome = models.CharField(max_length = 50)
    areaCientifica = models.ForeignKey(AreaCientifica, on_delete = models.CASCADE, related_name = 'Disciplina')
    ano = models.IntegerField()
    semestre = models.CharField(max_length = 50)
    ects = models.IntegerField()
    curricularUnitReadableCode = models.CharField(max_length = 50)
    docentes = models.ManyToManyField(Docente, related_name = 'Disciplinas', blank=True, null=True)
    linguagensProgramacao = models.ManyToManyField(LinguagemProgramacao , related_name = 'Disciplinas', blank=True, null=True)


    def __str__(self):
        return self.nome

class Curso (models.Model):
    nome = models.CharField(max_length = 50)
    apresentacao = models.TextField()
    objectivos = models.TextField()
    competencias = models.TextField()
    departamento =  models.ForeignKey(Departamento, on_delete = models.CASCADE, related_name = 'Curso')
    condicoesAcesso = models.TextField()
    oportunidadesCarreira = models.TextField()
    disciplinas = models.ManyToManyField(Disciplina, related_name = 'Curso')
    imagem = models.ImageField(upload_to='app/fotos', null=True, blank=True)

    def __str__(self):
        return self.nome

class Projeto (models.Model):
    disciplina = models.OneToOneField(Disciplina, on_delete = models.CASCADE, related_name = 'Projeto')
    descricao = models.TextField()
    conceitosAplicados = models.TextField()
    tecnologiasUtilizadas = models.TextField()
    linguagensProgramacao = models.ManyToManyField(LinguagemProgramacao , related_name = 'Projetos')
    imagem = models.ImageField(null = True, blank = True)
    linkYoutube = models.URLField()
    linkGitHub = models.URLField()








