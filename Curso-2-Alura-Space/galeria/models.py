from django.db import models

# Create your models here.

#django ORM (Object-Relational Mapping)
#Permite mapear classes Python para tabelas em um banco de dados relacional.
#Cada classe representa uma tabela, e cada atributo da classe representa uma coluna na tabela.

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null= False, blank= False) #Campo de texto com tamanho máximo de 100 caracteres, não pode ser nulo ou vazio.
    legenda = models.CharField(max_length=150, null= False, blank= False) #Campo de texto com tamanho máximo de 150 caracteres, não pode ser nulo ou vazio.
    descricao = models.TextField(null= False, blank= False) #Campo de texto longo, não pode ser nulo ou vazio.
    foto = models.CharField(max_length=100, null= False, blank= False) #Campo de texto com tamanho máximo de 100 caracteres, não pode ser nulo ou vazio.
    
    #Boas práticas: definir o método __str__ para facilitar a identificação dos objetos no admin do Django.
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
        #Retorna uma representação em string do objeto Fotografia, mostrando o nome da fotografia.