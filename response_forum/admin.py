from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from . import models


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'publication_date', 'page')
    list_filter = ['publication_date']
    search_fields = ['prompt']

    def page(self, obj: models.Response) -> str:
        url = reverse('response-forum:details', args=[obj.id])
        return format_html(f'<a href="{url}">-></a>')



admin.site.register(models.Response, ResponseAdmin)
