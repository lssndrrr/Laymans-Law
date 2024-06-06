from calendar import c
from django import forms

from authentication.models import CustomUser
from .models import Cases, Manggagawa
from django.core.exceptions import ValidationError 
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('NB', 'Non-Binary'),
    ('Other', 'Other / Prefer not to say')
    )

class MRegistration(forms.ModelForm):
    first_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    middle_initial = forms.CharField(max_length=3, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Initial'}))
    birth_date = forms.DateField(required=True, widget=forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date', 'class': 'form-control'}), input_formats=["%Y-%m-%d"])
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    contact_number = forms.RegexField(regex=r'^(09|\+639)\d{9}$', max_length=13, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}), error_messages={
            'invalid': 'Please enter a valid contact number in the format 09XXXXXXXXX or +639XXXXXXXXX.', 'placeholder': 'Contact Number'
        })
    trabaho = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation'}))
    
    class Meta:
        model = Manggagawa
        fields = ('first_name', 'middle_initial', 'last_name', 'birth_date', 'gender', 'contact_number', 'trabaho')


class MLogin(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    user_type = forms.CharField(widget=forms.HiddenInput, disabled=True)
    password = forms.CharField(required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password-input', 'placeholder':'Password'}), error_messages={
            'invalid': 'This user is not registered. Please proceed to sign up.'
        })
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'user_type')
        
class SubmitCase(forms.ModelForm):
    name = forms.CharField(max_length=500, widget=forms.TextInput(attrs={}))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={}))
    
    class Meta:
        model = Cases
        fields = ['name', 'description']