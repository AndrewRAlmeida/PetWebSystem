from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from noticias.models import Noticias

def noticias(request):
    noticias = Noticias.objects.filter(ativo=True).all()

    paginator = Paginator(noticias, 8)

    page = request.GET.get('page')
    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        noticias = paginator.page(1)
    except EmptyPage:
        noticias = paginator.page(paginator.num_pages)

    return render(request, 'noticias.html', locals())

def noticia(request, id):
    noticia = Noticias.objects.get(ativo=True, id=id)
    return render(request, 'noticia.html', locals())