from django.contrib import admin
from .models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'birthday', 'animal', 'is_main')
    list_display_links = ('name', 'owner', 'birthday', 'animal')


admin.site.register(Pet, PetAdmin)
