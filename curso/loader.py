from curso.models import *
import json


Departamento.objects.all().delete()
Curso.objects.all().delete()
AreaCientifica.objects.all().delete()
LinguagemProgramacao.objects.all().delete()
Docente.objects.all().delete()
Disciplina.objects.all().delete()
Projeto.objects.all().delete()


with open("curso/json/dadosLEI.json") as f :
    data = json.load(f)

    course_flat_plan = data["courseFlatPlan"]
    course_detail = data["courseDetail"]

    AreaCientifica.objects.create(nome = "Informática")

    for disciplina in course_flat_plan:
        Disciplina.objects.create(
        nome = disciplina["curricularUnitName"],
        areaCientifica =  AreaCientifica.objects.get(nome = "Informática"),
        ano = disciplina["curricularYear"],
        semestre = disciplina["semester"],
        ects = disciplina["ects"],
        curricularUnitReadableCode = ["curricularIUnitReadableCode"]
        )


    Departamento.objects.create(nome = course_detail["departement"])



    Curso.objects.create(
    nome = course_detail["courseName"],
    apresentacao = course_detail["presentation"],
    competencias = course_detail["competences"],
    departamento = Departamento.objects.get(nome = course_detail["departement"]),
    condicoesAcesso = course_detail["accessContidions"],
    oportunidadesCarreira = course_detail["careerOportunities"]
    )






