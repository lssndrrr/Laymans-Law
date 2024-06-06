from django.contrib import admin
from .models import Law, Translations, Summarizations

# Register your models here.

@admin.register(Law)
class LawAdmin(admin.ModelAdmin):
    pass

@admin.register(Summarizations)
class SummarizationsAdmin(admin.ModelAdmin):
    pass

@admin.register(Translations)
class TranslationsAdmin(admin.ModelAdmin):
    pass

# SUGGESTIONS, SMTH LIKE TIKTOK. PREDICTIVE ON WHAT CASES TO TAKE
