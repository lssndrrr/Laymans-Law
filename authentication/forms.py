from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # user_type = forms.CharField(widget=forms.HiddenInput, disabled=True, required=False)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password-input'}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'cpassword-input'}),
    )
    
    class Meta:
        model = CustomUser
        fields = ('email',)
