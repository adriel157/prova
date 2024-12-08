from django.contrib import admin
from .models import Noticia,Categoria, UserBlog
from django.contrib.auth.admin import UserAdmin


class UserBlogAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cpf', 'nome_cidade', 'nome_mae', 'endereco', 'nome_bairro')}),
    )

admin.site.register(UserBlog, UserBlogAdmin)


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao',)
    search_fields = ('titulo', )
    date_hierarchy = 'data_publicacao'
    ordering = ('-data_publicacao',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
