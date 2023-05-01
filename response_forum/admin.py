from django.contrib import admin

from . import models


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'publication_date')
    list_filter = ['publication_date']
    search_fields = ['prompt']


admin.site.register(models.Response, ResponseAdmin)
