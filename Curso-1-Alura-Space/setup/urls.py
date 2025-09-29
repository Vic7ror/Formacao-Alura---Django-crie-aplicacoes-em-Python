from django.contrib import admin
from django.urls import path, include

# Define as rotas do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
