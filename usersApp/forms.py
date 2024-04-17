from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import CheckboxInput

from usersApp.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs') and not isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', ]


class UserUpdateForm(StyleFormMixin, UserChangeForm):
    password = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'email', 'password', ]



class SuperuserUpdateForm(StyleFormMixin, UserChangeForm):
    password = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = '__all__'
