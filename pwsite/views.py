from django.shortcuts import render

def index_view(request):
    return render(request, "index.html")

def sobre_view(request):
    return render(request, "sobre.html")

def interesses_view(request):
    return render(request, "interesses.html")
