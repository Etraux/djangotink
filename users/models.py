from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, unique=True, null=True)
    zipcode = models.CharField(max_length=6, blank=True)
    address = models.CharField(max_length=100, blank=True)
    address_detail = models.CharField(max_length=200, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name', 'phone']

    objects = CustomUserManager()

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email
