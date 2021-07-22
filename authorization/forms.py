from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import ReCaptchaField,ReCaptchaV3


class RegisterForm(forms.Form):
    captcha = ReCaptchaField(
        label='Security System',
        widget=ReCaptchaV3(),
        error_messages={
            'required': 'Please Enter Security Code'
        }
    )
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter a valid username'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'enter an email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'enter a password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        is_exist = User.objects.filter(username__iexact=username).exists()
        if is_exist:
            raise ValidationError('this username has taken')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        is_exist = User.objects.filter(email__iexact=email).exists()
        if is_exist:
            raise ValidationError('this email has taken')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('password should be more than 8 characters')
        return password


class LoginForm(forms.Form):
    captcha = ReCaptchaField(
        label='Security System',
        widget=ReCaptchaV3(),
        error_messages={
            'required': 'Please Enter Security Code'
        }
    )
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter a valid username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'enter a password'}))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('password should be more than 8 characters')
        return password


class VerifyForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'enter a valid username', 'style': 'width:20vw'}), required=True)
