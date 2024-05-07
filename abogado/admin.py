from django.contrib import admin
from .models import Abogado, Cases


# Register your models here.
@admin.register(Abogado)
class AbogadoAdmin(admin.ModelAdmin):
    pass