from django.urls import path
from .views import inicio_gerencia, listagem_noticia,cadastrar_noticia,editar_noticia, list_categorias, cadastrar_categoria, editar_categoria, excluir_categoria, editar_categoria, login_view, logout_view, register

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    path('categorias/', list_categorias, name='listagem_categorias'),
    path('categorias/cadastro', cadastrar_categoria, name='cadastro_categoria'),
    path('categorias/editar/<int:id>', editar_categoria, name='editar_categoria'),
    path('categorias/excluir/<int:id>', excluir_categoria, name='excluir_categoria'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='cadastrar_usuario'),
    # Add your URL patterns here
]