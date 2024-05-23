from django.shortcuts import render
from .models import Law, Summarizations, Translations
from django.http import HttpResponse


# Create your views here.
def lawList(request):
    laws = Law.objects.all()
    return render(request, "wiki/laborlaws.html", {"laws": laws})

def prelimW(request):
    if request.method == "GET":
        return render(request, "wiki/wiki-prelim.html")
    return render(request, "wiki/wiki-prelim.html")