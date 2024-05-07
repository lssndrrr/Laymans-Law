from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email provided is incorrect.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'admin')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    id = None
    email = models.EmailField(unique=True, primary_key=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    registered = models.BooleanField(default=False)
    
    USER_TYPE_CHOICES = (
        ('abogado', 'Abogado'),
        ('manggagawa', 'Manggagawa'),
        ('admin', 'Admin')
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    
    def is_lawyer(self):
        return self.user_type == 'abogado'

    def is_laymen(self):
        return self.user_type == 'manggagawa'
    
    def is_registered(self):
         return self.registered

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']
    objects = CustomUserManager()