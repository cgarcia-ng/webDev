from django import forms

class ProfileUpdateForm(forms.Form):
    # birthday = forms.DateField(required=True)
    biography = forms.Textarea()
    phone_number = forms.CharField(max_length=15)
    avatar = forms.ImageField()
    website = forms.URLField(max_length=200)
