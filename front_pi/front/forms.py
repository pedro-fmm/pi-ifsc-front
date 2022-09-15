from django import forms

class LoginForm(forms.Form):
    email           = forms.CharField(label='login-email', max_length=100)
    password        = forms.CharField(label='login-email', max_length=100)