from .models import Pet
import django_filters

class PetsFilter(django_filters.FilterSet):
    class Meta:
        model = Pet
        fields = ['castrado', 'vacinado', 'categoria']