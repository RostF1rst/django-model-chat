from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from . import models
from .models import Profile


# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'page']

    def page(self, obj: Profile) -> str:
        url = reverse('users:user_page', args=[obj.user.id])
        return format_html(f'<a href="{url}">-></a>')


admin.site.register(models.Profile, ProfileAdmin)
