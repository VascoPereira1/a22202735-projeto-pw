from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def function_benfica(request):
    return HttpResponse("Benfica em 1º lugar")

def function_sporting(request):
    return HttpResponse("Sporting em 1º lugar")

def function_porto(request):
    return HttpResponse("Porto em 1º lugar")


