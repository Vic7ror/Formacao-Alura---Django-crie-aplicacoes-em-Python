from django.urls import path
from galeria.views import index, imagem


# + Boas praticas +

#Rotas da aplicação galeria
urlpatterns = [
    path('',  index, name='index'), #Rota para a página inicial
    path('imagem/', imagem, name='imagem'), #Rota para a página de imagens 
]