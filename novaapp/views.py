from django.shortcuts import render

def pikachu_view(request):
    return render(request, "pikachu.html")

def charmander_view(request):
    return render(request, "charmander.html")

def menu_view(request):
    return render(request, "menuNavegacao.html")

