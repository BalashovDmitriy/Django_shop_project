from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm

from catalog.forms import MixinForm
from users.models import User
from django import forms


class UserCreationForm(MixinForm, BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserUpdateForm(MixinForm, BaseUserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'telegram', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
