from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from pets.models import Pet


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "profile.html"
    login_url = 'login'

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(
            *args, **kwargs)
        context['pets'] = Pet.objects.filter(owner=self.request.user)

        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "profile_edit.html"
    success_url = reverse_lazy('home')
    login_url = 'login'

    def get_object(self):
        return self.request.user
