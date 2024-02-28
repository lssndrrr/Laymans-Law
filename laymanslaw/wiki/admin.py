from django.contrib import admin
from .models import Law, Translations, Summarizations

# Register your models here.

@admin.register(Law)
class LawAdmin(admin.ModelAdmin):
    pass

