from django.contrib import admin
from .models import ProfileM

# Register your models here.

@admin.register(ProfileM)
class ProfileMAdmin(admin.ModelAdmin):
    pass