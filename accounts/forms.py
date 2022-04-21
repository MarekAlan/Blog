from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginFormView(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Login'}),
                               label='')  # po to żeby nie było labelki na widoku [Login:]
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
                               label='')


class CreateUserForm(forms.ModelForm):
    pass1 = forms.CharField(widget=forms.PasswordInput())
    pass2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        data = super().clean()
        if data['pass1'] != data['pass2']:
            raise ValidationError("Hasła się nie zgadzają")

    class Meta:
        model = User
        fields = ['username']


class UserPermUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_permissions']
        widgets = {
            'user_permissions': forms.CheckboxSelectMultiple
        }
