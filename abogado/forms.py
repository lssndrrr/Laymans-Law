from django import forms
from .models import Abogado
import pandas as pd
from django.core.exceptions import ValidationError 
import os
from django.conf import settings



GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('NB', 'Non-Binary'),
    ('Other', 'Other / Prefer not to say')
    )


class ARegistration(forms.ModelForm):
    first_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_initial = forms.CharField(max_length=3, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(required=True, widget=forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date'}), input_formats=["%Y-%m-%d"])
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    roll_number = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    roll_signed_date = forms.DateField(required=True, widget=forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date'}), input_formats=["%Y-%m-%d"])
    contact_number = forms.RegexField(regex=r'^(09|\+639)\d{9}$', max_length=13, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={
            'invalid': 'Please enter a valid contact number in the format 09XXXXXXXXX or +639XXXXXXXXX.'
        })
    
    class Meta:
        model = Abogado
        fields = ('first_name', 'last_name', 'birth_date', 'gender', 'roll_number', 'roll_signed_date', 'contact_number')
        
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
            if csv_row['f_name'].lower() != first_name.lower() or csv_row['m_init'].lower() != middle_initial.lower() or csv_row['l_name'].lower() != last_name or csv_row['roll_s_date'].lower() != roll_signed_date:
                raise ValidationError("The provided roll number does not match with the other given data. Please re-enter and review carefully.")

        return cleaned_data
    