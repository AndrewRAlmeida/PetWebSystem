from django.contrib import admin

from noticias.models import Noticias


@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_cadastro', 'ativo')
    search_fields = ('titulo', 'conteudo')

    readonly_fields = ['image_tag']