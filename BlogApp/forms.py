from django import forms
from .models import  artigos, comentarioRating, infoAdicionalUser


class infoAdicionalUserForm(forms.ModelForm):
    class Meta:
        model = infoAdicionalUser
        fields = ['imagem', 'biografia', 'dataNascimento', 'interesses', 'profissao']

        widgets = {
        'dataNascimento' : forms.DateInput(attrs = {'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Recebe o autor como argumento
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user  # Define o autor do artigo
        if commit:
            instance.save()
        return instance




class ArtigoForm(forms.ModelForm):
    class Meta:
        model = artigos
        fields = ['titulo', 'corpoDoArtigo', 'imagem', 'horaPublicacao', 'categoria', 'introducao']

        widgets = {
        'horaPublicacao' : forms.DateInput(attrs = {'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        self.autor = kwargs.pop('autor', None)  # Recebe o autor como argumento
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.autor = self.autor  # Define o autor do artigo
        if commit:
            instance.save()
        return instance


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = comentarioRating
        fields = ['comentario', 'rating', 'horaComentario']

        widgets = {
        'horaComentario' : forms.DateInput(attrs = {'type':'date'})
        }

    def __init__(self, *args, **kwargs):
        self.autor = kwargs.pop('autor', None)
        self.artigo = kwargs.pop('artigo', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.autor = self.autor
        instance.artigo = self.artigo
        if commit:
            instance.save()
        return instance




