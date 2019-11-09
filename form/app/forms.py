#coding: utf-8

from django import forms


class Auth(forms.Form):
    username = forms.CharField(
        max_length=18,
        min_length=3,
        required=True,
        label="username",
        widget=forms.TextInput(attrs={'placeholder' : '最大不可超过18字符'}))

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="password")
