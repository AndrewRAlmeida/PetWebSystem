from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from pets.filters import PetsFilter
from pets.models import Pet, Adocoes


def inicio(request):
    pets_destaques = Pet.objects.filter(ativo=True)[:4]
    return render(request, 'index.html', locals())

def ong(request):
    return render(request, 'ong.html', locals())
def contato(request):
    return render(request, 'contato.html', locals())
def pets(request):
    pets = Pet.objects.filter(ativo=True)
    f = PetsFilter(request.GET, queryset=pets)
    paginator = Paginator(f.qs, 8)

    page = request.GET.get('page')
    try:
        pets = paginator.page(page)
    except PageNotAnInteger:
        pets = paginator.page(1)
    except EmptyPage:
        pets = paginator.page(paginator.num_pages)

    return render(request, 'pets.html', locals())

def pet(request, slug):
    pet = Pet.objects.get(slug=slug)

    solicitacao = False
    if request.user.is_authenticated:
        if Adocoes.objects.filter(usuario=request.user, pet=pet).first():
            solicitacao = True


    if request.POST:
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            adocao = Adocoes.objects.create(usuario=request.user, pet=pet)
            try:
                adocao.save()
                messages.success(request, 'Solicitação de adoção enviada, em breve retornaremos o contato!')
                return redirect('/pets/'+pet.slug)
            except Exception as e:
                messages.error(request, 'Erro, tente novamente!')
                return redirect('/pets/' + pet.slug)

    return render(request, 'pet.html', locals())