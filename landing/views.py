from django.shortcuts import render, redirect
from abugado.models import Abugado

# Create your views here.

def landing(request):
    if request.method == "GET":
        return render(request, "landing/landing_page.html")
    return render(request, "landing/landing_page.html")
