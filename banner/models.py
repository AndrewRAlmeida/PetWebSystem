import random
from django.db import models
from sorl.thumbnail import ImageField


class Banner(models.Model):
    slug = models.SlugField("Nome", unique=True)

    class Meta:
        ordering = ('slug',)
        verbose_name = "banner"
        verbose_name_plural = "banners"

    def __unicode__(self):
        return self.slug

    def __str__(self):
        return self.slug

    def imagem(self):
        """Returns random image using alternatives"""
        imagens = []
        imagens.extend([i.imagem for i in self.imagens.all()])

        return random.choice(imagens) if imagens else ''


class Imagens(models.Model):

    banner = models.ForeignKey(Banner, verbose_name="banner", related_name="imagens", on_delete=models.CASCADE)
    imagem = ImageField("imagem", upload_to='banners')
    link = models.CharField("link", max_length=255, blank=True, null=True)
    mobile = models.BooleanField(default=False)

    class Meta:
        verbose_name = "imagem"
        verbose_name_plural = "imagens"

    def __unicode__(self):
        return unicode(self.imagem)
