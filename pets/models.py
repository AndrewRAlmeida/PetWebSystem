from django.db import models
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe

from users.models import Usuario
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField

class Categoria(models.Model):
    ativo = models.BooleanField(default=True)
    nome = models.CharField(null=False, blank=False, unique=True, max_length=60)

    def __str__(self):
        return str(self.nome)

# Create your models here.
class Pet(models.Model):
    class Meta:
        ordering = ('-data_cadastro', )

    ativo = models.BooleanField(default=True)
    nome = models.CharField(null=False, blank=False, max_length=60)
    slug = models.SlugField(max_length=60, unique=True)
    idade = models.PositiveIntegerField(null=True, blank=True, help_text='em anos')
    vacinado = models.BooleanField(default=False)
    castrado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    raca = models.CharField(null=True, blank=True, max_length=60, verbose_name='Raça', help_text='use SRD caso não saiba ou não exista uma raça definida')
    cor = models.CharField(null=True, blank=True, max_length=20)

    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = RichTextField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='data de cadastro')

    @property
    def imagens(self):
        return Imagem.objects.filter(pet=self)

    @property
    def imagem(self):
        imagem = Imagem.objects.filter(pet=self, perfil=True).first()
        if not imagem:
            imagem = Imagem.objects.filter(pet=self)[0]
        if not imagem:
            imagem = ''
        return imagem

    def __str__(self):
        return str(self.nome)

    def save(self, rebuild=True, *args, **kwargs):
        if len(self.slug) == 0:
            self.slug = slugify(self.nome)
        else:
            self.slug = slugify(self.slug)

        super(Pet, self).save(*args, **kwargs)

class Imagem(models.Model):
    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    imagem = ImageField(upload_to='pets', blank=True)
    perfil = models.BooleanField(verbose_name='Foto principal')

    def image_tag(self):
        return mark_safe('<a href="{url}" target="blank"><img src="{url}" height="150" /></a>'.format(url=self.imagem.url))

    image_tag.short_description = ''

    def __str__(self):
        return self.pet.nome or ''

    def save(self):
        if self.perfil:
            try:
                temp = Imagem.objects.get(perfil=True, pet=self.pet)
                if self != temp:
                    temp.perfil = False
                    temp.save()
            except Imagem.DoesNotExist:
                pass
        super(Imagem, self).save()

class Adocoes(models.Model):
    class Meta:
        ordering = ('-data_cadastro', )
        verbose_name = 'Adoçao'
        verbose_name_plural = 'Adoções'

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.nome