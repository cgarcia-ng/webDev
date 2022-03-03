from django import forms

class ProfileUpdateForm(forms.Form):
    # birthday = forms.DateField(required=True)
    biography = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=15)
    avatar = forms.ImageField(required=False)
    website = forms.URLField(max_length=200)
