from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.forms import CheckboxInput

from mailingApp.models import Mailing, Client, Massage
from usersApp.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs') and not isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class ManagerMailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['status']


class SuperuserMailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class UserMailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ['owner', 'status']


class SuperuserClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class UserClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'description']


class SuperuserMassageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Massage
        fields = '__all__'


class UserMassageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Massage
        fields = ['title', 'text']
