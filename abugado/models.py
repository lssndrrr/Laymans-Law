from django.db import models
from django.conf import settings

# Create your models here.    

class Abugado(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_initial = models.CharField(max_length=2)
    license_number = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)
    abugado_acc = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    # optional! needs new library (Pillow) profile_pic = models.ImageField()
    
class Cases(models.Model):
    abugado = models.ForeignKey(to=Abugado, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    done = models.BooleanField()
    date_added = models.DateField(auto_now_add=True)