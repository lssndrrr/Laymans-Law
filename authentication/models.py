from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUser(AbstractUser):
    pass

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email provided is incorrect.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USER_TYPE_CHOICES = (
        ('abugado', 'Abugado'),
        ('manggagawa', 'Manggagawa')
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    
    def is_lawyer(self):
        return self.user_type == 'abugado'

    def is_laymen(self):
        return self.user_type == 'manggagawa'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']
    objects = CustomUserManager()