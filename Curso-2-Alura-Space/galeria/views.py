# Arquivo responsável por controlar as views (o que o usuário vê na tela)
from django.shortcuts import render

#httpResponse é uma classe que representa uma resposta HTTP
from django.http import HttpResponse

#Dicionário que armazena informações sobre as imagens
dados = {
    1: {"nome": "Nebulosa de Carina",
        "legenda": "webbtelescope.org/ NASA / James Webb"},
    2: {"nome": "Galáxia NGC 1079",
        "legenda": "nasa.org/ NASA / Hubble"},
}

#recebe a requisição e devolve uma resposta
def index(request):
    #render permite enviar um dicionário com dados para o template
    return render(request, 'galeria/index.html', {"cards": dados}) #renderiza o template index.html e o retorna como resposta para o usuário.

def imagem(request):
    return render(request, 'galeria/imagem.html') #renderiza o template imagens.html e o retorna como resposta para o usuário.