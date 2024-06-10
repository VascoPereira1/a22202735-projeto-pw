from django.shortcuts import render, redirect
from .models import Departamento, Curso, AreaCientifica, LinguagemProgramacao, Docente, Disciplina, Projeto
from .forms import CursoForm, DisciplinaForm, DepartamentoForm, AreaCientificaForm, LinguagemProgramacaoForm, DocenteForm, ProjetoForm


def novo_curso_view(request):
    form = CursoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursos:cursos')
    context = {'form': form}

    return render(request, 'novoCurso.html', context)


def edita_curso_view(request, curso_name):
    curso = Curso.objects.get(nome = curso_name)

    if request.POST:
        form = CursoForm(request.POST or None, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:curso',  curso)
    else:
        form = CursoForm(instance=curso)  # cria formulário com dados da instância autor

    context = {'form': form, 'curso' : curso}
    return render(request, 'editaCurso.html', context)


def apaga_curso_view(request, curso_name):
    curso = Curso.objects.get(nome = curso_name)
    curso.delete()
    return redirect('cursos:cursos')


def nova_disciplina_view(request):

    form = DisciplinaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursos:cursos')
    context = {'form': form}

    return render(request, 'novaDisciplina.html', context)

def edita_disciplina_view(request, disciplina_name):

    disciplina = Disciplina.objects.get(nome = disciplina_name)

    if request.POST:
        form = DisciplinaForm(request.POST or None, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('cursos:disciplina',  disciplina)
    else:
        form = DisciplinaForm(instance=disciplina)  # cria formulário com dados da instância autor

    context = {'form': form, 'disciplina' : disciplina}
    return render(request, 'editaDisciplina.html', context)

def apaga_disciplina_view(request, disciplina_name):
    disciplina = Disciplina.objects.get(nome = disciplina_name)
    disciplina.delete()
    return redirect('cursos:cursos')



def novo_Departamento_view(request):
    form = DepartamentoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursos:departamentos')
    context = {'form': form}

    return render(request, 'novoDepartamento.html', context)

def edita_departamento_view(request, departamento_name):
    departamento = Departamento.objects.get(nome = departamento_name)

    if request.POST :
        form = DepartamentoForm(request.POST or None, request.FILES, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('cursos:departamento', departamento)
    else:
        form = DepartamentoForm(instance=departamento)  # cria formulário com dados da instância autor

    context = {'form': form, 'departamento' : departamento}
    return render(request, 'editaDepartamento.html', context)

def apaga_departamento_view(request, departamento_name):
    departamento = Departamento.objects.get(nome = departamento_name)
    departamento.delete()
    return redirect('cursos:departamentos')

def nova_AreaCientifica_view(request):
    form = AreaCientificaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursos:areasCientificas')
    context = {'form': form}

    return render(request, 'novaAreaCientifica.html', context)



def edita_AreaCientifica_view(request, area_cientifica_name):
    areaCientifica = AreaCientifica.objects.get(nome = area_cientifica_name)

    if request.POST :
        form = AreaCientificaForm(request.POST or None, request.FILES, instance=areaCientifica)
        if form.is_valid():
            form.save()
            return redirect('cursos:areaCientifica', areaCientifica)
    else:
        form = AreaCientificaForm(instance=areaCientifica)  # cria formulário com dados da instância autor

    context = {'form': form, 'areaCientifica' : areaCientifica}
    return render(request, 'editaAreaCientifica.html', context)

def apaga_AreaCientifica_view(request, area_cientifica_name):
    areaCientifica = AreaCientifica.objects.get(nome = area_cientifica_name)
    areaCientifica.delete()
    return redirect('cursos:areasCientificas')

def novo_Docente_view(request):
    form = DocenteForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursos:docentes')
    context = {'form': form}

    return render(request, 'novoDocente.html', context)

def edita_Docente_view(request, docente_name):
    docente = Docente.objects.get(nome = docente_name)

    if request.POST :
        form = DocenteForm(request.POST or None, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('cursos:docente', docente)
    else:
        form = DocenteForm(instance=docente)  # cria formulário com dados da instância autor

    context = {'form': form, 'docente' : docente}
    return render(request, 'editaDocente.html', context)

def apaga_Docente_view(request, docente_name):
    docente = Docente.objects.get(nome = docente_name)
    docente.delete()
    return redirect('cursos:docentes')

def novo_Projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('cursos:cursos')
    context = {'form': form}

    return render(request, 'novoProjeto.html', context)

def edita_Projeto_view(request, disciplina_name):
    disciplina = Disciplina.objects.get(nome = disciplina_name)
    projeto = Projeto.objects.get(disciplina__nome = disciplina_name)

    if request.POST :
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('cursos:projeto', disciplina)
    else:
        form = ProjetoForm(instance=projeto)  # cria formulário com dados da instância autor

    context = {'form': form, 'disciplina' : disciplina}
    return render(request, 'editaProjeto.html', context)


def apaga_Projeto_view(request, disciplina_name):
    projeto = Projeto.objects.get(disciplina__nome = disciplina_name)
    projeto.delete()
    return redirect('cursos:disciplina', disciplina_name)




def listCurso_view(request, curso1_name):
    context = {
        'curso' : Curso.objects.get(nome = curso1_name)

    }
    return render(request, 'listCurso.html', context)


def listDepartamentos_view(request):
    context = {
        'departamentos' : Departamento.objects.all()
    }
    return render(request, 'listDepartamentos.html', context)

def listAreasCientificas_view(request):
    context = {
        'areasCientificas' : AreaCientifica.objects.all()
    }
    return render(request, 'listAreasCientificas.html', context)

def listDocentes_view(request):
    context = {
        'docentes' : Docente.objects.all()
    }
    return render(request, 'listDocentes.html', context)

def listDocente_view(request, docente_name):
    context = {
        'docente' : Docente.objects.get(nome = docente_name)
    }
    return render(request, 'listDocente.html', context)

def listAreaCientifica_view(request,areaCientifica_name):
    context = {
        'areaCientifica' : AreaCientifica.objects.get(nome = areaCientifica_name)
    }
    return render(request, 'listAreaCientifica.html', context)


def listDepartamento_view(request, departamento_name):
    context = {
        'departamento' : Departamento.objects.get(nome = departamento_name)
    }
    return render(request, 'listDepartamento.html', context)

def listDisciplina_view(request, disciplina1_name):
    context = {
        'disciplina' : Disciplina.objects.get(nome = disciplina1_name),
        'projeto' : Projeto.objects.filter(disciplina__nome = disciplina1_name),
    }
    return render(request, 'listDisciplina.html', context)

def listDisciplinaProjeto_view(request, disciplina2_name):
    context = {
        'projeto' : Projeto.objects.get(disciplina__nome = disciplina2_name),
    }
    return render(request, 'listDisciplinaProjeto.html', context)

def listCursos_view(request):
    context = {
        'cursos' : Curso.objects.all()
    }

    return render(request, 'listCursos.html', context)