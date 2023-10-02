from django import forms

from blog.models import Blog
from catalog.forms import MixinForm


class BlogForm(MixinForm, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'text', 'image', 'to_publish')
