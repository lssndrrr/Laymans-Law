from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    # user_type = forms.CharField(widget=forms.HiddenInput, disabled=True, required=False)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password-input', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'cpassword-input', 'placeholder': 'Confirm Password'}),
    )
    
    class Meta:
        model = CustomUser
        fields = ('email',)
        
class ChangePWForm(forms.Form):
    current_password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password-input', 'placeholder': 'Old Password'}),
        )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'cpassword-input', 'placeholder': 'Enter New Password'}),
    )
    new_password2 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'cpassword-input', 'placeholder': 'Confirm New Password'}),
    )
    class Meta:
        fields = ['password1', 'password2']
    
    
class DeleteAccForm(forms.Form):
    current_password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password-input', 'placeholder': 'Old Password'}),
        )
    confirm = forms.BooleanField(label="This action is irreversible. Are you sure you want to proceed?", widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    class Meta:
        fields = ['current_password', 'confirm']
