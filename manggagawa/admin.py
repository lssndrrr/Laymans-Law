from django.contrib import admin
from .models import Manggagawa

# Register your models here.

@admin.register(Manggagawa)
class ManggagawaAdmin(admin.ModelAdmin):
    pass