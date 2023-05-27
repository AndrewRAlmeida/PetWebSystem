# -*- coding: utf-8 -*-

from django.conf import settings
from django import template
from banner.models import Banner
from sorl.thumbnail import get_thumbnail

register = template.Library()

@register.inclusion_tag('includes/banner.html')
def get_banner(slug, size='200x200', **kwargs):
    banner = Banner.objects.get_or_create(slug=slug)[0]
    ims = []
    ims_m = []
    for img in banner.imagens.all():
        if img.mobile:
            ims_m.append({'img': get_thumbnail(img.imagem, size, **kwargs), 'link': img.link})
        else:
            ims.append({'img': get_thumbnail(img.imagem, size, **kwargs), 'link': img.link})
    return {'banner': banner, 'ims': ims, 'ims_m': ims_m}
