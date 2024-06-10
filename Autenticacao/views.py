from django.shortcuts import render, redirect
from django.contrib.auth import models
from django.contrib.auth import authenticate, login, logout



def registo_view(request, homePage_name):
    homePage = homePage_name
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect(f'https://a22202735.pythonanywhere.com/Autenticacao/login/{homePage}')

    return render(request, 'registo.html', {'homePage': homePage, })



def logout_view(request, homePage_name):
    homePage = homePage_name
    logout(request)
    if homePage == 'Bandas':
        return redirect('https://a22202735.pythonanywhere.com/AppBandas/')
    if homePage == 'Artigos':
        return redirect('https://a22202735.pythonanywhere.com/BlogApp/')
    if homePage == 'Cursos':
        return redirect('https://a22202735.pythonanywhere.com/AppCurso/')
    return redirect(f'https://a22202735.pythonanywhere.com/{homePage}')



def login_view(request, homePage_name):

    homePage = homePage_name

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            if homePage == 'Bandas':
                return redirect('https://a22202735.pythonanywhere.com/AppBandas/')
            if homePage == 'Artigos':
                return redirect('https://a22202735.pythonanywhere.com/BlogApp/')
            if homePage == 'Cursos':
                return redirect('https://a22202735.pythonanywhere.com/AppCurso/')
            return redirect(f'https://a22202735.pythonanywhere.com/{homePage}')


        else:
            render(request, 'login.html', {
                'mensagem':'Credenciais inválidas', 'homePage': homePage,
            })

    return render(request, 'login.html', {'homePage': homePage, })

