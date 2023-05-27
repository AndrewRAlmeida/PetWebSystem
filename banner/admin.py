from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Banner, Imagens

class ImagensInline(AdminImageMixin, admin.TabularInline):
    model = Imagens
    extra = 0

class BannerAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('slug',)
    search_fields = ('slug',)
    inlines = (ImagensInline,)

admin.site.register(Banner, BannerAdmin)
