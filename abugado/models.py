from django.db import models

# Create your models here.
class Abugado(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    license_number = models.CharField(max_length=200)
    sex = models.CharField(max_length=2)
    contact_number = models.CharField(max_length=12)
    email_add = models.CharField(max_length=200)
    
class Cases(models.Model):
    abugado = models.ForeignKey(to=Abugado, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    done = models.BooleanField()
    date_added = models.DateField(auto_now_add=True)