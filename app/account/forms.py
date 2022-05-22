from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": 'Username',
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": 'Password',
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": 'Username',
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": 'Password',
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": 'Password check',
                "class": "form-control"
            }
        ))
    terms = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={}
        ))

    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2')


class UpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    update = forms.CharField(required=False)
    delete = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'birthday', 'biography',
                  'contacts', 'update', 'delete',)
        widgets = {
            'birthday': forms.DateInput(attrs={
                'type': 'date',
            })
        }
