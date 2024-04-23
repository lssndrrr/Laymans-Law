from django.db import models

# Create your models here.

class Manggagawa(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    license_number = models.CharField(max_length=200)
    sex = models.CharField(max_length=2)
    contact_number = models.CharField(max_length=12)
    email_add = models.CharField(max_length=200)
    password = models.CharField(max_length=200)