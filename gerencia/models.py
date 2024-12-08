from django.db import models
from usuarios.models import UserBlog
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserBlog(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    nome_cidade = models.CharField(max_length=100, blank=True, null=True)
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    nome_bairro = models.CharField(max_length=100, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='gerencia_user_set',  # Adicione related_name aqui
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='gerencia_user_permissions',  # Adicione related_name aqui
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
        related_query_name='user',
    )

    def __str__(self):
        return f"{self.username} - {self.cpf}"


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    data_publicacao = models.DateField(auto_created=True)
    texto = models.TextField()
    image = models.ImageField(upload_to='noticias/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey( UserBlog, on_delete=models.CASCADE, blank=True,null=True)  
    

    