from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', required=False)
    last_name = forms.CharField(label='Last Name', required=False)
    email = forms.EmailField(max_length=200, help_text='Required', required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# class EditUserForm2(forms.ModelForm):
#
#
#     class Meta:
#         model = User
#         fields = '__all__'
