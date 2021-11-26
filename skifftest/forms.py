from django import forms

class S_UserAuthForm(forms.Form):
    user_name = forms.CharField(label = 'User name:', max_length = 50)
    user_password = forms.CharField(label = 'Password:', max_length = 30, widget = forms.PasswordInput())