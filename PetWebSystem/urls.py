from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

import noticias.views
import portal.views
from PetWebSystem import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls')),
    path('pets/', portal.views.pets, name='pets'),
    path('pets/<slug:slug>', portal.views.pet, name='pet'),
    path('users/', include('users.urls')),
    path('noticias/', noticias.views.noticias, name='noticias'),
    path('noticias/<int:id>', noticias.views.noticia, name='noticia')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
