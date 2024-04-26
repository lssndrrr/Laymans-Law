from django.db import models

# Create your models here.

class Law(models.Model):
    name = models.CharField(max_length=1000)
    code = models.CharField(max_length=1000)
    fullLaw = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.code}: {self.name}"
        

class Translations(models.Model):
    law = models.ForeignKey(to=Law, on_delete=models.CASCADE)
    Bisaya_Translation = models.CharField(max_length=1000)
    Tagalog_Translation = models.CharField(max_length=1000)
    Waray_Translation = models.CharField(max_length=1000)
    def Get_Translation(self, language):
        if language == "Bisaya":
            return self.Bisaya_Translation
        elif language == "Tagalog":
            return self.Tagalog_Translation
        elif language == "Waray":
            return self.Waray_Translation


class Summarizations(models.Model):
    law = models.ForeignKey(to=Law, on_delete=models.CASCADE)
    def __str__(self):
        return self.Summary
    Summary = models.CharField(max_length=1000)

