# Arquivo responsável por controlar as views (o que o usuário vê na tela)
from django.shortcuts import render

#httpResponse é uma classe que representa uma resposta HTTP
from django.http import HttpResponse

#recebe a requisição e devolve uma resposta
def index(request):
    return render(request, 'galeria/index.html') #renderiza o template index.html e o retorna como resposta para o usuário.

def imagem(request):
    return render(request, 'galeria/imagem.html') #renderiza o template imagens.html e o retorna como resposta para o usuário.