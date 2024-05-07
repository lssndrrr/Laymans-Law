from django.core.exceptions import ValidationError
from datetime import date


## VALIDATORS

def validate_age(bdate):
    today = date.today()
    if today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day)) >= 18:
        return bdate
    else:
        raise ValidationError("You have to be 18 to sign up.")