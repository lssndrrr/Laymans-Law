from django.db import models
from django.conf import settings
from .validators import validate_age

# custom field
class ManggagawaID(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['editable'] = False
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)
    
    def pre_save(self, model_instance, add):
        if add:
            last_instance = model_instance.__class__.objects.order_by('-m_id').first()
            if last_instance:
                value = last_instance.m_id + 1
            else:
                value = 1 + 1898 # year of independence
            return value
        else:
            return super().pre_save(model_instance, add)

# Create your models here.

class Manggagawa(models.Model):
    ## sign up
    m_id = ManggagawaID()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_initial = models.CharField(max_length=4)
    birth_date = models.DateField(validators=[validate_age])
    gender = models.CharField(max_length=2)
    contact_number = models.CharField(max_length=12)
    trabaho = models.CharField(max_length=200)
    
    ## one to one connection with customuser
    manggagawa_acc = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='manggagawa_profile', primary_key=True)
    
    ## profile stuff
    # optional! needs new library (Pillow) profile_pic = models.ImageField()

class Cases(models.Model):
    case_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    done = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    raised_by = models.ForeignKey(to=Manggagawa, on_delete=models.CASCADE, related_name='cases')