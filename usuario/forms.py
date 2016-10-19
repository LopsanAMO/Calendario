from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        labels = {
            'username': _(''),
            'first_name': _(''),
            'last_name': _(''),
            'email': _(''),
            'password': _(''),
        }
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'placeholder': 'Username'
                }
            ),
            'first_name': forms.TextInput(
                attrs = {
                    'placeholder': 'Nombre'
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'placeholder': 'Apellido'
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    'placeholder': 'Email'
                }
            ),
            'password': forms.TextInput(
                attrs = {
                    'placeholder': 'Contraseña'
                }
            ),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
