from django.contrib import admin
from .models import Law, Translations, Summarizations

# Register your models here.

@admin.register(Law, Translations, Summarizations)
class LawAdmin(admin.ModelAdmin):
    pass


# SUGGESTIONS, SMTH LIKE TIKTOK. PREDICTIVE ON WHAT CASES TO TAKE
