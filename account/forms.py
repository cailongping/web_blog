from django import forms
from django.contrib.auth.models import User
from .models import UserInfo

class RegisterForm(forms.ModelForm):
    """Form definition for Register."""
    username = forms.CharField(label="用户名", widget=forms.TextInput(
        attrs={'class':'input is-radiusless is-shadowless'}
    ))
    email = forms.CharField(label="邮箱", widget=forms.EmailInput(
        attrs={'class':'input is-radiusless is-shadowless'}
    ))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(
        attrs={'class':'input is-radiusless is-shadowless'}
    ))
    password2 = forms.CharField(label="再次输入密码", widget=forms.PasswordInput(
        attrs={'class':'input is-radiusless is-shadowless'}
    ))

    class Meta:
        """Meta definition for Registerform."""
        model = User
        fields = ('username','email')


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("您输入的两次密码不一致！")
    
        return password2


class UserInfoForm(forms.ModelForm):
    """Form definition for UserInfo."""
    phone = forms.CharField(label="手机号", widget=forms.TextInput(
        attrs={'class':'input is-radiusless is-shadowless'}
    ))

    class Meta:
        """Meta definition for UserInfoform."""

        model = UserInfo
        fields = ('phone',)
