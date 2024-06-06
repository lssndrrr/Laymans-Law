from django import forms

from authentication.models import CustomUser
from .models import Abogado
import pandas as pd
from django.core.exceptions import ValidationError 
import os
from django.conf import settings
import logging




logger = logging.getLogger(__name__)


GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('NB', 'Non-Binary'),
    ('Other', 'Other / Prefer not to say')
    )


class ARegistration(forms.ModelForm):
    first_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    middle_initial = forms.CharField(max_length=3, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Initial'}))
    birth_date = forms.DateField(required=True, widget=forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date', 'class':'form-control'}), input_formats=["%Y-%m-%d"])
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    roll_number = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Roll Number'}))
    roll_signed_date = forms.DateField(required=True, widget=forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date', 'class':'form-control'}), input_formats=["%Y-%m-%d"])
    contact_number = forms.RegexField(regex=r'^(09|\+639)\d{9}$', max_length=13, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}), error_messages={
            'invalid': 'Please enter a valid contact number in the format 09XXXXXXXXX or +639XXXXXXXXX.'
        })
    
    class Meta:
        model = Abogado
        fields = ('first_name', 'middle_initial', 'last_name', 'birth_date', 'gender', 'roll_number', 'roll_signed_date', 'contact_number')
        
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        middle_initial = cleaned_data.get('middle_initial')
        last_name = cleaned_data.get('last_name')
        roll_signed_date = cleaned_data.get('roll_signed_date')
        roll_number = cleaned_data.get('roll_number')

        if first_name and middle_initial and last_name and roll_signed_date and roll_number:
            file = os.path.join(settings.BASE_DIR, 'static', 'abogado', 'Lawyers_List.csv') ## changed when csv is updated
            try:
                df = pd.read_csv(file, parse_dates=['roll_s_date'])
            except FileNotFoundError:
                raise ValidationError("CSV file not found.")

            if roll_number not in df['roll_no'].values:
                raise ValidationError("The roll number provided does not belong to an existing lawyer.")
            
            csv_row = df[df['roll_no'] == roll_number].iloc[0]

            if csv_row['f_name'] != first_name.upper() or csv_row['m_init'] != middle_initial.upper() or csv_row['l_name'] != last_name.upper() or csv_row['roll_s_date'].date() != roll_signed_date:
                raise ValidationError("The provided roll number does not match with the other given data. Please re-enter and review carefully.")

        return cleaned_data
    
class ALogin(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-inputs','placeholder':'Email'}))
    user_type = forms.CharField(widget=forms.HiddenInput, disabled=True)
    password = forms.CharField(required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-inputs', 'id': 'password-input','placeholder':'Password'}),
    )
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'user_type')
    