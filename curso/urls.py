from django.urls import path
from . import views


app_name = 'cursos'
urlpatterns = [
    path('', views.listCursos_view, name = 'cursos'),
    path('cursos/<str:curso1_name>', views.listCurso_view, name = 'curso'),
    path('disciplina/<str:disciplina1_name>', views.listDisciplina_view, name = 'disciplina'),
    path('disciplina/projeto/<str:disciplina2_name>', views.listDisciplinaProjeto_view, name = 'projeto'),
    path('departamentos', views.listDepartamentos_view, name = 'departamentos'),
    path('departamento/<str:departamento_name>', views.listDepartamento_view, name = 'departamento'),
    path('areasCientificas', views.listAreasCientificas_view , name = 'areasCientificas'),
    path('areaCientifica/<str:areaCientifica_name>', views.listAreaCientifica_view, name = 'areaCientifica'),
    path('docentes', views.listDocentes_view, name = 'docentes'),
    path('docente/<str:docente_name>', views.listDocente_view, name = 'docente'),
    path('editaCurso/<str:curso_name>' , views.edita_curso_view, name = 'edita_curso'),
    path('novoCurso', views.novo_curso_view, name = 'novo_curso'),
    path('apagarCurso/<str:curso_name>' , views.apaga_curso_view, name = 'apaga_curso'),
    path('editaDisciplina/<str:disciplina_name>', views.edita_disciplina_view, name = 'edita_disciplina'),
    path('novaDisciplina', views.nova_disciplina_view, name = 'nova_disciplina'),
    path('apagarDisciplina/<str:disciplina_name>', views.apaga_disciplina_view, name = 'apaga_disciplina'),
    path('editaDepartamento/<str:departamento_name>' , views.edita_departamento_view, name = 'edita_departamento'),
    path('novoDepartamento', views.novo_Departamento_view, name = 'novo_departamento'),
    path('apagarDepartamento/<str:departamento_name>', views.apaga_departamento_view, name = 'apaga_departamento'),
    path('editaAreaCientifica/<str:area_cientifica_name>', views.edita_AreaCientifica_view, name = 'edita_areaCientifica'),
    path('novaAreaCientifica', views.nova_AreaCientifica_view, name = 'nova_areaCientifica'),
    path('apagarAreaCientifica/<str:area_cientifica_name>', views.apaga_AreaCientifica_view, name ='apaga_areaCientifica'),
    path('editaDocente/<str:docente_name>', views.edita_Docente_view,  name = 'edita_docente'),
    path('novoDocente', views.novo_Docente_view, name = 'novo_docente'),
    path('apagarDocente/<str:docente_name>', views.apaga_Docente_view, name = 'apaga_docente'),
    path('editaProjeto/<str:disciplina_name>', views.edita_Projeto_view, name = 'edita_projeto'),
    path('novoProjeto', views.novo_Projeto_view, name = 'novo_projeto'),
    path('apagaProjeto/<str:disciplina_name>', views.apaga_Projeto_view, name = 'apaga_projeto'),
    ]