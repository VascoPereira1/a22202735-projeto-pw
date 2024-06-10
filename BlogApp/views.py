from django.shortcuts import render, redirect, get_object_or_404
from .forms import  ComentarioForm, ArtigoForm, infoAdicionalUserForm
from .models import  artigos, comentarioRating, infoAdicionalUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required
def novo_comentario_view(request, artigo_name):
    artigo1 = artigos.objects.get(titulo = artigo_name)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, autor = request.user, artigo = artigo1)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo', artigo1)
    else:
        form = ComentarioForm(autor = request.user, artigo = artigo1)
    return render(request, 'novoComentario.html', {'form': form})


def novo_InformacaoUser_view(request):
    if request.method == 'POST':
        form = infoAdicionalUserForm(request.POST,request.FILES,  user = request.user)  # Passa o usuário autenticado como autor
        if form.is_valid():
            form.save()
            return redirect('artigos:artigos')  # Redireciona para a página inicial após criar o artigo
    else:
        form = infoAdicionalUserForm(user=request.user)  # Passa o usuário autenticado como autor
    return render(request, 'novoInformacaoUser.html',  {'form': form})




@login_required
def novo_artigo_view(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST,request.FILES,  autor=request.user)  # Passa o usuário autenticado como autor
        if form.is_valid():
            form.save()
            return redirect('artigos:artigos')  # Redireciona para a página inicial após criar o artigo
    else:
        form = ArtigoForm(autor=request.user)  # Passa o usuário autenticado como autor
    return render(request, 'novoArtigo.html',  {'form': form})


def edita_usuario_view(request):
    info_adicional = infoAdicionalUser.objects.get(user = request.user)
    if request.POST:
        form = infoAdicionalUserForm(request.POST or None, request.FILES, instance=info_adicional,  user=request.user)
        if form.is_valid():
            form.save()
            return redirect('artigos:usuario', request.user.pk)
    else:
        form = infoAdicionalUserForm(instance=info_adicional,  user=request.user)

    context = {'form': form}
    return render(request, 'editaAutor.html', context)





@login_required
def edita_artigo_view(request, artigo_name):
    artigo = artigos.objects.get(titulo = artigo_name)

    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=artigo, autor=request.user)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo', artigo )
    else:
        form = ArtigoForm(instance=artigo, autor=request.user)

    context = {'form': form, 'artigo':artigo}
    return render(request, 'editaArtigo.html', context)

@login_required
def apaga_artigo_view(request, artigo_name):
     artigo = artigos.objects.get(titulo = artigo_name)
     artigo.delete()
     return redirect('artigos:artigos')



@login_required
def edita_comentario_view(request, artigo_name, id):
    comentario = comentarioRating.objects.get(id = id)
    artigo1 = artigos.objects.get(titulo = artigo_name)

    if request.POST:
        form = ComentarioForm(request.POST or None, request.FILES, instance=comentario, artigo=artigo1, autor = request.user)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo', artigo1)
    else:
        form = ComentarioForm(instance=comentario)

    context = {'form': form, 'comentario':comentario}
    return render(request, 'editaComentario.html', context)

@login_required
def apaga_comentario_view(request, artigo_name, id):
    comentario = comentarioRating.objects.get(id = id)
    artigo = artigos.objects.get(titulo = artigo_name)

    comentario.delete()
    return redirect('artigos:artigo', artigo)



def listArtigo_view(request, artigo_name):
    context = {
        'artigo' : artigos.objects.get(titulo = artigo_name),
        'comentarios' : comentarioRating.objects.filter(artigo__titulo = artigo_name),
    }
    return render(request, 'listArtigo.html', context)

def listArtigos_view(request):
    usuario_autenticado = request.user
    context = {
        'artigos' : artigos.objects.all(),
        'autor' : usuario_autenticado,
    }
    return render(request, 'listArtigos.html', context)

def listMeusArtigos_view(request):
    usuario_autenticado = request.user
    context = {
        'artigos' : artigos.objects.all(),
        'autor' : usuario_autenticado,
    }
    return render(request, 'listMeusArtigos.html', context)


def listUsuarios_view(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, 'listUsuarios.html',context)

def listUsuario_view(request, usuario_id):
    user = get_object_or_404(User, pk=usuario_id)
    context = {
        'user': user
    }
    return render(request, 'listUsuario.html', context)








