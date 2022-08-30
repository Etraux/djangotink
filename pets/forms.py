from django import forms

from .models import Pet


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            "name",
            "birthday",
            "photo",
            "animal",
            "registration_number",
            "diseases_info",
            "allergies_info",
            "preferences",
            "is_main",
        )
        widgets = {
            "birthday": forms.SelectDateWidget(years=range(1970, 2020)),
            "is_main": forms.CheckboxInput(attrs={"class": "checkbox"}),
        }


class PetChangeForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = (
            "name",
            "birthday",
            "photo",
            "animal",
            "registration_number",
            "diseases_info",
            "allergies_info",
            "preferences",
            "is_main",
        )
        widgets = {
            "birthday": forms.SelectDateWidget(years=range(1970, 2020)),
            "is_main": forms.CheckboxInput(attrs={"class": "checkbox"}),
        }
