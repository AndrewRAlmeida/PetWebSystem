from django.contrib import admin
from .models import Pet, Categoria, Imagem, Adocoes


class ImagemInline(admin.TabularInline):
    model = Imagem

    fields = ['image_tag', 'pet', 'imagem', 'perfil']
    readonly_fields = ['image_tag']

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'categoria', 'castrado', 'vacinado', 'data_cadastro')
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}

    inlines = [ImagemInline]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Adocoes)
class Adocoesdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pet', 'data_cadastro')
    search_fields = ('usuario', 'pet')