from django.contrib import admin
from .models import Departamento
from .models import Curso
from .models import AreaCientifica
from .models import LinguagemProgramacao
from .models import Docente
from .models import Disciplina
from .models import Projeto



class DepartamentoAdmin (admin.ModelAdmin):
    list_display = ('nome', )
    search_fields = ('nome', )


class CursoAdmin (admin.ModelAdmin):
    list_display = ('nome', 'apresentacao', 'objectivos', 'competencias', 'departamento', 'condicoesAcesso', 'oportunidadesCarreira', 'imagem')
    search_fields = ('nome', 'apresentacao', 'objectivos', 'competencias', 'departamento', 'condicoesAcesso', 'oportunidadesCarreira', 'imagem')


class AreaCientificaAdmin (admin.ModelAdmin):
    list_display = ('nome', )
    search_fields = ('nome', )

class LinguagemProgramacaoAdmin (admin.ModelAdmin):
    list_display =  ('nome', )
    search_fields = ('nome', )

class DocenteAdmin (admin.ModelAdmin):
    list_display = ('nome', )
    search_display = ('nome', )


class DisciplinaAdmin (admin.ModelAdmin):
    list_display = ('nome', 'areaCientifica', 'ano', 'semestre', 'ects', 'curricularUnitReadableCode' )
    search_display = ('nome', 'areaCientifica', 'ano', 'semestre', 'ects', 'curricularUnitReadableCode')


class ProjetoAdmin (admin.ModelAdmin):
    list_display = ('disciplina', 'descricao', 'conceitosAplicados', 'tecnologiasUtilizadas', 'imagem', 'linkYoutube', 'linkGitHub')
    search_display = ('disciplina', 'descricao', 'conceitosAplicados', 'tecnologiasUtilizadas', 'imagem', 'linkYoutube', 'linkGitHub')



admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(AreaCientifica, AreaCientificaAdmin)
admin.site.register(LinguagemProgramacao, LinguagemProgramacaoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Projeto, ProjetoAdmin)


