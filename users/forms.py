from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'name', 'phone', 'zipcode',
                  'address', 'address_detail',)


class CustomUserChangeForm(forms.ModelForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'phone', 'zipcode',
                  'address', 'address_detail')
        widgets = {
            'email': forms.TextInput(attrs={'disabled': True}),
            'phone': forms.TextInput(attrs={'disabled': True}),
        }
