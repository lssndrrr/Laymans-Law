from django.shortcuts import render, redirect
from abogado.models import Abogado
from abogado.views import Profile

# Create your views here.

def landing(request):
    if request.method == "GET" and request.user.is_authenticated:
        return redirect(Profile, request.user.abogado.roll_number)
    else:
        return render(request, "landing/landing_page.html")        
    