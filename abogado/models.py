from tabnanny import verbose
from django.db import models
from django.conf import settings
from .validators import validate_age


# Create your models here.    

class Abogado(models.Model):
    ## sign up
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_initial = models.CharField(max_length=2)
    birth_date = models.DateField(validators=[validate_age])
    gender = models.CharField(max_length=20)
    roll_number = models.IntegerField() # debating whether or not to turn this into a primary key
    roll_signed_date = models.DateField()
    contact_number = models.CharField(max_length=15)
    
    ## one to one connection with customuser
    abogado_acc = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='abogado_profile', primary_key=True)
    
    ## profile stuff
    verified = models.BooleanField(default=False)
    # cases_taken
    # wiki_contribs
    # optional! needs new library (Pillow) profile_pic = models.ImageField()
    
class Cases(models.Model):
    abogado = models.ForeignKey(to=Abogado, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    done = models.BooleanField()
    date_added = models.DateField(auto_now_add=True)