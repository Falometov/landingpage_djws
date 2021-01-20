from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider


class CmsAdm(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_image')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_image', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.cms_image:
            return mark_safe(f'<img src="{obj.cms_image.url}" width="200px">')
        else:
            return 'No image found'

    get_image.short_description = 'Image'


# Register your models here.
admin.site.register(CmsSlider, CmsAdm)