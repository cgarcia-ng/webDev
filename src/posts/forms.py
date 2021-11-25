from django import forms
from django.contrib.auth.models import User

from .models import Post


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=10)
    email = forms.EmailField(label='Email')

class CreatePostForm(forms.ModelForm):
    user = forms.CharField(max_length=250, widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['user', 'title', 'description', 'photo']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreatePostForm, self).__init__(*args, **kwargs)
        user = self.request.user
        self.fields['user'].initial = user

    def clean_user(self):
        user = User.objects.get(username=self.request.user.username)
        return user
