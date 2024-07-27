from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from django.db.models.manager import BaseManager
from django.forms import EmailField, ModelForm, CharField, Form

from apps.models import User, Category, Product
from apps.utils import change_phone
from apps.validators import phone_regex


class CustomBaseUserCreationForm(BaseUserCreationForm):
    phone = CharField(max_length=255)

    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ('phone',)


class CustomUserCreationForm(CustomBaseUserCreationForm):
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        phone = change_phone(phone)
        if (
                phone
                and self._meta.model.objects.filter(phone__iexact=phone).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "phone": self.instance.unique_error_message(
                            self._meta.model, ["phone"]
                        )
                    }
                )
            )
        else:
            return phone


class CustomAuthenticationForm(Form):
    phone = CharField(max_length=255, validators=[phone_regex])
    password = CharField()

    def clean(self):
        phone = self.cleaned_data.get("phone")
        password = self.cleaned_data.get("password")

        if phone and password:
            self.user_cache = authenticate(self.request, phone=change_phone(phone), password=password)
            if self.user_cache is None:
                raise ValidationError("Invalid phone number or password")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
