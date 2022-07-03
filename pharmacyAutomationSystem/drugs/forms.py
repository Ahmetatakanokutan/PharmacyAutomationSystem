from unittest.util import _MAX_LENGTH
import django


from django import forms

class loginForm(forms.Form):
    username = forms.CharField(max_length=100, label='username')
    password = forms.CharField(max_length=100, label='password', widget=forms.PasswordInput)