from tabnanny import verbose
from django.db import models
from django.conf import settings
from .validators import validate_age
from manggagawa.models import Cases


# Create your models here.    

class Abogado(models.Model):
    ## sign up
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_initial = models.CharField(max_length=4)
    birth_date = models.DateField(validators=[validate_age])
    gender = models.CharField(max_length=20)
    roll_number = models.IntegerField(unique=True) # debating whether or not to turn this into a primary key
    roll_signed_date = models.DateField()
    contact_number = models.CharField(max_length=15)
    
    ## one to one connection with customuser
    abogado_acc = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='abogado_profile', primary_key=True)
    
    ## profile stuff
    verified = models.BooleanField(default=False)
    cases_taken = models.IntegerField(default=0)
    # wiki_contribs
    # optional! needs new library (Pillow) profile_pic = models.ImageField()
    
class Handles(models.Model):
    abogado = models.ForeignKey(to=Abogado, on_delete=models.CASCADE)
    case_id = models.OneToOneField(to=Cases, on_delete=models.CASCADE)
    date_taken = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)
    date_closed = models.DateField(null=True, blank=True)