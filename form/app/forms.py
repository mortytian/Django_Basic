#coding: utf-8

from django import forms

from .models import Auth as AuthModel


class AuthModelForm(forms.ModelForm):
    class Meta:
        model = AuthModel
        fields = ['username', 'password'] # '__all__'
        exclude = []    # 不转成表单字段的model字段
        field_classes = {
            'username' : forms.CharField,
            'password' : forms.CharField
        }

        labels = {
            'username' : '用户名',
            'password' : '密码'
        }

        widgets = {
            'username' : forms.TextInput(
                attrs={'placeholder':'请输入用户名'}
            ),
            'password' : forms.PasswordInput(
                attrs={'placeholder':'请输入密码'},
                render_value=True
            )

        }

        error_messages={
            'uesrname' : {'required' : '用户名不可以为空'},
            'password' : {'min_length' : '最少不低于10个字符'}
        }

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if len(username) > 18:
            raise forms.ValidationError('用户名最大不能超过18')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password','')
        if len(password) > 18:
            raise forms.ValidationError('用户名最大不能超过18')
        return password



class Auth(forms.Form):

    username = forms.CharField(
        max_length=18,
        min_length=3,
        required=True,
        label="username",
        widget=forms.TextInput(attrs={'placeholder' : '最大不可超过18字符'}),
        error_messages={'required':'123'})

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'请输入密码'}),
        label="password")


    def clean(self):
        username = self.cleaned_data.get('username', '')
        password = self.cleaned_data.get("password" , '')
        if len(username) > 1:
                raise forms.ValidationError('用户名最大不能超过18')

    # def clean_username(self):
    #     username = self.cleaned_data.get('username', '')
    #     if len(username) > 4:
    #         raise forms.ValidationError('用户名最大不能超过18')
    #     return username