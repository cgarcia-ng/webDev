from django import forms
from django.db.models import fields
from django.forms import ModelForm

from .models import Post

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=10)
    email = forms.EmailField(label='Email')

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['user', 'title', 'description', 'photo']