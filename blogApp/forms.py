from django.forms import CheckboxInput
from django import forms

from blogApp.models import Blog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs') and not isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['view_count', 'at_published', 'owner', 'slug']

