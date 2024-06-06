from django.db import models
from abogado.models import Abogado

# Create your models here.

class Law(models.Model):
    index = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1000)
    code = models.CharField(max_length=1000)
    fullLaw = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.code}: {self.name}"
        

class Translations(models.Model):
    law = models.ForeignKey(to=Law, on_delete=models.CASCADE)
    translation_id = models.AutoField(primary_key=True)
    Bisaya_Translation = models.CharField(max_length=5000)
    Tagalog_Translation = models.CharField(max_length=5000)
    Waray_Translation = models.CharField(max_length=5000)
    def Get_Translation(self, language):
        if language == "Bisaya":
            return self.Bisaya_Translation
        elif language == "Tagalog":
            return self.Tagalog_Translation
        elif language == "Waray":
            return self.Waray_Translation
        
class TranslationInfo(models.Model):
    submit_date = models.DateField(auto_now_add=True)
    translation_id = models.OneToOneField(to=Translations, on_delete=models.CASCADE)
    abogado = models.OneToOneField(to=Abogado, on_delete=models.CASCADE)
    
class TranslationVerified(models.Model):
    translation_id = models.ManyToManyField(to=Translations)
    abogado = models.ManyToManyField(to=Abogado) # unsure
    verify_date = models.DateField(auto_now_add=True)


class Summarizations(models.Model):
    summary_id = models.AutoField(primary_key=True)
    law = models.ForeignKey(to=Law, on_delete=models.CASCADE)
    def __str__(self):
        return self.Summary
    Summary = models.CharField(max_length=5000)
    
class SummaryInfo(models.Model):
    submit_date = models.DateField(auto_now_add=True)
    abogado = models.OneToOneField(to=Abogado, on_delete=models.CASCADE)
    summary_id = models.OneToOneField(to=Summarizations, on_delete=models.CASCADE)
    
class SummaryVerified(models.Model):
    summary_id = models.ManyToManyField(to=Summarizations)
    abogado = models.ManyToManyField(to=Abogado) # unsure
    verify_date = models.DateField(auto_now_add=True)

