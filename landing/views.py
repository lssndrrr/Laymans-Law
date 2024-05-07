from django.shortcuts import render, redirect
from abogado.models import Abogado

# Create your views here.

def landing(request):
    if request.method == "GET":
        return render(request, "landing/landing_page.html")
    return render(request, "landing/landing_page.html")