from django import forms
from .models import Abugado

GENDER_CHOICES = (
    ('f', 'Female'),
    ('m', 'Male'),
    ('nb', 'Non-Binary'),
    ('other', 'Other/Prefer not to say')
    )


class ARegistration(forms.ModelForm):
    first_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_initial = forms.CharField(max_length=3, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    contact_number = forms.RegexField(regex=r'^(09|\+639)\d{9}$', max_length=13, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Abugado
        fields = ('first_name', 'last_name', 'gender', 'contact_number')
    