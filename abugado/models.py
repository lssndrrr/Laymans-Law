from django.db import models

# Create your models here.

class AbugadoAcc(models.Model):
    account_created = models.DateField(auto_now_add=True)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=200)
    # optional! needs new library (Pillow) profile_pic = models.ImageField()

class Abugado(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    license_number = models.CharField(max_length=200)
    sex = models.CharField(max_length=2)
    contact_number = models.CharField(max_length=12)
    abugado_acc = models.OneToOneField(to=AbugadoAcc, on_delete=models.CASCADE, primary_key=True)
    
class Cases(models.Model):
    abugado = models.ForeignKey(to=Abugado, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    done = models.BooleanField()
    date_added = models.DateField(auto_now_add=True)