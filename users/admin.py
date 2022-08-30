from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'name', 'phone')
    list_display_links = ('email', 'name', 'phone')
    list_filter = ('email', 'is_staff', 'is_active', 'name')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name',
                           'phone', 'zipcode', 'address', 'address_detail', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'name', 'phone', 'zipcode', 'address', 'address_detail')}
         ),
    )
    search_fields = ('email', 'name', 'phone')
    ordering = ('email', 'name')


admin.site.register(CustomUser, CustomUserAdmin)
