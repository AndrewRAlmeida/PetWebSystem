from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def subs_url(context, **kwargs):
    query = context['request'].GET.copy()

    for i, d in kwargs.items():
        query[i] = d

    return query.urlencode()
