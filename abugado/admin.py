from django.contrib import admin
from .models import Abugado, Cases


# Register your models here.
@admin.register(Abugado)
class AbugadoAdmin(admin.ModelAdmin):
    pass