from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe


class Noticias(models.Model):
    class Meta:
        ordering = ['data_cadastro']
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    ativo = models.BooleanField(default=True)
    titulo = models.CharField(verbose_name="título", blank=False, null=False, max_length=60)
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='data de cadastro')
    conteudo = RichTextField(null=True, blank=True, verbose_name='conteúdo')
    imagem = models.ImageField(upload_to='noticias', blank=False, null=False)

    def image_tag(self):
        return mark_safe('<a href="{url}" target="blank"><img src="{url}" height="150" /></a>'.format(url=self.imagem.url))

    image_tag.short_description = ''
