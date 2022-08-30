from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.db.models import JSONField


class Pet(models.Model):
    ANIMAL_TYPE_CHOICES = (("Dog", "Dog"), ("Cat", "Cat"), ("Other", "Other"))
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthday = models.DateField(auto_now_add=False, null=True, blank=True)
    animal = models.CharField(max_length=50, null=True, blank=True, choices=ANIMAL_TYPE_CHOICES)
    photo = models.ImageField(upload_to="pets", default="default.jpg", null=True, blank=True)
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    diseases_info = JSONField(encoder="", default=dict, blank=True, null=True)
    allergies_info = JSONField(encoder="", default=dict, blank=True, null=True)
    preferences = JSONField(encoder="", default=dict, null=True, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pet_detail", args=[str(self.id)])

    def clean(self):
        if self.is_main:
            active = Pet.objects.filter(is_main=True, owner=self.owner)
            if self.pk:
                active = active.exclude(pk=self.pk)
            if active.exists():
                raise ValidationError("You already have a main pet.")
